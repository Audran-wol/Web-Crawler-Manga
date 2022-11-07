from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_EMAIL = "@WolfhardsA"
TWITTER_PASSWORD = "professional@tools"
CHROME_PATH = Service(r"C:\Users\Tiedang\Desktop\Development\chromedriver_win32\chromedriver.exe")
SPEED_TEST_URL = "https://www.speedtest.net/"
TWITTER_URL = "https://twitter.com/"


class InternetSpeedTweeterBot:
    def __init__(self):
        self.s = Service(r"C:\Users\Tiedang\Desktop\Development\chromedriver_win32\chromedriver.exe")
        self.driver = webdriver.Chrome(service=self.s)
        self.upload_speed = 0
        self.download_speed = 0

    def get_internet_speed(self):
        self.driver.get(url=SPEED_TEST_URL)
        self.driver.maximize_window()
        time.sleep(2)
        go_button = self.driver.find_element_by_class_name("start-button")
        go_button.click()
        time.sleep(50)
        self.download_speed = self.driver.find_element_by_class_name("download-speed").text
        self.upload_speed = self.driver.find_element_by_class_name("upload-speed").text
        print(self.download_speed, self.upload_speed)

    def tweet_at_provider(self):
        self.driver.get(url=TWITTER_URL)
        time.sleep(6)
        sign_button = self.driver.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div[1]/div[1]"
                                                        "/div/div[3]/div[5]/a/div")
        sign_button.click()
        time.sleep(4)
        username_field = self.driver.find_element_by_name('text')
        username_field.send_keys(TWITTER_EMAIL)
        username_field.send_keys(Keys.ENTER)
        time.sleep(4)
        password_field = self.driver.find_element_by_name('password')
        password_field.send_keys(TWITTER_PASSWORD)
        password_field.send_keys(Keys.ENTER)
        time.sleep(6)
        tweeter_click = self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/main/div/div/div/div/'
                                                          'div/div[2]/div/div[2]/div[1]/div/div/div/div[2]'
                                                          '/div[1]/div/div/div/div/div/div/div/div/div/label/'
                                                          'div[1]/div/div/'
                                                          'div/div/div[2]/div/div/div/div')
        tweeter_click.click()
        tweeter_message = self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div'
                                                            '/div[2]/div/div[2]'
                                                            '/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/'
                                                            'div/div/div'
                                                            '/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div'
                                                            '/div')
        tweeter_message.send_keys(f'Hi this is a tweet from python selenuim module am complaining about internet speed'
                                  f' in my locality its '
                                  f'{self.download_speed} for dowload and'
                                  f'{self.upload_speed} for upload speed.But when i payed they promised above '
                                  f'{PROMISED_DOWN} and {PROMISED_UP} ')

        tweet_button = self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/'
                                                         'div[2]/div/div'
                                                         '[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]')
        tweet_button.click()
        time.sleep(3)


bot = InternetSpeedTweeterBot()
bot.get_internet_speed()
bot.tweet_at_provider()


