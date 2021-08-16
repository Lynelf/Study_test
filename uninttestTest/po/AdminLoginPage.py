from utils.selenium_tools import find_element

class AdminLoginPage():
    def __init__(self, driver):
        '''
            1.使用构造方法封装页面的所有元素
        '''
        self.title = "ShopXO后台管理系统"
        self.url = 'http://132.232.44.158:9999/shopxo/admin.php?s=/admin/logininfo.html'

        self.driver = driver
        self.username = ("name", "username")
        self.password = ("name", "login_pwd")
        self.loginbtn = ("xpath", "/html/body/div/div/div[2]/div/form/div/div[3]/button")

    def login(self, username, password):
        '''
            2.封装登录的操作步骤
        '''
        find_element(self.driver, self.username).send_keys(username)
        find_element(self.driver, self.password).send_keys(password)
        find_element(self.driver, self.loginbtn).click()