import sqlite3
import os

# Get the directory where this script is saved
script_dir = os.path.dirname(os.path.abspath(__file__))

# full path to the database file
db_path = os.path.join(script_dir, "trackdb.db")


connect = sqlite3.connect(db_path)
cursor = connect.cursor()

print("Displat Track Table: ")
for row in cursor.execute('SELECT * FROM track'):
    print(row)


print("\n\nCombine Table Artist and Genre: ")
for row in cursor.execute('SELECT album.id,album.title,artist.name FROM album join artist on album.artist_id = artist.id'):
    print(row)


cursor.close()
connect.close()