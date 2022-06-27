'''
机构首页
'''
# 页面元素对象层
import json
from Base.base import Base

index_label = "class,label" #首页label

# 页面对象层
class IndexPage(object):
    def __init__(self, driver):
        self.driver = driver

    def find_index_label(self):
        # ele = self.driver.find_element_by_id('project_name')
        ele = Base(self.driver).get_elements(index_label).text
        return ele


# 对象操作层
class IndexOper(object):
    def __init__(self, driver):
        self.index_label_page = IndexPage(driver)

    def get_index_label_info(self):
        eles = ''.join(self.index_label_page.find_index_label())
        return eles


# 业务逻辑层
class IndexScenario(object):
    def __init__(self, driver):
        self.Index_oper = IndexOper(driver)

    def index_label(self):
        self.Index_oper.get_index_label_info()