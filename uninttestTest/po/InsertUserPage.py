from utils.selenium_tools import find_element
from selenium import webdriver
import unittest

class InsertUserPage():

    def __init__(self, driver):
        '''
        1.使用构造方法封装页面元素
        '''
        self.title = "ShopXO后台管理系统"
        self.url1 = 'http://132.232.44.158:9999/shopxo/admin.php?s=/admin/logininfo.html'
        self.url2 = 'http://132.232.44.158:9999/shopxo/admin.php?s=/index/index.html'

        self.username = ("name", "username")
        self.password = ("name", "login_pwd")
        self.loginbtn = ("xpath", "/html/body/div/div/div[2]/div/form/div/div[3]/button")

        self.driver = driver
        self.userGl = ("xpath", '//*[@id="admin-offcanvas"]/div/ul/li[5]/a')
        self.userLb = ("xpath", '//*[@id="power-menu-126"]/li[1]/a')
        
        self.Insertbtn = ("xpath", '/html/body/div[1]/div/div/a[1]')
        self.username2 = ("name", "username")
        self.nickname = ("name", "nickname")
        self.phone = ("name", "mobile")
        self.email = ("name", "email")
        self.zfb_openid = ("name", "alipay_openid")
        self.weixin_openid = ("name", "weixin_openid")
        self.baidu_openid = ("name", "baidu_openid")
        self.address = ("name", "address")
        self.integral = ("name", "integral")
        self.pwd = ("name", "pwd")
        self.savebtn = ("xpath", '/html/body/div[1]/div/form/div[14]/button')

        self.results = ("xpath", '//*[@id="data-list-160"]/td[2]/ul/li[1]')
        
        
        
    def login(self, username, password):
        '''
            2.封装登录的操作步骤
        '''
        find_element(self.driver, self.username).send_keys(username)
        find_element(self.driver, self.password).send_keys(password)
        find_element(self.driver, self.loginbtn).click()

    def InsertUser(self, username2, nickname, phone, email, zfb_openid, weixin_openid, baidu_openid, address, integral, pwd):
        '''
        2.封装新增用户步骤
        '''
        find_element(self.driver, self.userGl).click()
        find_element(self.driver, self.userLb).click()
        
        iframe = self.driver.find_element_by_id('ifcontent')
        self.driver.switch_to_frame(iframe)
        find_element(self.driver, self.Insertbtn).click()

        find_element(self.driver, self.username2).send_keys(username2)
        find_element(self.driver, self.nickname).send_keys(nickname)
        find_element(self.driver, self.phone).send_keys(phone)
        find_element(self.driver, self.email).send_keys(email)
        find_element(self.driver, self.zfb_openid).send_keys(zfb_openid)
        find_element(self.driver, self.weixin_openid).send_keys(weixin_openid)
        find_element(self.driver, self.baidu_openid).send_keys(baidu_openid)
        find_element(self.driver, self.address).send_keys(address)
        find_element(self.driver, self.integral).send_keys(integral)
        find_element(self.driver, self.pwd).send_keys(pwd)
        find_element(self.driver, self.savebtn).click()

        # assert find_element(self.driver, self.results) != None   # 可以
        assert find_element(self.driver, self.results)   # 可以

        # try:
        #     find_element(self.driver, self.results)
        # except:
        #     return print("添加用户失败")   ???


        
        
        




        


