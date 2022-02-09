from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import wget
import time
import json
import pprint
import csv



chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)


#specify the path to chromedriver.exe (download and save on your computer)
driver = webdriver.Chrome('C:/Users/maglo/chromedriver.exe',options=chrome_options)

wait = WebDriverWait(driver, 10)
#open the webpage ( I am using the mobile.facebook because it has less functionalilty so it will be "harder" for facebook bot to track us?!)
driver.get("https://mobile.facebook.com/groups_browse/your_groups", )



#click the login button
Clikclogin = button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[role='button']"))).click()
driver.implicitly_wait(10)

#target username
username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='email']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='pass']")))

#enter username and password (don't worry I made this facebook account just for doing the scrawling and and collecting data)
username.clear()
username.send_keys("info.sensmart@gmail.com")
password.clear()
password.send_keys("19734682")

driver.implicitly_wait(10)
#target the login button and click it
button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='button']"))).click()

links = []
titles = []


element = driver.find_element(By.CLASS_NAME, "_7hkg").get_attribute('href')

driver.implicitly_wait(10)
time. sleep(5)

#I was worried that the webdrive would not identify the different page, so I had to wait and press the "END" Key multiple times
webdriver.ActionChains(driver).key_down(Keys.END).perform()
time. sleep(3)
webdriver.ActionChains(driver).key_down(Keys.END).perform()
time. sleep(3)
webdriver.ActionChains(driver).key_down(Keys.END).perform()
time. sleep(3)

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "_7hkg")))


#"_7hjkg" is the class name of the in the HTML file
link = driver.find_elements(By.CLASS_NAME, "_7hkg")
for e in link:
    a = e.get_attribute('href')
    if (a != None):
        links.append(a)
        

title = driver.find_elements(By.XPATH, "//div[@class='h3z9dlai ld7irhx5 pbevjfx6 igjjae4c']")

for f in title:
    c = f.text
    if (c != None):
        titles.append(c)









#Now need to find a way to to collect the posts from the groups in the json file