import sqlite3
import time
from random import randint

DB_PATH = "/Users/ayaazeari/cybersecurity/DB/orders.db"

def simulate_activity():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    while True:
        # random order
        c.execute("INSERT INTO orders (order_id, amount) VALUES (?, ?)", (randint(1000, 9999), randint(10, 500)))
        c.execute("INSERT INTO reviews (review_id, comment) VALUES (?, ?)", (randint(1, 100), "Sample review"))
        conn.commit()
        print("Inserted data into orders and reviews tables.")
        # Wait for 10 sec
        time.sleep(10)
if __name__ == "__main__":
    simulate_activity()
