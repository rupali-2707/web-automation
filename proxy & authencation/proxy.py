from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy,ProxyType
import time
from selenium.webdriver.chrome.service import Service

proxy_ip='107.175.58.164'
# proxy_ip=i[4]
proxy=Proxy()
proxy.proxy_type=ProxyType.MANUAL
proxy.http_proxy=proxy_ip
proxy.ssl_proxy=proxy_ip

cap=webdriver.DesiredCapabilities.CHROME
proxy.add_to_capabilities(cap)



service=Service("C:\\browserdrivers\\chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver=webdriver.Chrome(service=service,options=options,desired_capabilities=cap)


driver.get("https://whatismyipaddress.com")



