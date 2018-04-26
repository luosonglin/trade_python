import schedule
import time
# import today_ticks
import datetime


def job():
    # today_ticks.read()
    print("haha!")


# schedule.every(10).minutes.do(job)
# schedule.every().hour.do(job)
# schedule.every().day.at("17:08").do(job)
# schedule.every().monday.do(job)
# schedule.every().wednesday.at("13:15").do(job)
# schedule.every(2).seconds.do(job)

# while True:
#     schedule.run_pending()
#     time.sleep(1)

schedule.every().day.at("18:00").do(job)

if datetime.datetime.now().weekday() < 6:
    while True:
        schedule.run_pending()
        time.sleep(1)

