import sqlite3
import streamlit as st

conn = sqlite3.connect('events.db')  # Change to persistent DB if needed
cursor = conn.cursor()

st.title("IMDb Engagement Dashboard")

# Active users
cursor.execute("SELECT COUNT(DISTINCT user_id) FROM events")
st.metric("Active Users", cursor.fetchone()[0])

# Top Movies
cursor.execute("""
    SELECT movie, COUNT(*) as views 
    FROM events 
    WHERE event_type='view' 
    GROUP BY movie 
    ORDER BY views DESC
""")
rows = cursor.fetchall()
st.subheader("Top Movies Today")
for movie, count in rows:
    st.write(f"🎬 {movie} — {count} views")
