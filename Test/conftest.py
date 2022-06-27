import pytest
from selenium import webdriver
import os
import allure


# driver = None
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
        '''
        hook pytest失败
        :param item:
        :param call:
        :return:
        '''
        # execute all other hooks to obtain the report object
        outcome = yield
        rep = outcome.get_result()
        # we only look at actual failing test calls, not setup/teardown
        if rep.when == "call" and rep.failed:
                mode = "a" if os.path.exists("./Report/report/failures") else "w"
                with open("./Report/report/failures", mode) as f:
                        # let's also access a fixture for the fun of it
                        if "tmpdir" in item.fixturenames:
                                extra = " (%s)" % item.funcargs["tmpdir"]
                        else:
                                extra = ""
                        f.write(rep.nodeid + extra + "\n")
                # pic_info = adb_screen_shot()
                with allure.step('添加失败截图...'):
                        allure.attach(driver.get_screenshot_as_png(), "失败截图", allure.attachment_type.PNG)
# @pytest.fixture(scope='session')
def browser():
        global driver
        # if driver is None:
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(20)
        return driver
