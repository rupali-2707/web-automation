import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from urllib.parse import urlparse
import os
import custom_logger

logger = custom_logger.get_logger(__name__)


def validIP(address):
        parts = address.split(".")
        if len(parts) != 4:
            return False
        for item in parts:
            if not 0 <= int(item) <= 255:
                return False
        return True

def url_validator(x):
    try:
        result = urlparse(x)
        return all([result.scheme, result.netloc])
    except:
        return False

def open_mail():
    try:
        time.sleep(6)
        driver.find_element_by_xpath("/html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/div[2]/div/div[1]/div/div[1]/div[9]/div/div[1]/div[3]/div/table/tbody/tr[1]").click()
        time.sleep(5)
    except:
        driver.find_element_by_xpath("/html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/div[2]/div/div[1]/div/div/div[8]/div/div[1]/div[3]/div/table/tbody/tr[1]").click()
        time.sleep(5)

        
def starred_mail():
    print("starred :")
    time.sleep(5)
    try:
        driver.find_element_by_xpath("/html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/div[2]/div/div[1]/div/div[2]/div/table/tr/td[1]/div[2]/div[2]/div/div[3]/div/div/div/div/div/div[1]/div[2]/div[1]/table/tbody/tr[1]/td[2]/div/div/span").click()
        print("\t\tstarred done!!!!")
        time.sleep(5)
    except:
        print("\t\t failed")

def important_marked():
    print("important : ")
    time.sleep(5)
    driver.find_element_by_xpath(
            "/html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/div[1]/div[2]/div[1]/div/div[5]/div").click()
    time.sleep(4)
    try:
        driver.find_element_by_xpath("//*[text()='Mark as important']").click()
        time.sleep(4)
        print("\t\tMark as important successfully")
    except:
        print("\t\tAlready important")
        # time.sleep(3)
        # driver.find_element_by_xpath(
        #         "/html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/div[1]/div[3]/div[1]/div/div[5]/div").click()
    time.sleep(4)

def archieve():
    print("archieve : ")
    try:
        try:
            driver.find_element_by_xpath(
                '/html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/div[1]/div[2]/div[1]/div/div[2]/div[1]/div').click()
            print("\t\tArchive successfully")
        except:
            driver.find_element_by_xpath(
                '/html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/div[1]/div[3]/div[1]/div/div[2]/div[1]/div').click()
            print("\t\tArchive successfully")
            time.sleep(5)
    except:
        print("\t\tfailed")

def go_back():
    try:
        driver.find_element_by_xpath("/html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/div[1]/div[2]/div[1]/div/div[1]/div/div").click()
    except:
        driver.find_element_by_xpath("//input[@placeholder='Search mail']").click()
        driver.implicitly_wait(4)
        driver.find_element_by_xpath("//input[@placeholder='Search mail']").clear()
        driver.implicitly_wait(4)
        driver.find_element_by_xpath("//input[@placeholder='Search mail']").send_keys("is:unread in:inbox")
        driver.implicitly_wait(4)
        driver.find_element_by_xpath("//input[@placeholder='Search mail']").send_keys(Keys.ENTER)
        print("\t\tbackk")
        time.sleep(5)




def inbox(count):

        time.sleep(4)
        driver.find_element_by_xpath("//input[@placeholder='Search mail']").click()
        driver.implicitly_wait(4)
        driver.find_element_by_xpath("//input[@placeholder='Search mail']").clear()
        driver.implicitly_wait(4)
        driver.find_element_by_xpath("//input[@placeholder='Search mail']").send_keys("is:unread in:inbox")
        driver.implicitly_wait(4)
        driver.find_element_by_xpath("//input[@placeholder='Search mail']").send_keys(Keys.ENTER)
        time.sleep(3)
        for i in range(0,count):
                print(i)
                open_mail()
                starred_mail()
                important_marked()
                archieve()
                go_back()

        


PROXY_HOST = '107.175.58.164' #input("Enter proxy: ")
PROXY_PORT = '12345' #input("Enter Port: ")
PROXY_USER = '555'
PROXY_PASS = '555'

manifest_json = """
{
    "version": "1.0.0",
    "manifest_version": 2,
    "name": "Chrome Proxy",
    "permissions": [
        "proxy",
        "tabs",
        "unlimitedStorage",
        "storage",
        "<all_urls>",
        "webRequest",
        "webRequestBlocking"
    ],
    "background": {
        "scripts": ["background.js"]
    },
    "minimum_chrome_version":"22.0.0"
}
"""
background_js = """
var config = {
        mode: "fixed_servers",
        rules: {
          singleProxy: {
            scheme: "http",
            host: "%s",
            port: parseInt(%s)
          },
          bypassList: ["localhost"]
        }
      };

chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});

function callbackFn(details) {
    return {
        authCredentials: {
            username: "%s",
            password: "%s"
        }
    };
}

chrome.webRequest.onAuthRequired.addListener(
            callbackFn,
            {urls: ["<all_urls>"]},
            ['blocking']
);
""" % (PROXY_HOST, PROXY_PORT, PROXY_USER, PROXY_PASS)



url='https://gmail.com'  #enter your url





print("Script Started...")


if(validIP(PROXY_HOST)):

        if(url_validator(url)):
            start = int(input("Start profile: "))
            end = int(input("End profile: "))

            
            for x in range(start, end):
                    print(f"Running profile: {x} from range({start}-{end})")
                    username = os.getlogin()
                    cap=webdriver.DesiredCapabilities.CHROME
                    service=Service("C:\\browserdrivers\\chromedriver.exe")
                    options = webdriver.ChromeOptions()
                    chrome_driver = r"C:\\browserdrivers\\chromedriver.exe"
                    options.add_argument("--log-level=3")
                    options.add_argument("user-data-dir=C:/Users/{username}/Desktop/selen/{x}".format(x=x, username=username))

                    driver = None

                    try:
                         driver=webdriver.Chrome(service=service,options=options,desired_capabilities=cap)
                         driver.get(url)

                    except Exception as e:
                        if driver:
                         driver.quit()
                        print(e)

                    try:
                        # spam(2)
                        inbox(3)
                    except Exception as e:
                        print("Error occurred", e)
                        logger.error(f"Error Running profile: {x} from range({start}-{end})")

                    print("\t{x}: Finished...".format(x=x))
                    driver.quit()
        else:

            print("Wrong url")
            exit()
else:

    print("wrong IP Address")
    exit()
            # try:
            #     cap=webdriver.DesiredCapabilities.CHROME
            #     service=Service("C:\\browserdrivers\\chromedriver.exe")
            #     options = webdriver.ChromeOptions()
            #     options.add_experimental_option('excludeSwitches', ['enable-logging'])
            #     driver=webdriver.Chrome(service=service,options=options,desired_capabilities=cap)
            #     driver.get(url)
            # except Exception as e:
            #     if driver:
            #         driver.quit()
            #     print(e)

              
        