import schedule
import time

def job():
    print("Running scheduled task!")

# Schedule the task to run every day at 10:00 AM
schedule.every().day.at("10:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
