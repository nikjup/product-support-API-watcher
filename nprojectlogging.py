import requests
import logging
from datetime import datetime

# Set up logging
logging.basicConfig(
    filename='nprojectlogging.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# List of APIs to monitor
endpoints = [
    "https://api.open-meteo.com/v1/forecast?latitude=35&longitude=139&current_weather=true",
    "https://api.github.com",
    "https://fake-api.example.com"  # To simulate failure
]

# Function to ping API and log result
def monitor_api():
    for url in endpoints:
        try:
            start_time = datetime.now()
            response = requests.get(url, timeout=5)
            response_time = (datetime.now() - start_time).total_seconds()
            
            if response.status_code == 200:
                logging.info(f"{url} | Status: {response.status_code} | Response Time: {response_time:.2f}s")
                print(f"[INFO] {url} - 200 OK - {response_time:.2f}s")
            else:
                logging.warning(f"{url} | Non-200 Status: {response.status_code} | Time: {response_time:.2f}s")
                print(f"[WARNING] {url} - Status: {response.status_code} - {response_time:.2f}s")

        except requests.exceptions.RequestException as e:
            logging.error(f"{url} | ERROR: {str(e)}")
            print(f"[ERROR] {url} - {str(e)}")

# Running the script once
if __name__ == "__main__":
    monitor_api()
