# 导入unittest
import time
from typing import Mapping
import unittest
from unittest.main import main
from selenium import webdriver

# 所有的测试用例类，都是需要继承unittest.TestCase
class TestCaseSearch(unittest.TestCase):
    
    # 成员方法管理测试用例：test_开头命名
    def test_01_search_success(self):
        '''
            搜索商品的测试用例
        '''
        driver = webdriver.Chrome(executable_path='drivers/chromedriver.exe')
        driver.maximize_window()
        driver.get('http://132.232.44.158:9999/shopxo/')
        driver.find_element_by_id('search-input').send_keys("华为")
        driver.find_element_by_id('ai-topsearch').click()
        time.sleep(3)

        title = "华为 - ShopXO企业级B2C电商系统提供商 - 演示站点"
        # assert driver.title == title
        self.assertEqual(driver.title, title)

        driver.quit()

# 这是调试脚本的方法
# 会调用所有test_开头的方法
if __name__ == "__main__":
    # print(__name__)
    unittest.main()

