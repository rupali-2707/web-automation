import time
import random
import zipfile
import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


import custom_logger

logger = custom_logger.get_logger(__name__)

MAXRETRY = 3

##PROXY_HOST = '191.102.152.8'
PROXY_HOST = input("Enter proxy: ")
PROXY_PORT = input("Enter Port: ")
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


def retry(func):
    def wrapper(*args, **kwargs):
        count = 1
        while count <= MAXRETRY:
            try:
                print("Attempt", count)
                return func(*args, **kwargs)
            except Exception as e:
                count += 1
                if count > 3:
                    raise e

    return wrapper


@retry
def inbox_OpenClick():
    driver.find_element_by_xpath(
        "/html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/div[2]/div/div[1]/div/div[2]/div[5]/div[2]/div/table/tbody/tr[1]/td[6]/div/div/div[3]/span/span").click()
    time.sleep(random.uniform(1, 2))
    #driver.implicitly_wait(3)
    try:
        driver.find_element_by_partial_link_text("Hi").click()
        driver.switch_to.window(driver.window_handles[-1])
        time.sleep(random.uniform(1, 2))
        # driver.implicitly_wait(2)
        driver.close()
        driver.switch_to.window(driver.window_handles[0])

        print("\t\tClick on link successfully")


    except:
        # driver.get("https://mail.google.com/mail/u/0/#search/is%3Aunread+welcome+to")
        # print("Hi Not found")
        inbox_Archive()







@retry
def inbox_Important():
    driver.find_element_by_xpath(
        "/html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/div[1]/div[3]/div[1]/div/div[5]/div").click()
    #time.sleep(random.uniform(2, 3))
    driver.implicitly_wait(3)
    try:
        driver.find_element_by_xpath("//*[text()='Mark as important']").click()
        #time.sleep(random.uniform(1, 2))
        driver.implicitly_wait(2)
        print("\t\tMark as important successfully")
    except:
        print("\t\tAlready important")
        driver.find_element_by_xpath(
            "/html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/div[1]/div[3]/div[1]/div/div[5]/div").click()
    #time.sleep(random.uniform(2, 3))
    driver.implicitly_wait(3)


@retry
def inbox_Star():
    driver.find_element_by_xpath(
        "/html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/div[1]/div[3]/div[1]/div/div[5]/div").click()
    #time.sleep(random.uniform(2, 3))
    driver.implicitly_wait(3)
    try:
        driver.find_element_by_xpath("//*[text()='Add star']").click()
        #time.sleep(random.uniform(1, 2))
        driver.implicitly_wait(3)
        print("\t\tAdd star successfully")
    except:
        print("\t\tAlready marked star")
        driver.find_element_by_xpath(
            "/html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/div[1]/div[3]/div[1]/div/div[5]/div").click()
    #time.sleep(random.uniform(1, 2))
    driver.implicitly_wait(3)


@retry
def inbox_Archive():
    try:
        driver.find_element_by_xpath(
            '/html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/div[1]/div[2]/div[1]/div/div[2]/div[1]/div').click()
        print("\t\tArchive successfully")
    except:
        driver.find_element_by_xpath(
            '/html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/div[1]/div[3]/div[1]/div/div[2]/div[1]/div').click()
        print("\t\tArchive successfully")

    try:
        driver.implicitly_wait(10)
        driver.get("https://mail.google.com/mail/u/0/#search/is%3Aunread+Auto+Insurance+OR+best_senior_deals")
    except:
        driver.implicitly_wait(10)
        driver.find_element_by_xpath(
            "/html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/div[1]/div[3]/div[1]/div/div[1]/div/div").click()

        #driver.get("https://mail.google.com/mail/u/0/#search/is%3Aunread+welcome+to")


    #time.sleep(random.uniform(1, 2))
    driver.implicitly_wait(10)


@retry
def inbox(count):
    try:
        print("\tInbox reporting start...")
        driver.find_element_by_xpath("//input[@placeholder='Search mail']").click()
        driver.implicitly_wait(4)
        driver.find_element_by_xpath("//input[@placeholder='Search mail']").clear()
        driver.implicitly_wait(4)
        driver.find_element_by_xpath("//input[@placeholder='Search mail']").send_keys("is:unread in:inbox Auto Insurance OR best_senior_deals")
        driver.implicitly_wait(4)
        driver.find_element_by_xpath("//input[@placeholder='Search mail']").send_keys(Keys.ENTER)
        time.sleep(random.uniform(15, 25))

    except Exception as e:
        driver.get("https://mail.google.com/mail/u/0/#search/is%3Aunread+Auto+Insurance+OR+best_senior_deals")
        print(e)
        time.sleep(random.uniform(15, 25))

    for x in range(count):
        try:
            inbox_OpenClick()
            inbox_Important()
            inbox_Star()
            inbox_Archive()
            print("\t\tOpen&Click&Important&Archive for message n {n} successfully".format(n=x + 1))
        except:
            print("\t\tOpen&Click&Important&Archive for message n {n} failed".format(n=x + 1))
        time.sleep(random.uniform(1, 2))
        driver.implicitly_wait(3)


