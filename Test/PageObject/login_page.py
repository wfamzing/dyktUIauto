'''
登录页
'''
# 页面元素对象层
from Base.base import Base

loginname_input = "xpath,//input[@type='text']" #登录名元素
loginpwd_input = "xpath,//input[@type='password']" #登陆密码元素
login_btn = "class,button" #登录按钮
loginerr_alert = "class,el-message__content" #错误弹窗
org_name = "class,name" #机构名称


class LoginPage(object):
    def __init__(self, driver):
        # 私有方法
        self.driver = driver

    def find_username(self):
        # 查找并返回用户名输入框元素
        ele = Base(self.driver).get_element(loginname_input)
        return ele

    def find_password(self):
        # 查找并返回密码输入框元素
        ele = Base(self.driver).get_element(loginpwd_input)
        return ele

    def find_login_btn(self):
        # 查找并返回登录按钮元素
        ele = Base(self.driver).get_element(login_btn)
        return ele

    def find_login_name(self):
        # 查找并返回登录后的用户名元素
        ele = Base(self.driver).get_element(org_name)
        return ele

    def find_login_failed_info(self):
        self.driver.implicitly_wait(20)
        # 查找并返回登录失败后的提示信息元素
        ele = Base(self.driver).get_element(loginerr_alert)
        return ele

# 页面元素操作层
class LoginOper(object):
    def __init__(self, driver):
        # 私有方法，调用元素定位的类
        self.login_page = LoginPage(driver)
        #self.driver = driver

    def input_username(self, username):
        # 对用户名输入框做clear和send_keys操作
        self.login_page.find_username().clear()
        self.login_page.find_username().send_keys(username)

    def input_password(self, password):
        # 对密码输入框做clear和send_keys操作
        self.login_page.find_password().clear()
        self.login_page.find_password().send_keys(password)

    def click_login_btn(self):
        # 对登录按钮做点击操作
        self.login_page.find_login_btn().click()
        # self.driver.implicitly_wait(20)

    def get_login_name(self):
        # 返回登录后的用户名元素的文字
        return self.login_page.find_login_name().text

    def get_login_failed_info(self):
        # 返回登录失败后提示信息的文字
        return self.login_page.find_login_failed_info().text

    # def input_verfication_code(self, fixed_value=123456): # 万能验证码
    #     self.login_page.find_verification_code().send_keys(fixed_value)

# 页面业务场景层
class LoginScenario(object):
    def __init__(self, driver):
        # 私有方法：调用页面元素操作
        self.login_oper = LoginOper(driver)

    def login(self, username, password):
        # 定义一个登录场景，用到了3个操作
        self.login_oper.input_username(username)
        self.login_oper.input_password(password)
        # self.login_oper.input_verfication_code()
        self.login_oper.click_login_btn()