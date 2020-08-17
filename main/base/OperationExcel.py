#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xlrd
import xlwt
from xlutils.copy import copy
import json

class OperationExcel:
    """操作excel"""

    def __init__(self, file_path=None, sheet_name=None):
        self.file_path = file_path
        self.sheet_name = sheet_name
        self.data = self.get_data()

    def get_data(self):
        """
        获取sheets的内容
        :return:
        """
        data = xlrd.open_workbook(self.file_path)
        table = data.sheet_by_name(self.sheet_name)
        return table

    def get_max_rows(self):
        """
        获取单元格行数
        :return:
        """
        return self.data.nrows

    def get_max_cols(self):
        """
        获取单元格列数
        :return:
        """
        return self.data.ncols

    def get_cell_value(self, row, col):
        """
        获取单元格数据
        :param row: 行
        :param col: 列
        :return:
        """
        return self.data.cell_value(row, col)

    def get_cell_type(self, row, col):
        """
        获取单元格数据的类型
        :param row: 行
        :param col: 列
        :return:
        """
        # 0：空内容  1：字符集  2：数字  3：日期  4：布尔  5：错误
        return self.data.cell_type(row, col)

    def get_row_value(self, row):
        """
        获取某一行的内容
        :param row:行号
        :return:
        """
        return self.data.row_values(row)

    def get_col_data(self, col):
        """
        获取某一列的内容
        :param col:列号
        :return:
        """
        return self.data.col_values(col)

    def write_value(self, row, col, value):
        """
        回写数据到excel
        :param row:行
        :param col:列
        :param value:值
        :return:
        """
        read_data = xlrd.open_workbook(self.file_path, formatting_info=True)
        new_data = copy(read_data)  # 将xlrd的对象转化为xlwt的对象
        table = new_data.get_sheet(self.sheet_name)
        table.write(row, col, value, self.set_style())
        new_data.save(self.file_path)

    @staticmethod
    def set_style(name='宋体', height=220, bold=False):
        style = xlwt.XFStyle()  # 初始化样式

        font = xlwt.Font()  # 为样式创建字体
        font.name = name  # 定义具体的字体
        font.bold = bold  # 定义是否加粗
        font.color = 'black'  # 黑色
        # font.color_index = 4  # 定义字体颜色
        font.height = height  # 定义字体大小  220就是11号字体，大概就是11*20得来的吧
        style.font = font  # 最终把自定义的字体，定义到风格里面

        alignment = xlwt.Alignment()  # 设置字体在单元格的位置
        alignment.horz = xlwt.Alignment.HORZ_CENTER  # 水平方向 居中：HORZ_CENTER  左对齐：HORZ_LEFT  右对齐：HORZ_RIGHT
        alignment.vert = xlwt.Alignment.VERT_CENTER  # 垂直方向 居中：VERT_CENTER  顶部对齐：VERT_TOP  底部对齐：VERT_BOTTOM
        style.alignment = alignment

        border = xlwt.Borders()  # 给单元格加框线
        border.left = xlwt.Borders.THIN  # 左
        border.top = xlwt.Borders.THIN  # 上
        border.right = xlwt.Borders.THIN  # 右
        border.bottom = xlwt.Borders.THIN  # 下
        border.left_colour = 0x40  # 设置框线颜色，0x40是黑色
        border.right_colour = 0x40
        border.top_colour = 0x40
        border.bottom_colour = 0x40
        style.borders = border

        return style

if __name__ == '__main__':
    opera = OperationExcel(file_path=u'/Users/xiaobobo/Desktop/设计表.xlsx', sheet_name=u'表名')
    opera.get_data()
    opera.get_cell_value(1, 2)
    print opera.get_row_value(1)
    print(json.dumps(opera.get_row_value(1)).decode("unicode-escape"))
    #opera.write_value(3, 1, 'ceshi样式')