@retry
def spam(count):
    print("\tSpam reporting start...")
    driver.implicitly_wait(5)
    driver.find_element_by_xpath("//input[@placeholder='Search mail']").click()
    driver.find_element_by_xpath("//input[@placeholder='Search mail']").clear()
    driver.find_element_by_xpath("//input[@placeholder='Search mail']").send_keys("in:spam Welcome to")
    driver.find_element_by_xpath("//input[@placeholder='Search mail']").send_keys(Keys.ENTER)
    #time.sleep(random.uniform(15, 20))
    driver.implicitly_wait(30)
    for x in range(count):
        try:
            driver.find_element_by_xpath(
                "/html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/div[2]/div/div[1]/div/div[2]/div[5]/div[2]/div/table/tbody/tr[1]/td[6]/div/div/div[3]/span/span").click()
            #time.sleep(random.uniform(2, 3))
            driver.implicitly_wait(2)
            driver.find_element_by_xpath(
                "/html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/div[1]/div[3]/div[1]/div/div[5]/div").click()
            #time.sleep(random.uniform(1, 2))
            driver.implicitly_wait(2)
            try:
                driver.find_element_by_xpath("//*[text()='Mark as important']").click()
                #time.sleep(random.uniform(1, 2))
                driver.implicitly_wait(2)
                print("\t\tMark as important successfully")
            except:
                print("\t\tAlready important")
            #time.sleep(random.uniform(1, 2))
            driver.implicitly_wait(2)
            driver.find_element_by_xpath(
                "/html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/div[2]/div/div[1]/div/div[3]/div/table/tr/td[1]/div[2]/div[2]/div/div[3]/div/div/div/div/div/div[1]/div[2]/div[2]/div[1]/div/div[2]/div/button").click()
            print("\t\tOpen&Important&Not spam for message n {n} successfully".format(n=x + 1))
        except:
            print("\t\tOpen&Important&Not spam for message n {n} failed".format(n=x + 1))
        #time.sleep(random.uniform(2, 3))
        driver.implicitly_wait(3)


print("Script Started...")

start = int(input("Start profile: "))
end = int(input("End profile: "))

while True:
    for x in range(start, end):
        print(f"Running profile: {x} from range({start}-{end})")
        username = os.getlogin()
        options = webdriver.ChromeOptions()
        chrome_driver = r"C:\\browserdrivers\\chromedriver.exe"
        pluginfile = 'proxy_auth_plugin.zip'
        with zipfile.ZipFile(pluginfile, 'w') as zp:
            zp.writestr("manifest.json", manifest_json)
            zp.writestr("background.js", background_js)
        options.add_extension(pluginfile)
        options.add_argument("--log-level=3")
        options.add_argument("user-data-dir=C:/Users/{username}/Desktop/selen/{x}".format(x=x, username=username))

        driver = None

        try:

            driver = webdriver.Chrome(executable_path=chrome_driver, options=options)
            driver.set_window_size(1200, 1000)
            print(driver.get_window_size())

            driver.get("https://mail.google.com/mail/u/0/#inbox")
        except Exception as e:
            if driver:
                driver.quit()
            print(e)
            logger.error(f"Error Running profile: {x} from range({start}-{end})")
            continue

        #time.sleep(random.uniform(5, 7))
        driver.implicitly_wait(10)

        try:
            driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td/p[2]/font/a[1]').click()
        except:
            pass

        try:

            driver.find_element_by_partial_link_text("Inbox").click()
            #time.sleep(random.uniform(2, 3))
            driver.implicitly_wait(10)
        except:
            driver.refresh()
            #time.sleep(random.uniform(3, 5))
            driver.implicitly_wait(10)

        try:
            # spam(2)
            inbox(102)
        except Exception as e:
            print("Error occurred", e)
            logger.error(f"Error Running profile: {x} from range({start}-{end})")

        print("\t{x}: Finished...".format(x=x))
        driver.quit()

print("Script Finished...")
