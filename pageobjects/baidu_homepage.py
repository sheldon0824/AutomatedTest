from framework.base_page import BasePage


class HomePage(BasePage):
    """
    可以这样设想，一个page object可以先将一个页面的所有element都列出来，
    对每个element都进行命名，即变量名，并写出它的定位方式
    """
    input_box = "id=>kw"  # 搜索的输入框。为每一个element取一个名字并赋值它的定位方式
    search_submit_btn = "xpath=>//*[@id='su']"  # 搜索提交按钮
    baidu_news = "xpath=>//*[@id='u1']/a[1]"

    def type_search(self, text):
        self.type(self.input_box, text)  # base_page.type(self, selector, text)

    def send_submit_btn(self):
        self.click(self.search_submit_btn)

    def click_news(self):
        self.click(self.baidu_news)
        self.sleep(2)
