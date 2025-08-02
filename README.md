# product-support-API-watcher
A Python script to monitor multiple APIs and log response status and time.
# 🛡️ API Monitoring Script

A simple Python tool that checks the health of multiple API endpoints by sending requests, measuring response times, and logging the results. Useful for simulating real-world production monitoring.

---

## 🚀 Features

- ✅ Monitors multiple APIs
- 📏 Measures response time
- ⚠️ Detects and logs failures or slow responses
- 📝 Saves all results in a log file (`nprojectlogging.log`)
- 🧰 Easy to extend with alerts, retry logic, or dashboards

---

## 📁 Files in this Repo

api-monitoring-script/
├── nprojectlogging.py # Python script to monitor APIs
├── nprojetlogging.log # Sample output log file
└── README.md # Project documentation (this file)
## ⚙️ Prerequisites

- Python 3.x
- Install the required package:

bash

pip install requests

🧑‍💻 How to Run

Clone this repository or download the files.

Open terminal or command prompt.

Run the script:

bash
Copy
Edit
python nprojetlogging.py
The script will ping each API in the list once.

Output will be saved in the nprojetlogging.log file.

📌 Use Cases

Uptime monitoring for small APIs

API demo projects or testing tools

Log-based monitoring for internal services

Foundation for real-time alerting systems

💡 Ideas for Future Improvement

🔁 Run every X minutes using cron or Task Scheduler

🔔 Add email or Slack alerts on failures

🗃️ Store logs in a database

📊 Visualize response time in Power BI or Excel

⏱ Retry logic for slow or failed APIs
