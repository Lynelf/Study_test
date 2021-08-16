from selenium import webdriver
from selenium.webdriver.remote.file_detector import LocalFileDetector
from selenium.webdriver.support.ui import WebDriverWait

def find_element(driver, locator, time=10):
    '''
    自定义的动态查找元素
    '''
    return WebDriverWait(driver, 10).until(lambda s: s.find_element(*locator))