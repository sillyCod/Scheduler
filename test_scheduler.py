# -*- coding: utf-8 -*-

from apscheduler.schedulers.blocking import BlockingScheduler
import datetime

scheduler = BlockingScheduler()


def job(text):
    print text + datetime.datetime.now()

scheduler.add_job(job, 'interval', seconds=15, args=['Jude', ])

scheduler.start()
