
# Real-Time Analytics Pipeline – IMDb User Engagement Metrics

This project simulates a real-time data pipeline for processing and analyzing user engagement events (views, clicks) like those on IMDb. It demonstrates a foundational system design for data engineering pipelines and includes a simulated stream, real-time consumer processing, SQL storage, and dashboard visualization.

---

##  Technologies Used

- **Python** – simulation, streaming, data processing
- **queue.Queue** – simulates streaming pipeline (like Amazon Kinesis)
- **SQLite** – stores processed events in-memory
- **Streamlit** – optional dashboard visualization
- **Google Colab / Jupyter** – development platform

---

## Architecture

```text
+------------------+       +--------------+       +----------------+
|  Producer (Sim)  |  -->  |   Queue ()   |  -->  |  Consumer Code |
+------------------+       +--------------+       +--------+-------+
                                                        |
                                                  Stores into DB
                                                        ↓
                                             +-----------------------+
                                             | SQLite (in-memory DB) |
                                             +-----------+-----------+
                                                         ↓
                                           +--------------------------+
                                           | Streamlit Metrics Dashboard |
                                           +--------------------------+
```

---

## How to Run

1. Clone the repo:
```bash
git clone https://github.com/yourusername/imdb-realtime-pipeline.git
cd imdb-realtime-pipeline
```

2. Install dependencies:
```bash
pip install streamlit
```

3. Run Python simulation:
```bash
python main.py
```

4. (Optional) Start dashboard:
```bash
streamlit run dashboard.py
```

---

## Metrics Tracked

- Active Users (unique user IDs)
- Most Viewed Movies Today
- Clicks and Views by Type
- Hourly Trends (future enhancement)

---

## Future Enhancements

- Integrate with **Amazon Kinesis** for real AWS streaming
- Use **Amazon DynamoDB** for scalable storage
- Add **WebSocket-based live dashboard updates**
- Replace simulation with real IMDb dataset (if available)
- Connect to **Amazon QuickSight** for production BI

---

## Author

Gugan Loganathan
