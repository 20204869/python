# -*- coding: utf-8 -*-
import xlrd  #读取excel文件
import xlwt  #向excel写文件并设置格式
import xlutils  #excel高级操作工具

'''
pip uninstall xlrd
pip install xlrd==1.2.0
xlrd 升级到2.0 只支持.xls文件，降级即可支持.xls和.xlsx
'''

book = xlrd.open_workbook("../data/excel-text.xlsx")
sheet = book.sheet_by_name("Table 9 ")

data = {}
for i in range(14, sheet.nrows):
    # Start at 14th row, because that is where the countries begin
    row = sheet.row_values(i)
    country = row[1]
    data[country] = {
        'child_labor': {
            'total': [row[4], row[5]],
            'male': [row[6], row[7]],
            'female': [row[8], row[9]],
        },
        'child_marriage': {
            'married_by_15': [row[10], row[11]],
            'married_by_18': [row[12], row[13]],
        }
    }
    if country == "Zimbabwe":
        break
import pprint
pprint.pprint(data)