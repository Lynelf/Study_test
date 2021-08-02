import xlrd

def read_excel(excel_path, sheet_name, skip_first=True):
    """
        读取excel，并返回所有行的数据
    """
    results = []
    datas = xlrd.open_workbook(excel_path)      # 打开excel
    table = datas.sheet_by_name(sheet_name)     # 打开具体的页面

    # 是否跳过首行
    start_row = 1
    if skip_first is False:
        start_row = 0

    # 遍历取出所有行的数据
    for row in range(start_row, table.nrows):
        results.append(table.row_values(row))

    return results
