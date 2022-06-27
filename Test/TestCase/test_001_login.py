from time import sleep

from selenium import webdriver
import pytest
import allure
# 导入本用例用到的页面对象文件
from Test.PageObject import login_page
from Common.parse_csv import parse_csv
from Common.parse_yml import parse_yml
from Test.conftest import browser

host = parse_yml("./Config/dykt.yml", "websites", "host")
# host = parse_yml("D:\Love\Chapter_13\Config\\redmine.yml", "websites", "host")
url = host
data = parse_csv("./Data/test_01_login.csv")
# data = parse_csv("D:\Love\Chapter_13\Data\\test_01_login.csv")
print(data)
# data = [('admin', 'error', '0'), ('admin', 'rootroot', '1')]
@allure.story("机构端登录用例")
@pytest.mark.parametrize(("casename","username", "password", "status", "expect"), data)
class TestLogin():
    def setup(self):
        self.driver = browser()
        # self.driver.maximize_window()
        # self.driver.implicitly_wait(20)
        # 访问登录页
        with allure.step("step1:打开登录页"):
            self.driver.get(url)


    def teardown(self):
        sleep(3)
        self.driver.quit()

    def test_001_login(self, casename, username, password, status, expect):
        allure.dynamic.title(casename)
        # 登录的3个操作用业务场景方法一条语句代替
        login_page.LoginScenario(self.driver).login(username,password)
        if status == '0':
            # 登录失败后的提示信息，通过封装的元素操作来代替
            with allure.step("step2:输入错误用户名密码"):
                text = login_page.LoginOper(self.driver).get_login_failed_info()
                # self.driver.save_screenshot('./Report/report/a.png')
            assert text == expect
            # self.driver.save_screenshot('./Report/report/a.png')
        elif status == '1':
            # 登录后显示的用户名，通过封装的元素操作来代替
            with allure.step("step2:输入正确用户名密码"):
                text = login_page.LoginOper(self.driver).get_login_name()
            assert text == expect
        else:
            print('参数化的状态只能传入0或1')

if __name__ == '__main__':
    # pytest.main(['-s', '-q', '--alluredir', '../report/'])
    pytest.main(['-s', 'test_001_login.py', '--html=./report.html'])
    # pytest.main(['-s', '-q', '--alluredir', '../../Report/report'])
    # os.system('allure generate ./Report/allure-report --clean')