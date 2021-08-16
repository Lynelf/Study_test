from selenium.webdriver.support.ui import WebDriverWait

def find_element(driver, locator, timeout=10):
    """
        自定义的动态查找元素
    """
    return WebDriverWait(driver, 10).until(lambda s: s.find_element(*locator))