import time
import unittest
from framework.browser_engine import BrowserEngine


class BaiduSearch(unittest.TestCase):

    def setUp(self):
        """
        写【测试固件】时，需要的套件之一，setUp()主要为测试固件开始时的前期准备
        :return:
        """
        browser = BrowserEngine(self)
        self.driver = browser.open_browser(self)

    def tearDown(self):
        """
        写【测试固件】时，需要的套件之一，tearDown()是指测试结束时候的操作，一般是指关闭浏览器啦
        :return:
        """
        self.driver.quit()

    def test_baidu_search(self):
        """
        注意测试固件的用例方法一定要用test开头
        :return:
        """
        self.driver.find_element_by_id('kw').send_keys('selenium')
        time.sleep(2)
        try:
            assert "selenium" in self.driver.title
            print('Found selenium in the title, Test Pass.')
        except Exception as e:
            print("Test Fail", format(e))

    def test_search_2(self):
        pass


if __name__ == '__main__':
    unittest.main()

