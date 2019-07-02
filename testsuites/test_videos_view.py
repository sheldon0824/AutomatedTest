import time
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.baidu_homepage import HomePage
from pageobjects.baidu_news_home import NewsHomePage
from pageobjects.news_sports_home import SportsNewsHomePage


class ViewVideo(unittest.TestCase):

    def setUp(self):
        browser = BrowserEngine(self)
        self.driver = browser.open_browser(self)

    def tearDown(self):
        self.driver.quit()

    def test_view_video(self):
        # 初始化百度首页，并点击新闻链接
        baiduhome = HomePage(self.driver)
        baiduhome.click_news()

        # 在百度新闻页，再点击体育链接
        newshome = NewsHomePage(self.driver)
        newshome.click_sports()

        # 跳转到体育页后，再点击sports video链接
        sportsvideo = SportsNewsHomePage(self.driver)
        sportsvideo.click_video()
        sportsvideo.take_window_img()


if __name__ == '__main__':
    unittest.main()


