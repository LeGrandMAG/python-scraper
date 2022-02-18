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

import time





chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)


#specify the path to chromedriver.exe (download and save on your computer)
driver = webdriver.Chrome('C:/Users/maglo/chromedriver.exe',options=chrome_options)

wait = WebDriverWait(driver, 10)
#open the webpage ( I am using the mobile.facebook because it has less functionalilty so it will be "harder" for facebook bot to track us?!)
driver.get("https://mobile.facebook.com/groups/3323854697841336/", )

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

driver.implicitly_wait(2)
#target the login button and click it
button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='button']"))).click()

links = []
titles = []

try:
    element = driver.find_element(By.CLASS_NAME, "_7hkg").get_attribute('href')
except:
    print("This class does not exist")  

driver.implicitly_wait(2)
time.sleep(5)

#I was worried that the webdrive would not identify the different page, so I had to wait and press the "END" Key multiple times
webdriver.ActionChains(driver).key_down(Keys.END).perform()
time.sleep(3)
webdriver.ActionChains(driver).key_down(Keys.END).perform()
time.sleep(3)
webdriver.ActionChains(driver).key_down(Keys.END).perform()
time.sleep(5)
class_name = ["_4gus", "_1-sk", "_4guw", "_4gut", "_5rgt _5nk5 _5msi", "_il"]

post={
    'details': []
}

love =[]

print("Now collecting the data", end="")
time.sleep(2)
for e in range(3):
    print('.', end="")
    time.sleep(2)
print('\n')

def Collect():
    for b in class_name:

        for a in range(3)
            webdriver.ActionChains(driver).key_down(Keys.END).perform()
            time.sleep(1)
        time.sleep(5)
        lili= love.append(driver.find_elements(By.CLASS_NAME, b))
        webdriver.ActionChains(driver).key_down(Keys.END).perform()*3
        print(b + " exists")
        for a in love:
            for u in a:
                ex = u.text
                if (ex not in post['details']):
                    print(ex)
                    print("---------------------------------------------------------------------------------------------------")
                    time.sleep(2)
                    post['details'].append(ex)
                    print("\n")
        time. sleep(3)
        driver.close()  
        print("Driver is closed\n")





def SaveJason():    
    a_file = open("data.json", "w", -1, 'utf-8')
    json.dump(post, a_file)
    a_file.close()

    print(">>>>>>>>>>>> HERE IS YOUR FILE <<<<<<<<<<<<\n\n"*5)
    a_file = open("data.json", "r",-1, 'utf-8')
    output = a_file.read()
    print(output)

    print("File saved successfully")


##title = "class _4gus "
##state = "_4gut"
##price = "_4guw"

##content="_il"