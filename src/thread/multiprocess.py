#!/usr/bin/env python
# -*- coding: utf-8 -*-
from concurrent.futures import ThreadPoolExecutor  # 多线程库

def multiprocess(func, query_list):
    '''
    多线程函数
    :param func: 执行函数
    :param query_list: 参数组成的list
    :return:
    '''
    try:
        length = len(query_list)  # 统计list长度，用来安排线程数
        nums = 4  # 默认4个线程
        if length < nums:
            if length == 0:
                 print('list为空')
                 return
            else:
                n = length
        else:
            n = nums

        # 多线程执行
        with ThreadPoolExecutor(n) as executor:
            result = executor.map(func, query_list)
            '''map_fun：你传入的要执行的map函数
                   itr_arg：一个可迭代的参数，可以是列表字典等可迭代的对象
                   基本上和python的map函数一样
                   注意result并不是你map_fun返回的结果，而是一个生成器，如果要从中去结果，你可以使用列表生成式或者其他你想使用的方法
                '''
            for res in result:
                print(res)  # 这个res就是你map_fun返回的结果，你可以在这里做进一步处理
        print('done')

    except Exception as e:
        print('error:%s' % e)
        return None


def test_func(n):
    return n


if __name__ == "__main__":
    # 构造作为参数的list
    test_list = [i for i in range(20)]
    # 多线程运行，会打印出list中的数值
    multiprocess(test_func, test_list)