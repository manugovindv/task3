# -*- coding: utf-8 -*-
"""
Created on Sat May 7  08:51:28 2021

@author: Delta
"""



from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import os
import random
import requests


BRAVE_PATH = "C:\\Program Files (x86)\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"    #path of chromium based browser
CHROME_PROFILE_PATH = "user-data-dir=C:\\Users\\Manu Govind V\\AppData\\Local\\BraveSoftware\\Brave-Browser\\User Data\\wtsp"  #path to store a user session/profile


options = webdriver.ChromeOptions()
"""saving the user profile"""
options.add_argument(CHROME_PROFILE_PATH)  #needs to scan qr code only 1 time. Next time the script is run, it will use the saved user-profile
options.binary_location = BRAVE_PATH

#mention path to chromedriver
browser=webdriver.Chrome('D:\\codes\\drivers\\chromedriver.exe', options=options)


browser.get("http://www.ieeeuvce.in/posts/")
newlist = browser.find_elements_by_css_selector(".venobox.preview-link.vbox-item") #getting list of all images
print("----------------------------------------------------------------")


#choosing a random image from the gallery
url = random.choice(newlist).get_attribute("href")


print("opening wtsp-------------------------------")
browser.get("https://web.whatsapp.com/")



print("saving image----------------------------")

response = requests.get(url) 
ext = response.headers['Content-Type'].split('/')[-1] #getting image extension

print(response.headers['Content-Type'])

imgname = os.path.abspath(f"images/random_image.{ext}")

with open(imgname, "wb") as f:
    f.write(response.content)
    print("saved image")

group_name = 'note'  #change group name here
group_xpath = f'//span[@title="{group_name}"]'  

print("pressing group icon")


#group name
WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, group_xpath))).click()

#attach icon
WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@title="Attach"]'))).click()

WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]'))).send_keys(imgname)

#sendbutton
WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//span[@data-icon="send"]'))).click()



WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'))).send_keys("A random image is downloaded from the gallery and sent to this group")

WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//span[@data-icon="send"]'))).click()



time.sleep(4)
browser.get('https://www.youtube.com/watch?v=dQw4w9WgXcQ')  #just some important code XD

WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body'))).send_keys('f')

