import xlrd


#打开Excel表，获取整个表的信息
excel = xlrd.open_workbook("xrldbiao.xlsx")  
#选择对应的表
table = excel.sheet_by_name("Sheet1")   
#选择对应值。（行号，列号）
value = table.cell_value(1,2)
# print(value)
all = table._cell_values
# print(all)

# row0 = table.row_values(0)   #以行为单位,获取某行的值
# print(row0)
# col0 = table.col_values(0)   #以列为单位，获取某列的值
# print(col0)


# # 获取一共有多少行
# r = table.nrows
# # 获取一共有多少列
# c = table.ncols
# print(r,c)

# print("----------------------------------------")
# for i in range(r):
#     print("---------------------------------------")
#     rowlist = table.row_values(i)
#     for j in rowlist:
#         print(j,end=" ")
#     print(" ")



# print("---------------九九乘法表---------------")
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(j,"*",i,"=",j*i,end="\t")
#     print("")

 