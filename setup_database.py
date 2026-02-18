import sqlite3
import os

os.makedirs("data", exist_ok=True)

conn = sqlite3.connect("data/sample.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    month TEXT,
    revenue INTEGER
)
""")

cursor.executemany(
    "INSERT INTO sales VALUES (?, ?)",
    [
        ("Jan", 1000),
        ("Feb", 1500),
        ("Mar", 2000)
    ]
)

conn.commit()
conn.close()