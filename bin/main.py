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
    CoreJob.log.logger.info('定时跑批脚本启动!')
    coreJob.startJob()


