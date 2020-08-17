#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from main.base.RunMethod import RunMethod
from main.base.base_config import BASE_URL, DB_MD
import logging
from main.base.config_manage import config_manage


class BaseCase(unittest.TestCase):
    """
    setUpClass：每次运行脚本，优先执行，只执行一次
    tearDownClass：脚本运行完成后执行，只执行一次
    """


@classmethod
def tearDownClass(cls):
    pass

    """
    setUp：每执行一条用例前，优先执行一次
    tearDown：每执行完一条用例后，执行一次
    """


def setUp(self):
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    self.log = logging.getLogger(__name__)
    #self.log = Logger(custom_color=True, name='base_case')
    self.log.info("--------------------【{}测试用例开始】--------------------".format(
        self.__class__.__name__ + '.' + self._testMethodName))


def tearDown(self):
    self.log.info("--------------------【{}测试用例结束】--------------------\n".format(
        self.__class__.__name__ + '.' + self._testMethodName))
    self.log.del_handler()  # 防止重复写入日志


def base_test(self, i, data_case):
    """
    核心逻辑框，所有用例都执行这里的逻辑（登录接口另外单独一个函数）
    :param i: 用例行
    :param data_case: 测试用例
    :return:
    """
    is_run = data_case.get_is_run(i)  # 是否运行
    if is_run:

        url = BASE_URL + data_case.get_request_url(i)  # 用例url
        method = data_case.get_request_method(i)  # 请求方法
        request_data = data_case.get_request_data(i)  # 请求数据
        expect = data_case.get_expect_data(i)  # 预期结果
        header = data_case.is_header(i)  # 请求头
        depend = data_case.is_depend(i)  # 依赖
        depend_data = data_case.get_depend_data(i)  # 依赖请求数据
        depend_key = data_case.get_depend_key(i)  # 依赖关键字参数
        sql_data = data_case.get_sql(i)  # 获取sql列表

        header["Authorization"] = config_manage.read_token()["Data"]["Token"]  # 更新token到请求头中

        # 执行查询数据库逻辑
        if sql_data is not None:
            for data in sql_data:
                sql = data["sql"]  # 获取sql
                result = DB_MD.ExecQuery(sql)

                if result:
                    result = str(result[0][0])
                else:
                    raise ValueError("查询结果为空，请检查sql或数据")

                # 根据key赋值到请求数据/依赖请求数据/预期结果
                for key in data.keys():
                    if key.lower() == "request":
                        for_request = data[key]
                        request_data = self.get_sql_value_to_request_data(request_data=request_data, key=for_request,
                                                                          result=result)
                    elif key.lower() == "expect":
                        for_expect = data[key]
                        expect[for_expect] = result
                    elif key.lower() == "depend":
                        for_depend = data[key]
                        depend_data = self.get_sql_value_to_request_data(request_data=depend_data, key=for_depend,
                                                                         result=result)
                    elif key.lower() == "sql":
                        pass
                    else:
                        raise ValueError(self.log.info("键应为 1.request 2.expect 3.depend，请检查键是否正确"))

        # 执行依赖接口逻辑
        if depend is not None:
            depend = eval(depend)  # 转字典
            depend_url = BASE_URL + depend["url"]  # 依赖接口
            depend_method = depend["method"]  # 请求方式
            depend_content = depend.get("content")  # 接口描述

            res = RunMethod().run_main(method=depend_method, url=depend_url, data=depend_data,
                                       header=header)
            data_case.write_result_depend(i, res.text)
            self.log.info("**********执行依赖：{}**********".format(depend_content))
            self.log.info("请求接口: " + depend_url)
            self.log.info("请求头:" + str(header))
            self.log.info("请求数据:" + str(depend_data))
            self.log.info("返回响应: " + res.text)
            #check_response_status(res, isprint=False)  # 检查执行是否成功

            # 更新依赖值到请求数据中
            if depend_key is not None:
                for key, value in depend_key.items():
                    res_value = self.get_keyValue(res=res.json(), key=key)
                    request_data[value] = res_value

        self.log.info("**********执行主用例**********")
        res = RunMethod().run_main(method=method, url=url, data=request_data, header=header)

        self.base_assert(i, url, header, request_data, expect, res, data_case)  # 断言


