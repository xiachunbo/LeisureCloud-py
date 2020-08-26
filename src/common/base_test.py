from main.base.RunMethod import RunMethod
from main.base.GetData import GetData


def base_test():
    """
    基础测试框
    """
    BASE_URL = ''
    data_case = GetData('file_path', 'sheet_name')  # 测试用例对象
    case_count = data_case.get_case_lines  # 用例数

    for i in range(1, int(case_count)):
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

        # 执行主用例
        res = RunMethod().run_main(method=method, url=url, data=request_data, header=header)

        # 断言（放后面讲）
        #base_assert(i, url, header, request_data, expect, res, data_case