import sqlite3
import os

DB_PATH = os.path.join("db","krawlix.sqlite")

def create_table():
    # Creates knowledge table if it doesn't exists

    connect = sqlite3.connect(DB_PATH)
    cur = connect.cursor()
    cur.execute('''
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

def save_summary_to_file(summary_data, folder="summaries"):
    # save summary to text file inside summaries/folder

    if not os.path.exists(folder):
        os.makedirs(folder)

    filename = summary_data["topic"].replace(" ", "_") + ".txt"
    filepath = os.path.join(folder, filename)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(summary_data["summary"])