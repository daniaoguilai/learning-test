# -*- coding:utf-8 -*-

import xlrd
import xlwt
from xlutils.copy import copy
import os

filepath1 = "D:\\OS.20190722.xlsx"
filepath2 = "D:\\bak.20190722.xlsx"

t = {}
x1 = xlrd.open_workbook(filepath1)
x2 = xlrd.open_workbook(filepath2)
index1 = x1.sheet_names()[0]

s1 = x1.sheet_by_name(index1)
s2 = x2.sheet_by_index(0)

nrows1 = s1.nrows
nrows2 = s2.nrows

x3 = copy(x2)

s3 = x3.get_sheet(0)


for row in range(1,nrows1):
    t[s1.cell_value(row,9)]=s1.cell_value(row,22)
for row in range(1,nrows2):
    s3.write(row,22,t[s2.cell_value(row,9)])
x3.save('test.xls')


