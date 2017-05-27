# -*- coding: utf-8 -*-

from apscheduler.schedulers.blocking import BlockingScheduler
import datetime
import pymongo
import abc


class Task(object):

    __metaclass__ = abc.ABCMeta

    def __init__(self, date):
        self.date = date

    @abc.abstractmethod
    def execute_task(self):
        pass

    def start_task(self):
        self.execute_task()

if __name__ == '__main__':
    class A(Task):
        def execute_task(self):
            print 'I\'m A, inherit Task.'

    A(2015).start_task()
