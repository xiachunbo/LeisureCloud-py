#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import urllib3
import json

class RunMethod:
    def __init__(self):
        self.session = requests.session()
        urllib3.disable_warnings()

    def run_main(self, method, url, data=None, header=None, params=None):
        """
        归类请求方法
        :param method:  请求方法
        :param url: 接口
        :param data: 请求参数
        :param header: 请求头
        :return: response（请求结果）
        """
        if method.lower() == 'Post'.lower():  # 向指定资源提交数据进行处理请求（例如提交表单或者上传文件）。数据被包含在请求体中。POST 请求可能会导致新的资源的建立和/或已有资源的修改。
            res = self.session.post(url=url, json=data, headers=header, verify=False)

        elif method.lower() == 'Get'.lower():  # 请求指定的页面信息，并返回实体主体。
            res = self.session.get(url=url, json=data, headers=header, params=params, verify=False)

        elif method.lower() == 'HEAD'.lower():  # 类似于 GET 请求，只不过返回的响应中没有具体的内容，用于获取报头
            res = self.session.head(url=url, json=data, headers=header, verify=False)

        elif method.lower() == 'PUT'.lower():  # 从客户端向服务器传送的数据取代指定的文档的内容。
            res = self.session.put(url=url, json=data, headers=header, verify=False)

        elif method.lower() == 'DELETE'.lower():  # 请求服务器删除指定的页面。
            res = self.session.delete(url=url, json=data, headers=header, verify=False)

        elif method.lower() == 'OPTIONS'.lower():  # 允许客户端查看服务器的性能。
            res = self.session.options(url=url, json=data, headers=header, verify=False)

        elif method.lower() == 'PATCH'.lower():  # 是对 PUT 方法的补充，用来对已知资源进行局部更新
            res = self.session.patch(url=url, json=data, headers=header, verify=False)
        else:
            res = self.session.get(url=url, json=data, headers=header, verify=False)
        return res


if __name__ == '__main__':
    url = ' http://localhost:1855/processDefinition/processDefinitionByType'
    data = {
        'parem': 'xxx'
    }
    header = {
        "Content-Type": "text/html; charset=utf-8",
        "Accept-Charset": "utf-8"
    }
    run = RunMethod()
    run_test = run.run_main(method="Get", url=url, data=data, header=header)
    lottery_message = json.dumps(run_test.json(), ensure_ascii=False)
    print(lottery_message)