
import queue, random, time
from threading import Thread
import sqlite3

# Simulated stream queue
event_queue = queue.Queue()

# Producer simulating IMDb user events
def producer(n=50, delay=0.05):
    movies = ["Oppenheimer", "Dune", "Barbie", "TopGun", "Avengers"]
    for _ in range(n):
        event = {
            "timestamp": time.time(),
            "user_id": f"user_{random.randint(1,10)}",
            "movie": random.choice(movies),
            "event_type": random.choice(["view", "click"])
        }
        event_queue.put(event)
        time.sleep(delay)
    event_queue.put(None)

# In-memory database
conn = sqlite3.connect('events.db', check_same_thread=False)
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS events (
        timestamp TEXT,
        user_id TEXT,
        movie TEXT,
        event_type TEXT
    )
""")
conn.commit()

# Consumer processes and stores events
def consumer():
    while True:
        event = event_queue.get()
        if event is None:
            break
        cursor.execute(
            "INSERT INTO events (timestamp, user_id, movie, event_type) VALUES (?, ?, ?, ?)",
            (str(event["timestamp"]), event["user_id"], event["movie"], event["event_type"])
        )
    conn.commit()

# Run threads
producer_thread = Thread(target=producer)
consumer_thread = Thread(target=consumer)
producer_thread.start()
consumer_thread.start()
producer_thread.join()
consumer_thread.join()

# Print metrics
cursor.execute("SELECT COUNT(DISTINCT user_id) FROM events")
print("Active Users:", cursor.fetchone()[0])

cursor.execute("""
    SELECT movie, COUNT(*) as views 
    FROM events 
    WHERE event_type='view' 
    GROUP BY movie 
    ORDER BY views DESC
""")
print("\nTop Movies:")
for row in cursor.fetchall():
    print(f"{row[0]}: {row[1]} views")
