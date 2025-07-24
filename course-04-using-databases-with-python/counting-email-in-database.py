import sqlite3
import urllib.request
import os

db_path = os.path.join(os.path.dirname(__file__), 'emaildb.sqlite')
connect = sqlite3.connect(db_path)
cursor = connect.cursor()

cursor.execute('DROP TABLE IF EXISTS Counts')
cursor.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')
url = input("Enter URL:").strip()

response = urllib.request.urlopen(url)
data = response.read().decode()

response.close()

lines = data.splitlines()
for line in lines:
    if not line.startswith('From '):
        continue
    pieces = line.split()
    email = pieces[1]
    org = email.split('@')[1]

    cursor.execute('SELECT count from Counts WHERE org = ?',(org,))
    row = cursor.fetchone()

    if row is None:
        cursor.execute('INSERT INTO Counts(org, count) VALUES (?, 1)',(org,))
    else:
        cursor.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',(org,))

connect.commit()
for row in cursor.execute('SELECT * FROM Counts'):
    print(row)

cursor.close()
connect.close()