import sqlite3
import csv
from pathlib import Path

# I use the pathlib for cross-platform handling
db_path = Path("pubs.db")
pubs_csv = Path("data/pubs.csv")
tags_csv = Path("data/tags.csv")

# Create tables
def create_tables():
    with sqlite3.connect(db_path) as conn:
        c = conn.cursor()

        c.execute("""
        DROP TABLE IF EXISTS pubs;
        """)

        c.execute("""
                DROP TABLE IF EXISTS tags;
        """)

        c.execute("""
        CREATE TABLE pubs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL
        );
        """)

        c.execute("""
        CREATE TABLE tags (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            pub_id INTEGER NOT NULL,
            tags TEXT NOT NULL,
            FOREIGN KEY (pub_id) REFERENCES pubs (id)
        );
        """)
        conn.commit()

# Load the pub and tags data from the csv files
def load_csv():
    with sqlite3.connect(db_path) as conn:
        c = conn.cursor()

        # Load pubs
        with open(pubs_csv, newline='', encoding ="utf-8") as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                c.execute("INSERT OR IGNORE INTO pubs (name) VALUES (?);", (row[1],))

        # Load tags
        with open(tags_csv, newline='', encoding="utf-8") as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                pub_id, tags = row
                c.execute("INSERT OR IGNORE INTO tags (pub_id, tags) VALUES (?, ?);", (pub_id, tags))
    conn.commit()

if __name__ == "__main__":
    create_tables()
    load_csv()
    print("Database setup complete!")