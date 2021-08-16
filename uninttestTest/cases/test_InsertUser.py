import unittest
from selenium import webdriver
from po.InsertUserPage import InsertUserPage

# class TestCaseInsertUser(unittest.TestCase):

#     def test_01_InsertUser_success(self):
#         driver = webdriver.Chrome(executable_path='drivers/chromedriver.exe')
#         driver.maximize_window()

#         InsertU = InsertUserPage(driver)
#         driver.get(InsertU.url1)
#         InsertU.login("admin","shopxo")
#         driver.get(InsertU.url2)
#         InsertU.InsertUser("小红","红红","1731315469","123@163.com","1731315469","1731315469","1731315469","中国","2","123456")

#         driver.quit()