# coding:utf-8
import config_manage
import os
import json
import configparser

# 项目相关文件目录常量
PROJECT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))  # 项目路径
TESTDATA_PATH = os.path.join(PROJECT_PATH, "test_data")  # 测试数据目录
TESTCASE_PATH = os.path.join(PROJECT_PATH, "test_case" + os.sep)  # 测试用例目录
LOG_PATH = os.path.join(PROJECT_PATH, "test_report" + os.sep + "logs" + os.sep)  # 日志目录
REPORT_PATH = os.path.join(PROJECT_PATH, "test_report" + os.sep + "report" + os.sep)  # 测试报告目录
CONFIG_PATH = os.path.join(PROJECT_PATH, "configs" + os.sep)  # 配置文件目录
TOKEN_PATH = os.path.join(CONFIG_PATH, "token.json")  # token文件

root_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
conf = configparser.ConfigParser()
YAML_PATH = root_path + '/conf/config.yml'
def get_yaml_config():
    f = open(YAML_PATH, 'r').read()  # 只读模式打开并读取字符串
    dic = config_manage.load(f, Loader=config_manage.FullLoader)  # 将配置参数转为字典格式
    return dic


def write_token(token):
    with open(TOKEN_PATH, 'w') as fp:
        fp.write(json.dumps(token))


def read_token():
    with open(TOKEN_PATH, 'r') as fp:
        dic_data = json.load(fp)
        return dic_data


if __name__ == "__main__":
    get_config = get_yaml_config()
    print(get_config['URL'])
    data = {"token": "test"}
    write_token(token=data)
    print(read_token())