def base_login(self, i, data_case):
    """
    登录接口用，在登陆成功后，写入token到文件中
    :param i: 用例行
    :param data_case: 测试用例对象
    :return:
    """

    is_run = data_case.get_is_run(i)
    if is_run:
        url = BASE_URL + data_case.get_request_url(i)  # 用例url
        method = data_case.get_request_method(i)  # 请求方法
        request_data = data_case.get_request_data(i)  # 请求数据
        expect = data_case.get_expect_data(i)  # 预期结果
        header = data_case.is_header(i)  # 请求头
        depend = data_case.is_depend(i)  # 依赖url相关数据
        depend_data = data_case.get_depend_data(i)  # 依赖请求数据
        depend_key = data_case.get_depend_key(i)  # 依赖关键字参数
        # sql_data = data_case.get_sql(i)  # 获取sql列表

        """若需要执行数据库逻辑，或依赖接口逻辑，看base_test"""

    self.log.info("执行主用例".center(20, "*"))
    res = RunMethod().run_main(method=method, url=url, data=request_data, header=header)

    is_success = self.base_assert(i, url, header, request_data, expect, res, data_case)
    # 写入token到token.json文件
    if is_success is True:
        config_manage.write_token(res.json())


def base_assert(self, i, url, header, request_data, expect, res, data_case):
    """
    通用断言，根据预期结果键值对>断言>实际结果，相等则成功，反之失败
    :param i: 用例行
    :param url: 用例接口
    :param header: 请求头
    :param request_data: 请求数据
    :param expect: 预期结果
    :param res: 实际结果
    :param data_case: 用例
    :return: 是否成功标识
    """
    expect_keys = list(expect.keys())
    len_keys = len(expect_keys)

    global isSuccess

    for index, key in enumerate(expect_keys):
        # 最后键标识位
        if len_keys == index + 1:
            is_last = True
        else:
            is_last = False

        # 根据预期结果的键查询响应结果对应键，并断言
        if key in res.json().keys():
            e = type(res.json()[key])(expect[key])  # 转换expect值的type为result值的type
            try:
                self.assertEqual(e, res.json()[key])
            except AssertionError as msg:
                self.log.info("请求接口: " + url)
                self.log.info("请求头: " + str(header))
                self.log.info("请求数据: " + str(request_data))
                self.log.info("实际结果: " + res.text)
                self.log.info("预期结果: " + str(expect))
                data_case.write_result(i, res.text)
                data_case.write_is_success(i, "Fail")
                isSuccess = False
                self.log.error("断言失败")
                raise AssertionError(msg)
            else:
                if is_last is True:
                    self.log.info("请求接口: " + url)
                    self.log.info("请求头: " + str(header))
                    self.log.info("请求数据: " + str(request_data))
                    self.log.info("预期结果：" + str(expect))
                    self.log.info("实际结果：" + res.text)
                    self.log.info("断言成功")
                    data_case.write_result(i, res.text)
                    data_case.write_is_success(i, "Success")
                    isSuccess = True
        else:
            for k, v in res.json().items():
                v_type = type(v)
                while v_type != dict:
                    if v_type is list:
                        v_list = v
                        for vv in v_list:
                            if type(vv) is dict:
                                v = vv
                                v_type = dict
                    else:
                        break
                else:
                    if key in v.keys():
                        e = type(v[key])(expect[key])  # 转换expect值的type为result值的type
                        try:
                            self.assertEqual(e, v[key])
                        except AssertionError as msg:
                            self.log.info("请求接口: " + url)
                            self.log.info("请求头: " + str(header))
                            self.log.info("请求数据: " + str(request_data))
                            self.log.info("实际结果: " + res.text)
                            self.log.info("预期结果: " + str(expect))
                            data_case.write_result(i, res.text)
                            data_case.write_is_success(i, "Fail")
                            isSuccess = False
                            self.log.error("断言失败")
                            raise AssertionError(msg)
                        else:
                            if is_last is True:
                                self.log.info("请求接口: " + url)
                                self.log.info("请求头: " + str(header))
                                self.log.info("请求数据: " + str(request_data))
                                self.log.info("预期结果：" + str(expect))
                                self.log.info("实际结果：" + res.text)
                                self.log.info("断言成功")
                                data_case.write_result(i, res.text)
                                data_case.write_is_success(i, "Success")
                                isSuccess = True
    return isSuccess

def test1(self):
    self.log.info('unittest')

if __name__ == '__main__':
    unittest.main()
