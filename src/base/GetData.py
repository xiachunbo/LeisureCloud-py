import json
from main.base.data_config import data_config
from main.base.OperationExcel import OperationExcel


class GetData(object):
    """获取excel数据"""

    def __init__(self, file_path, sheet_name):
        self.opera_excel = OperationExcel(file_path, sheet_name)

    def get_case_lines(self):
        """获取excel行数，即case的个数"""
        return self.opera_excel.get_max_rows()

    def get_is_run(self, row):
        """获取是否执行"""
        col = int(data_config.get_run())
        run_model = self.opera_excel.get_cell_value(row, col)
        if run_model == 'yes':
            flag = True
        else:
            flag = False
        return flag

    def is_header(self, row):
        """
        获取header
        :param row: 行号
        :return:
        """
        col = int(data_config.get_header())
        header = self.opera_excel.get_cell_value(row, col)
        if header != '':
            return json.loads(header)
        else:
            return None

    def get_request_method(self, row):
        """
        获取请求方式
        :param row: 行号
        :return:
        """
        # col 列
        col = int(data_config.get_request_method())
        request_method = self.opera_excel.get_cell_value(row, col)
        return request_method

    def get_request_url(self, row):
        """
        获取url
        :param row: 行号
        :return:
        """
        col = int(data_config.get_url())
        url = self.opera_excel.get_cell_value(row, col)
        return url

    def get_request_data(self, row):
        """
        获取请求数据
        :param row:行号
        :return:
        """
        col = int(data_config.get_request_data())
        data = self.opera_excel.get_cell_value(row, col)
        if data == '':
            return None
        # return json.loads(data)
        return eval(data)

    def get_expect_data(self, row):
        """
        获取预期结果
        :param row:
        :return:
        """
        col = int(data_config.get_expect())
        expect = self.opera_excel.get_cell_value(row, col)
        if expect == "":
            return None
        else:
            return eval(expect)

    def write_result(self, row, value):
        """
        写入结果数据
        :param value: 结果
        :param row: 行号
        :return:
        """
        col = int(data_config.get_result())
        self.opera_excel.write_value(row, col, value)

    def write_result_depend(self, row, value):
        """
        写入依赖结果数据
        :param value: 结果
        :param row: 行号
        :return:
        """
        col = int(data_config.get_depend_result())
        self.opera_excel.write_value(row, col, value)

    def write_is_success(self, row, value):
        """
        写入结果数据
        :param value: 结果
        :param row: 行号
        :param col: 列号
        :return:
        """
        col = int(data_config.get_is_success())
        self.opera_excel.write_value(row, col, value)

    def get_depend_data(self, row):
        """
        获取依赖数据的key
        :param row:行号
        :return:
        """
        col = int(data_config.get_depend_data())
        depend_data = self.opera_excel.get_cell_value(row, col)
        if depend_data == "":
            return None
        else:
            return json.loads(depend_data)

    def get_depend_key(self, row):
        """
        获取依赖请求结果的某个参数值
        :param row: 行号
        :return:
        """
        col = int(data_config.get_depend_result_key())
        depend_key = self.opera_excel.get_cell_value(row, col)
        if depend_key == "":
            return None
        else:
            return eval(depend_key)

    def is_depend(self, row):
        """
        判断是否有case依赖
        :param row:行号
        :return:
        """
        col = int(data_config.get_depend_case())  # 获取是否存在数据依赖列
        depend_url = self.opera_excel.get_cell_value(row, col)
        if depend_url == "":
            return None
        else:
            return depend_url

    def get_title(self, row):
        """
        获取用例标题
        :param row: 行号
        :return:
        """
        col = int(data_config.get_title())
        title = self.opera_excel.get_cell_value(row, col)
        if title == "":
            return None
        else:
            return title

    def get_sql(self, row):
        """
        获取sql
        :param row: 行号
        :return:
        """
        col = int(data_config.get_sql())
        sql = self.opera_excel.get_cell_value(row, col)
        if sql == "":
            return None
        else:
            # return json.loads(sql)
            return eval(sql)