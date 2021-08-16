import pytest
import requests
from requests.api import post

# test开头的方法
def test_daying01_success():
    print("hello word")

def test_huoqu02_success():
    url = "http://127.0.0.1:8080/morning/getAllGoods"
    res =  requests.get(url=url)
    # print(res.text)

    assert res.status_code == 200
    assert str(res.json()["success"]) == "True"

   
def test_denglu03_shibai():
    url = "http://132.232.44.158:5000/userLogin/"  
    datas = {"username":"test", "password":"test", "captcha":"123456"}
    res = requests.request("post",url=url,json=datas)

    assert res.status_code == 200
    assert res.json()["code"] == 200



