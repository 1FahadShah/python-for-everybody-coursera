import os
import json
import sqlite3

current_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(current_dir, 'roster_data_db.sqlite')

connect = sqlite3.connect(db_path)
cur = connect.cursor()

cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User (
    id     INTEGER PRIMARY KEY,
    name   TEXT UNIQUE
);

CREATE TABLE Course (
    id     INTEGER PRIMARY KEY,
    title  TEXT UNIQUE
);

CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
    role        INTEGER,
    PRIMARY KEY (user_id, course_id)
)
''')

json_dir = os.path.join(current_dir, 'roster_data.json')
json_file = open(json_dir).read()
json_data = json.loads(json_file)


for entry in json_data:
    name = entry[0]
    title = entry[1]
    role = entry[2]

    cur.execute('INSERT OR IGNORE INTO User(name) VALUES(?)',(name,))
    cur.execute('SELECT id FROM User WHERE name = ?',(name,))
    user_id = cur.fetchone()[0]

    cur.execute('INSERT OR IGNORE INTO Course(title) VALUES(?)', (title,))
    cur.execute('SELECT id FROM Course WHERE title = ?', (title,))
    course_id = cur.fetchone()[0]

    cur.execute('INSERT OR IGNORE INTO Member(user_id, course_id, role) VALUES(?, ?, ?)', (user_id, course_id, role))
    cur.execute('SELECT id FROM Course WHERE title = ?', (title,))
     

connect.commit()

print('Data from JSON added to DB')

print('''Performing:\n
SELECT User.name,Course.title, Member.role FROM 
    User JOIN Member JOIN Course 
    ON User.id = Member.user_id AND Member.course_id = Course.id
    ORDER BY User.name DESC, Course.title DESC, Member.role DESC LIMIT 2;

''')

cur.execute('''
SELECT User.name,Course.title, Member.role FROM 
    User JOIN Member JOIN Course 
    ON User.id = Member.user_id AND Member.course_id = Course.id
    ORDER BY User.name DESC, Course.title DESC, Member.role DESC LIMIT 2;
''')


rows = cur.fetchall()
print("Succesful! Tables Joined: ")

for row in rows:
    name, title, role = row
    print(f"{name} | {title} | {role}")



print('''\n\nNow Performing:\n
SELECT 'XYZZY' || hex(User.name || Course.title || Member.role ) AS X FROM 
    User JOIN Member JOIN Course 
    ON User.id = Member.user_id AND Member.course_id = Course.id
    ORDER BY X LIMIT 1;

''')

cur.execute('''
SELECT 'XYZZY' || hex(User.name || Course.title || Member.role ) AS X FROM 
    User JOIN Member JOIN Course 
    ON User.id = Member.user_id AND Member.course_id = Course.id
    ORDER BY X LIMIT 1;
''')

row = cur.fetchone()
print("Successful! Tables Joined")
print(f"Code : {row[0]}")








