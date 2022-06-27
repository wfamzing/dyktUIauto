from time import sleep

from selenium import webdriver
import pytest
import allure
# 导入本用例用到的页面对象文件
from Test.PageObject import login_page
from Test.PageObject import orgindex_page
from Common.parse_csv import parse_csv
from Common.parse_yml import parse_yml
from Test.conftest import browser

host = parse_yml("./Config/dykt.yml", "websites", "host")
# host = parse_yml("D:\wf\dyktUIauto\Config\dykt.yml", "websites", "host")
url = host
username = parse_yml("./Config/dykt.yml", "logininfo", "username")
password = parse_yml("./Config/dykt.yml", "logininfo", "password")
# username = parse_yml("D:\wf\dyktUIauto\Config\dykt.yml", "logininfo", "username")
# password = parse_yml("D:\wf\dyktUIauto\Config\dykt.yml", "logininfo", "password")
data = parse_csv("./Data/test_01_orgindex.csv")
# data = parse_csv("D:\wf\dyktUIauto\Data/test_01_orgindex.csv")

print(data)
# data = [('admin', 'error', '0'), ('admin', 'rootroot', '1')]
@allure.story("机构端首页用例")
@pytest.mark.parametrize(("casename", "status", "expect"), data)
class TestOrgindex():
    def setup(self):
        self.driver = browser()
        # self.driver.implicitly_wait(20)
        # 访问登录页
        with allure.step("step1:打开登录页"):
            self.driver.get(url)
        # 登录
        login_page.LoginScenario(self.driver).login(username, password)

    def test_org_index(self, casename, status, expect):
        # 测试用例名称
        allure.dynamic.title(casename)
        if status == '0':
            # 登录失败后的提示信息，通过封装的元素操作来代替
            with allure.step("step2:验证label准确性"):
                text = orgindex_page.IndexOper(self.driver).get_index_label_info()
                # self.driver.save_screenshot('./Report/report/a.png')
            assert text == expect
            # self.driver.save_screenshot('./Report/report/a.png')
        elif status == '1':
            # 登录后显示的用户名，通过封装的元素操作来代替
            with allure.step("step2:验证label准确性"):
                text = orgindex_page.IndexOper(self.driver).get_index_label_info()
                # self.driver.save_screenshot('./Report/report/a.png')
            print(text)
            assert text == expect
        else:
            print('参数化的状态只能传入0或1')

    def teardown(self):
        sleep(3)
        self.driver.quit()

if __name__ == '__main__':
    pytest.main(['-s', 'test_02_new_project.py'])