from os import execl
import xlrd
from xlrd import sheet

def readexcel(ExcelName,SheetName):
    '''
    这是一个用来读取Excel表格的方法
    '''
    excel = xlrd.open_workbook(ExcelName)
    table = excel.sheet_by_name(SheetName)
    r = table.nrows
    tablelist = []
    for i in range(r):
        rowlist = table.row_values(i)
        tablelist.append(rowlist)
    return(tablelist)

# datas = readexcel("xrldbiao.xlsx","Sheet1")
# print(datas)

def add(int1,int2):
    sum = int1 + int2
    return sum

