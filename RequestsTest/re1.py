import requests
from dbtools import query

url = "http://127.0.0.1:8080/morning/getAllGoods"
res = requests.get(url)
assert res.status_code == 200
assert res.json()["success"] == True

# 查询数据库
sql = "select * from tb_goods"
b = query(sql)
assert len(b) != 0

print("获取所有商品接口调用成功！")