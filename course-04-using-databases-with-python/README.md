# 🚀 **Course 04 – Using Databases with Python**

This folder contains all my scripts, datasets, SQLite files, and course certificate from **Course 4** of the *Python for Everybody* specialization on Coursera, taught by [Dr. Charles Severance (Dr. Chuck)](https://www.py4e.com/).

This course marked my transition from simple scripting into **real backend logic**, where Python meets SQL to build scalable, queryable, structured data systems — all under my brand **1FahadShah**.

---

## 🧠 What I Learned

This course focused on integrating **Python with SQL (SQLite3)** to store, retrieve, transform, and analyze structured data — forming the core of modern backend and automation stacks.

### ✅ Topics Covered

#### 🛠️ SQL Fundamentals in Python
- Connecting to SQLite databases via `sqlite3`
- Creating tables, inserting records, and executing SQL queries
- Using `SELECT`, `JOIN`, `INSERT OR IGNORE`, and `ORDER BY`

#### 🔌 Data Source Integration
- Ingesting data from **CSV files** using the `csv` module
- Parsing **JSON files** into normalized tables
- Storing external web data into SQLite via `urllib`

#### 🧩 Database Schema Design
- Designing relational tables: `User`, `Course`, `Member`, `Artist`, `Album`, `Track`, `Genre`
- Normalizing data to prevent redundancy
- Defining primary keys and foreign key relations

#### 🧠 Real SQL Queries & Joins
- Joining across multiple tables
- Building analytics logic (e.g. `SELECT hex(...)`, aggregation, role filters)
- Transforming raw email text to domain counts (ETL-style)

---

## 📁 Folder Contents
```bash
course-04-using-databases-with-python/
├── README.md                         # Course 4 project documentation
├── counting-email-in-database.py     # Extract domains from raw mail & store counts
├── emaildb.sqlite                    # SQLite DB storing org-level email counts
├── json_roster_to_db.py              # Parse JSON → Normalize into 3-table DB
├── music_tracks_csv_to_db.py         # Parse CSV → Populate artist/genre/album/track schema
├── music_tracks_db.sqlite            # DB with music tracks loaded from CSV
├── roster_data.json                  # Source JSON file with user/course/role
├── roster_data_db.sqlite             # DB with User/Course/Member relations
├── trackdb.db                        # Secondary DB for track join analysis
├── tracks.csv                        # Raw music metadata for ETL
├── tracks.py                         # SQL joins across Track/Album/Artist/Genre
├── course-04-self-study-notes.pdf    # Handwritten Notes
└── course-04-certificate.pdf         # Coursera Certificate
```
---

## 🧰 Tools Used

- Python 3.x  
- SQLite 3  
- `sqlite3`, `csv`, `json`, `os`, `urllib`  
- Git + GitHub  
- `.db`, `.csv`, `.json` inputs to simulate real-world ingestion  

---

## ✍️ Notes

- This course taught me to think like a **data backend engineer**: model relationships, normalize inputs, write clean SQL, and control everything through Python.
- Every script here reflects a **real-world mini pipeline** — parsing, transforming, and persisting data from raw source to relational form.
- My automation and AI pipelines moving forward will be **database-backed** — and this is the foundation.

---

## 🌐 Connect with Me

- [LinkedIn](https://linkedin.com/in/1fahadshah)  
- [GitHub](https://github.com/1fahadshah)  
- [Medium](https://medium.com/@1fahadshah)  
- [X / Twitter](https://twitter.com/1fahadshah)

> 📌 This is part of my larger roadmap to master Python for AI, automation, and backend development.  
> *Code moves data. SQL gives it structure. I'm here to dominate both.* — **1FahadShah**



