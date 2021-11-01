import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from threading import Thread
import pyautogui

hostname = "107.175.58.164"
port = "12345"
proxy_username = "555"
proxy_password = "555"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
chrome_options = Options()
chrome_options.add_argument('--proxy-server={}'.format(hostname + ":" + port))
driver = webdriver.Chrome(options=chrome_options,executable_path="C:\\browserdrivers\\chromedriver.exe")


def enter_proxy_auth(proxy_username, proxy_password):
    time.sleep(1)
    pyautogui.typewrite(proxy_username)
    pyautogui.press('tab')
    pyautogui.typewrite(proxy_password)
    pyautogui.press('enter')


def open_a_page(driver, url):
    driver.get(url)

Thread(target=open_a_page, args=(driver, "http://www.example.com/")).start()
Thread(target=enter_proxy_auth, args=(proxy_username, proxy_password)).start()

time.sleep(8)
