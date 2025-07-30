import sqlite3
import os

DB_PATH = os.path.join("db","krawlix.sqlite")

def create_table():
    # Creates knowledge table if it doesn't exists

    connect = sqlite.connect(DB_PATH)
    cur = connect.cursor()
    cur.exceute('''
        CREATE TABLE IF NOT EXISTS knowledge(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            topic TEXT,
            summary TEXT,
            source TEXT,
            source_url TEXT,
            created_at TEXT
        )
    ''')

    connect.commit()
    connect.close()