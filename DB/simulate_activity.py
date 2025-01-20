import sqlite3
import time
from random import randint

dbpath = "/Users/ayaazeari/cybersecurity/DB/orders.db"

def simulate():
    db = sqlite3.connect(dbpath)
    cur = db.cursor()
    order_id = 0

    try:
        while True:
            order_id += 1
            value = randint(10, 500)
            cur.execute("INSERT INTO orders (order_id, amount) VALUES (?, ?)", (order_id, value))
            db.commit()
            print(f"Added order {order_id} for ${value}.")
            if randint(1, 20) <= 5: 
                add_review(cur, db, order_id)
            sleep_time = randint(1, 30)
            print(f"Waiting {sleep_time} seconds before the next order...")
            time.sleep(sleep_time)
            if order_id > 1 and randint(1, 20) <= 10: 
                random_order_id = randint(1, order_id)
                add_review(cur, db, random_order_id)

    except KeyboardInterrupt:
        print("Simulation stopped by user.")
    finally:
        db.close()

def add_review(cur, db, order_id):
    reviews = ["beautiful", "love it", "too small", "just like in the pic", "bad quality"]
    comment = reviews[randint(0, len(reviews) - 1)]
    cur.execute("INSERT INTO reviews (order_id, comment) VALUES (?, ?)", (order_id, comment))
    db.commit()
    print(f"Added review to order {order_id}: {comment}")

if __name__ == "__main__":
    simulate()
