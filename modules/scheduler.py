import schedule
import time

def task():
    print("Scheduled task running...")

def start_scheduler():
    schedule.every().day.at("10:00").do(task)
    while True:
        schedule.run_pending()
        time.sleep(1)
