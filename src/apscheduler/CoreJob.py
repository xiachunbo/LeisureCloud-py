#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
from src.common.Logger import Logger
from src.db.Database import Database
from pytz import utc
from apscheduler.jobstores.memory import MemoryJobStore
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
from apscheduler.events import EVENT_JOB_MAX_INSTANCES, EVENT_JOB_ERROR, EVENT_JOB_MISSED, EVENT_JOB_EXECUTED
class CoreJob:
    root_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    log = Logger(root_path + '/logs/all.log', level='info')

    def __init__(self):
        jobstores = {
            'default': MemoryJobStore()
        }
        executors = {
            'default': ThreadPoolExecutor(200),
            'processpool': ProcessPoolExecutor(10)
        }
        job_defaults = {
            'coalesce': True,
            'max_instances': 1,
            'misfire_grace_time': 60
        }
        self.exception = None
        self.scheduler = BlockingScheduler(jobstores=jobstores, executors=executors, job_defaults=job_defaults, timezone=utc)
        self.scheduler.add_listener(self.my_listener, EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)
    def my_job1(self):
        self.log.logger.info('my_job1 is running, Now is %s' % datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    def my_listener(self, event):
         if event.exception:
             print '任务出错了！！！！！！'
         #else:
         #    print '任务照常运行...'

    def startJob(self):
        # 每隔5秒运行一次my_job1
        self.scheduler.add_job(self.my_job1, 'interval', seconds=1,id='my_job1')
        self.scheduler.start()

    def endJob(self):
        self.scheduler.shutdown()


    def db_oper(self):
         root_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
         path = root_path + "/conf/sql_conf_test.conf"
        # 测试 select
         dba = Database(database_config_path=path)
         ret = dba.test_pool_select("SELECT * FROM act_re_model")
         print(ret)
         print('11111')