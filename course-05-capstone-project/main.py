import sys
import os
from crawler.fetch import fetch_summary
from crawler.db_writer import create_table, insert_summary, save_summary_to_file
from crawler.utils import get_timestamp
from datetime import datetime

def crawl_topics(topics_file_path):
    """
    this function reads topics from a text file
    and fetches summaries for each of them.
    """

    if not os.path.exists(topics_file_path):
        print("File not found:", topics_file_path)
        return

    create_table()

    topics = []

    # this will get topics from file and append it to 'topics' list
    with open(topics_file_path, "r") as file:
        for line in file:
            line = line.strip()
            if line != "":
                topics.append(line)

    for topic in topics:
        print("Fetching Summary for: ",topic)
        result = fetch_summary(topic)

        if result:
            result["created_at"] = get_timestamp()
            insert_summary(result)
            save_summary_to_file(result)
            print(f"Summary for {topic} saved in DB")
        else:
            print("No Summary found for:", topic)
            with open("failed_topics.txt","a",encoding="utf-8") as fail_log:
                fail_log.write(topic + "\n")


#manage inputs from CLI

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py data/topics.txt")
    else:
        topics_file = sys.argv[1]
        crawl_topics(topics_file)