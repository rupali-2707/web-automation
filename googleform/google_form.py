from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.proxy import Proxy,ProxyType
import csv
import json


# service=Service("C:\\browserdrivers\\chromedriver.exe")
# options = webdriver.ChromeOptions()
# options.add_experimental_option('excludeSwitches', ['enable-logging'])
# driver=webdriver.Chrome(service=service,options=options)




# driver.get("https://docs.google.com/forms/d/e/1FAIpQLSdjPY9_tLoqfCzue8FEpj9w5scfw3rfO6VjTQQzyKFmzWssBA/viewform")
# time.sleep(2)




# ####################Opening JSON file ###################################3

# with open('data.json') as json_file:
#     data = json.load(json_file)
# print(type(data))

# for dic in data:
#     for key in dic:
#         if key == "firstName":
#             fn=driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(dic[key])
#         if key =="lastName":
#             ln=driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(dic[key])
#         if key == "email":
#             email=driver.find_element_by_css_selector('input[type=email]').send_keys([dic[key]])
#         if key=="phone number":
#             ph=driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(dic[key])
    
#     time.sleep(2)
#     sub=driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span').click()

#     an=driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[4]/a[2]').click()









 #############################with csv file###################

 
with open('data.csv', newline='') as f:
    reader = csv.reader(f)
    list1 = list(reader)

print(list1) 


for i in list1:

            
        proxy_ip=i[4]
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
        # time.sleep(5)
        # fn=driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(i[0])
        # time.sleep(3)
        # ln=driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(i[1])
        # time.sleep(3)
        # email=driver.find_element_by_css_selector('input[type=email]').send_keys([i[2]])
        # time.sleep(3)
        # ph=driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(i[3])
        # time.sleep(3)
        # sub=driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span').click()

        # # an=driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[4]/a[2]').click()

