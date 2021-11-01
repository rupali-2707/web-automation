from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
url='https://www.gmail.com'

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

        driver.find_element_by_css_selector('input[type=email').send_keys("anshikakaura20@gmail.com")
        driver.find_element_by_class_name('VfPpkd-LgbsSe').click()
        time.sleep(3)
        
        pass_input=driver.find_element_by_css_selector('input[type="password"]')
        pass_input.send_keys("ansh20122000")

        next_btn=driver.find_element_by_class_name('VfPpkd-LgbsSe')

        next_btn.click()
        
except ZeroDivisionError:
        print("Sorry ! You are dividing by zero ")
else:
    print("sorry")