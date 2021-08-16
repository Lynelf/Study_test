from os import name
import requests
from exceltools import read_excel

path = "lux的接口测试用例+1203.xlsx"
sheet_name = "登录模块"

res = read_excel(excel_path=path,sheet_name=sheet_name)
for case in res:
    id = case[0]
    name = case[1]
    url = case[3]
    data = eval(case[4])  #字符串转字典eval
    status_code = int(case[5])
    response_code = int(case[6])

    try:
        # 造请求
        res = requests.request("post", url=url, json=data)
        # 判断http状态响应码
        assert res.status_code == status_code
        # 判断响应返回值的信息
        assert res.json()["code"] == response_code
        print("第{}条测试用例{}执行成功".format(id,name))
    except:
        print("第{}条测试用例{}执行失败".format(id,name))