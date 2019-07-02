import time
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.baidu_homepage import HomePage


class BaiduSearch(unittest.TestCase):
    """百度搜索测试"""
    @classmethod
    def setUpClass(cls):
        """
        写【测试固件】时，需要的套件之一，setUp()主要为测试固件开始时的前期准备
        :return:
        """
        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser(cls)

    @classmethod
    def tearDownClass(cls):
        """
        写【测试固件】时，需要的套件之一，tearDown()是指测试结束时候的操作，一般是指关闭浏览器啦
        :return:
        """
        cls.driver.quit()

    def test_baidu_search(self):
        """关键字搜索及标题验证"""
        """
        注意测试固件的用例方法一定要用test开头
        :return:
        """
        # self.driver.find_element_by_id('kw').send_keys('selenium')
        # time.sleep(2)
        # try:
        #     assert "selenium" in self.driver.title
        #     print('Found selenium in the title, Test Pass.')
        # except Exception as e:
        #     print("Test Fail", format(e))
        homepage = HomePage(self.driver)
        """
        为什么这里要 self.driver?
        到一个新的页面，第一件事情就是初始化这个页面的‘一个页面对象实例’。
        这个self.driver可以这么理解：它是从browser_engine实例出来的，在初始化一个页面对象的时候，也把这个来自browser_engine的
        driver赋值给了这个页面对象，这样才能执行调用页面对象或者基类里面的相关driver方法。
        最重要的是，要保持driver一致。
        """
        homepage.type_search('selenium')
        homepage.send_submit_btn()
        time.sleep(2)
        homepage.take_window_img()
        # try:
        #     assert 'selenium266' in homepage.get_title()
        #     print("Found string 'selenium' in window's title")
        # except Exception as e:
        #     print('Something was wrong', format(e))
        if 'selenium266' in homepage.get_title():
            print("Found string 'selenium' in window's title")
        else:
            print("Couldn't match the title.")

    def test_search_2(self):
        """关键字Python查找"""
        homepage = HomePage(self.driver)
        homepage.type_search('Python')
        homepage.send_submit_btn()
        time.sleep(3)
        homepage.take_window_img()


if __name__ == '__main__':
    unittest.main()

