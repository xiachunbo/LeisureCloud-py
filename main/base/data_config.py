# coding:utf-8

# 根据索引，分别对应excel中的元素，若元素有改动，在这里维护即可
class data_config(object):
    Id = 0
    title = 1
    run = 2
    url = 3
    request_method = 4
    header = 5
    depend_url = 6
    depend_data = 7
    depend_result = 8
    depend_key = 9
    data = 10
    sql = 11
    expect = 12
    result = 13
    is_success = 14


def get_id():
    """获取case_id"""
    return data_config.Id


def get_title():
    """获取用例标题"""
    return data_config.title


def get_url():
    """获取请求url"""
    return data_config.url


def get_run():
    """获取是否运行"""
    return data_config.run


def get_request_method():
    """获取请求方式"""
    return data_config.request_method


def get_header():
    """获取header"""
    return data_config.header


def get_depend_case():
    """case依赖"""
    return data_config.depend_url


def get_depend_data():
    """依赖请求数据"""
    return data_config.depend_data


def get_depend_result():
    """依赖请求结果"""
    return data_config.depend_result


def get_depend_result_key():
    """依赖请求结果参数"""
    return data_config.depend_key


def get_request_data():
    """请求数据"""
    return data_config.data


def get_sql():
    """sql数据"""
    return data_config.sql


def get_expect():
    """预期结果"""
    return data_config.expect


def get_result():
    """实际结果"""
    return data_config.result


def get_is_success():
    """成功/失败结果"""
    return data_config.is_success