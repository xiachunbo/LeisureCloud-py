# coding=utf-8

import os
import atexit
from src.common.Logger import Logger
from src.apscheduler.CoreJob import CoreJob

coreJob = CoreJob()

def foo():
    coreJob.endJob()
    print("exit")
if __name__ == '__main__':
    atexit.register(foo)
    root_path = os.path.dirname(os.path.dirname(__file__))
    logger_conf = Logger(root_path + '/logs/all.log', level='info')
    logger_conf.logger.info('info')
    coreJob.startJob()


