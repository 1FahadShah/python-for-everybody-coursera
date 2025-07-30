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


def insert_summary(summary_data):
    # Insert summary into knowledge table

    connect = sqlite3.connect(DB_PATH)
    cur = connect.cursor()

    cur.execute('''
        INSERT INTO knowledge (topic, summary, source, source_url, created_at)
        VALUES (?, ?, ?, ?, ?)
    ''',
    (
        summary_data['topic'],
        summary_data['summary'],
        summary_data['source'],
        summary_data['source_url'],
        summary_data['created_at']
    ))

    connect.commit()
    connect.close()