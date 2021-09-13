from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
import time


CHROME_WEB_PATH = r"D:/chromedriver.exe"
TARGET_INSTA_ACCOUNT = "INSTA_PAGE"
USERNAME = "INSTA_USERNAME"
PASSWORD = "INSTA_PASSWORD"
NUMBER_OF_PAGES = 10


class InstaFollower:

    def __init__(self, file_path):
        self.driver = webdriver.Chrome(file_path)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(2)
        accept_all_button = self.driver.find_element_by_xpath('/html/body/div[3]/div/div/button[1]')
        accept_all_button.click()

        insta_username = self.driver.find_element_by_name("username")
        insta_username.send_keys(USERNAME)

        insta_password = self.driver.find_element_by_name("password")
        insta_password.send_keys(PASSWORD)
        insta_password.send_keys(Keys.ENTER)

        time.sleep(2)
        not_now_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
        not_now_button.click()

        time.sleep(3)
        not_now_button2 = self.driver.find_element_by_class_name("HoLwm")
        not_now_button2.click()

    def find_followers(self):
        self.driver.get(f"https://www.instagram.com/{TARGET_INSTA_ACCOUNT}")

        time.sleep(2)
        followers = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers.click()

        time.sleep(2)
        for i in range(NUMBER_OF_PAGES):
            modal = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]')
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(1)

    def follow(self):
        follow_buttons = self.driver.find_elements_by_css_selector("li button")
        for button in follow_buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[2]')
                cancel_button.click()


insta_bot = InstaFollower(CHROME_WEB_PATH)
insta_bot.login()
insta_bot.find_followers()
insta_bot.follow()

















