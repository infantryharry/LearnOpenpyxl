#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   0x12_练习4_条件判断新增列.py
@Time    :   2021/12/12 00:00:48
@Desc    :   None
'''

# here put the import lib
import openpyxl


wb = openpyxl.load_workbook(r'./课件/测试2.xlsx')
ws = wb['Sheet1']

wb.save(r'./课件/测试2_my.xlsx')
