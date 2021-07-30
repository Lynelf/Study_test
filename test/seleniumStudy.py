from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="chromedriver")
time.sleep(3)
driver.get("https://www.baidu.com")
driver.find_element_by_id("kw").send_keys("帅哥美女")
time.sleep(3)
driver.find_element_by_id("su").click()
time.sleep(3)
driver.quit()
