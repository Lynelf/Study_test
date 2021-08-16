from selenium import webdriver
from selenium_tool import find_element

driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.get("http://localhost:8080/morning//user/userLogin")
driver.maximize_window()

# 定位元素的方式
loginname = ("name","user.loginName")
password = ("id","password")
loginbtn = ("xpath",'//*[@id="btn_login"]')
title = "首页 - 猫宁商城"

# 登录操作
find_element(driver,locator=loginname).send_keys("1234@qq.com")
find_element(driver,password).send_keys("a123456")
find_element(driver,loginbtn).click()

assert driver.title == title
print("输入正确用户名和密码登录成功！")
driver.quit()

# driver.switch_to_frame("frame元素的定位")
# driver.switch_to_window(driver.window_handles[-1])
# driver.switch_to_alert().accept()
# driver.switch_to_alert().dismiss()