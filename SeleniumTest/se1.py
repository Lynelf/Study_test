from selenium import webdriver
import time


driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.get("http://localhost:8080/morning/user/userLogin")
driver.maximize_window()

e1 = driver.find_element_by_name("user.loginName")
e1.send_keys("1234@qq.com")

e2 = driver.find_element_by_id("password")
e2.send_keys("a123456")

e3 = driver.find_element_by_xpath('//*[@id="btn_login"]')
e3.click()

# time.sleep(2)
# driver.find_element_by_class_name("mian-nav-a").click()
# time.sleep(2)
# driver.find_element_by_css_selector("#userName").click()
# time.sleep(2)
# driver.find_element_by_link_text("猫宁商城").click()
# time.sleep(2)
# driver.find_element_by_partial_link_text("猫宁").click()


time.sleep(3)
title = "首页 - 猫宁商城"
assert driver.title == title
# print(driver.current_url)
print("登录成功!")
driver.quit()