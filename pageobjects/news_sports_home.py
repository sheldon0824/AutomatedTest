from framework.base_page import BasePage


class SportsNewsHomePage(BasePage):
    # Sports Video的入口
    video_link = "xpath=>//*/div[@class='mod']/div[@class='hd']/h3/a"

    def click_video(self):
        self.click(self.video_link)
        self.sleep(2)