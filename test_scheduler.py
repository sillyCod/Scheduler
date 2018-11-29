# -*- coding: utf-8 -*-

from apscheduler.schedulers.blocking import BlockingScheduler
import datetime

scheduler = BlockingScheduler()


def job(text):
    print(text + datetime.datetime.now().strftime("%H:%M:%S"))


# scheduler.add_job(job, 'interval', seconds=15, args=['Jude', ])
scheduler.add_job(job, 'cron', day_of_week='6', hour=17, minute=20, args=['Jude'])

scheduler.start()
