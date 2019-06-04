#!/usr/bin/env python
# coding=UTF-8

import xlwt

'''用途：将txt文件中获取的url、times写入到xls中'''

def write_xls():
    path = "/Users/lucky/Desktop/Auto/iBer_Python_Interface/iBer_Interface/Result/"
    workbook = xlwt.Workbook(encoding="utf-8")
    sheet = workbook.add_sheet("Sheet1")

    row = 0
    with open(path+"API_relult.txt") as  filetxt:
     for line in filetxt:
        line = line.strip()
        fileds = line.split(" ")
        for col, value in enumerate(fileds):
           sheet.write(row, col, value)
        row += 1
    workbook.save(path+"API_relult.xls")