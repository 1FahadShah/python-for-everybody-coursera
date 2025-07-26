import sqlite3
import os
import csv

current_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(current_dir, 'music_tracks_db.sqlite')

connect = sqlite3.connect(db_path)
cur = connect.cursor()

cur.executescript('''
CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY 
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);
''')

# load CSV to DB 

csv_file = os.path.join(current_dir, 'tracks.csv')

with open(csv_file, 'r') as csvfile: 
    reader = csv.reader(csvfile)
    
    for row in reader:
        if len(row) < 7:
            continue

        title = row[0].strip()
        artist = row[1].strip()
        album = row[2].strip()
        length = int(row[3].strip())
        ratings = int(row[4].strip())
        count = int(row[5].strip())
        genre = row[6].strip()

        cur.execute('INSERT OR IGNORE INTO Artist(name) VALUES(?)',(artist,))
        cur.execute('SELECT id FROM Artist WHERE name = ?', (artist,))
        artist_id = cur.fetchone()[0]

        cur.execute('INSERT OR IGNORE INTO Genre(name) VALUES(?)',(genre,))
        cur.execute('SELECT id FROM Genre WHERE name = ?', (genre,))
        genre_id = cur.fetchone()[0]

        cur.execute('INSERT OR IGNORE INTO Album(artist_id, title) VALUES(?,?)',(artist_id, album))
        cur.execute('SELECT id FROM Album WHERE title = ?', (album,))
        album_id = cur.fetchone()[0]

        cur.execute('''
        INSERT OR IGNORE INTO Track(title, genre_id, album_id, len, rating, count) 
        VALUES(?, ?, ?, ?, ?, ?)''',(title, genre_id, album_id, length, ratings, count))
        
        

connect.commit()
print("Succesfully Loaded CSV to DB!!")
print("Joined Table : ")
cur.execute('''
SELECT Track.title, Artist.name, Album.title, Genre.name 
    FROM Track JOIN Genre JOIN Album JOIN Artist 
    ON Track.genre_id = Genre.ID and Track.album_id = Album.id 
        AND Album.artist_id = Artist.id
    ORDER BY Artist.name LIMIT 3
''')

rows = cur.fetchall()
for row in rows:
    title, artist, album, genre = row
    print(f"{title} | {artist} | {album} | {genre}")




    
    


