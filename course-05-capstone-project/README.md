# 🚀 **Course 05 – Capstone Project**

## 🧠 KRAWLIX — Knowledge Crawler

KRAWLIX is a command-line knowledge extraction tool that fetches topic summaries from public sources like **DuckDuckGo** and **Wikipedia**, then stores them in both a local SQLite database and as `.txt` files.  
Designed entirely with **Python Standard Library only**, this is a real-world, **Portfolio Ready** capstone project built to demonstrate practical Python, API integration, and structured data storage.

---

## 🚀 Why I Built This

As part of my **Python for Everybody** specialization capstone, I wanted to go beyond toy problems and build a real, modular, CLI-based tool that:

- ✅ Integrates public APIs  
- ✅ Handles failures gracefully  
- ✅ Stores structured data  
- ✅ Uses zero external libraries  
- ✅ Feels like the base layer of a real AI assistant  

> This is **KRAWLIX** — a production-grade CLI tool that showcases my ability to design structured, scalable systems at the intersection of Python, data, and infrastructure.

---

## 🧠 Features

- 🔍 **Smart Fetching System**  
  - DuckDuckGo Instant Answer API (primary source)  
  - Wikipedia REST API (fallback if DuckDuckGo fails)

- 💡 **Built-in Stability Layer**  
  - Gracefully handles failed requests with structured `try-except` blocks  
  - Automatically switches to Wikipedia if DuckDuckGo returns empty  
  - Logs unresolved topics to `failed_topics.txt` for debugging

- 🗃 **Dual Output Storage**  
  - Structured entries into SQLite (`db/krawlix.sqlite`)  
  - Plaintext `.txt` files saved in `summaries/` folder

- 🧱 **Zero Dependency Architecture**  
  - Built using only: `urllib`, `json`, `sqlite3`, `os`, `sys`, `datetime`  
  - Fully modular design with clean separation of logic

- 🖥 **CLI Native**  
  - Accepts topic list via `data/topics.txt`  
  - Executed via `python main.py <file_path>`  
  - Minimal setup, fully local, cross-platform


---

## 🎥 Demo

![Krawlix CLI Demo](demo/krawlix-demo.gif)

> This CLI tool fetches structured summaries via DuckDuckGo/Wikipedia and stores them in both `.txt` and `.sqlite` formats — using only Python Standard Library.


## 🛠 Tech Stack


| Layer      | Tool                                |
| ---------- | ----------------------------------- |
| Language   | Python 3 (Standard Library Only)    |
| Storage    | SQLite3, File I/O (`.txt`)          |
| APIs       | DuckDuckGo, Wikipedia REST          |
| Interface  | CLI (`python main.py <topics.txt>`) |
| OS Tested  | Windows 11 + Python 3.11            |
| Versioning | Git + GitHub                        |


  
---

## 📂 Folder Contents

```bash
course-05-capstone-krawlix/
├── crawler/                     # API fetching, DB writing, utility modules
│   ├── fetch.py
│   ├── db_writer.py
│   └── utils.py
├── data/                        # Input topic list
│   └── topics.txt
├── db/                          # SQLite database
│   └── krawlix.sqlite
├── demo/                        # Demo GIF and visuals
│   └── krawlix-demo.gif
├── export/                      # (Optional) Export features (reserved)
├── summaries/                   # Saved topic summaries as text files
│   └── <topic>.txt
├── README.md                    # Project documentation
├── failed_topics.txt            # Log of topics not found
├── main.py                      # CLI entry point
├── requirements.txt             # Empty (used for environment consistency)
├── test.py                      # Manual test runner

```

---

## 🛠️ How It Works

### Step 1: Add topics to `data/topics.txt`

```text
Python programming
Artificial Intelligence
Generative AI
```

### Step 2: Run the crawler

```bash
python main.py data/topics.txt
```

### Step 3: Output

```text
summaries/Python_programming.txt        ✔️
summaries/Artificial_Intelligence.txt   ✔️
failed_topics.txt → NonexistentTopic123 ❌
```

---

## 📊 What This Project Proves

* End-to-end knowledge ingestion using legal public APIs
* Clean code separation across modules
* Text + database storage via `sqlite3` and file I/O
* Scalable system design
* CLI-based tool thinking aligned with Automation Engineering

---


## 📝 Notes

* This is a **true capstone**: designed, written, and tested independently.
* The architecture is intentionally clean, but extensible.
* Future versions can add Markdown export, CLI arguments, or integration into RAG pipelines.

> 🧠 This project demonstrates how clean scripting, modular thinking, and public APIs can produce production-grade tools — even within constraints.

---

## 🌐 Connect with Me

* [LinkedIn](https://linkedin.com/in/1fahadshah)
* [GitHub](https://github.com/1fahadshah)
* [Medium](https://medium.com/@1fahadshah)
* [X / Twitter](https://twitter.com/1fahadshah)



> 📌 This project aligns with my long-term path in Python — from automation to AI Systems.  
> *I build tools that scale knowledge, not just code.* — **1FahadShah**

