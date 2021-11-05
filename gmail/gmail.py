from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
url='https://stackoverflow.com/users/signup?ssrc=head&returnurl=%2Fusers%2Fstory%2Fcurrent%27'

cap=webdriver.DesiredCapabilities.CHROME

service=Service("C:\\browserdrivers\\chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver=webdriver.Chrome(service=service,options=options,desired_capabilities=cap)

# driver.get(url)

# driver.find_element_by_css_selector('input[type=email').send_keys("anshikakaura20@gmail.com")
# driver.find_element_by_class_name('VfPpkd-LgbsSe').click()

# driver.find_element_by_css_selector('input[type=password').send_keys("ansh20122000")
# driver.find_element_by_class_name('VfPpkd-LgbsSe').click()
try:
        driver.get(url)
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='openid-buttons']/button[1]").click()
        driver.find_element_by_xpath('//input[@type="email"]').send_keys("rupaligupta2707@gmail.com")
        driver.find_element_by_xpath('//*[@id="identifierNext"]').click()
        time.sleep(3)
        driver.find_element_by_xpath('//input[@type="password"]').send_keys("Rupali@123")
        driver.find_element_by_xpath('//*[@id="passwordNext"]').click()
        time.sleep(3)
        driver.get("https://mail.google.com")
        time.sleep(3)
        
    # driver.find_element_by_css_selector('input[type=email').send_keys("anshikakaura20@gmail.com")
        # driver.find_element_by_class_name('VfPpkd-LgbsSe').click()
        # time.sleep(3)
        
        # pass_input=driver.find_element_by_css_selector('input[type="password"]')
        # pass_input.send_keys("ansh20122000")

        # next_btn=driver.find_element_by_class_name('VfPpkd-LgbsSe')

        # next_btn.click()
        
except:
        print("Sorry ! You are dividing by zero ")
