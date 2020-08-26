# coding=utf-8

import os
from src.db.Database import Database

if __name__ == '__main__':
    root_path = os.path.dirname(os.path.dirname(__file__))
    path = root_path + "/conf/sql_conf_test.conf"
    # 测试 select
    dba = Database(database_config_path=path)
    ret = dba.test_pool_select("SELECT * FROM act_re_model")
    print(ret)
    print('11111')
