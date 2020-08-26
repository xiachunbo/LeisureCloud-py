# coding=utf-8
import os
import configparser
# 项目路径
root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
conf = configparser.ConfigParser()
conf.read(root_path + '/conf/config.ini') # 文件路径

#读取配置文件里所有的Section
print(conf.sections())

#打印出test1这个section下包含key
print(conf.options("config_data"))

