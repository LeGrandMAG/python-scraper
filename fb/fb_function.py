from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import os
import wget
import time
import json
import pprint
import csv
from fb_variable import post, driver, sec, scroll

from time import sleep


def WordList(mot,o):  
    n = 1
    while(n>0):
        new = str(input("Insert the keyword #" + str(n) + ": "))
        if new == '0':
            break
        else:
            mot.append(new)
            n+=1


def OpenLink(li, num,  driver):
        print("Now processing Page: "+"\n"+ li)
        driver.get(li)
        print(">>>Please wait!<<<")
        sleep(num)


def FbLogin(num, driver):

    #click the login button
    button = WebDriverWait(driver, num).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[role='button']"))).click()
    driver.implicitly_wait(num)

    #target username
    username = WebDriverWait(driver, num).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='email']")))
    password = WebDriverWait(driver, num).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='pass']")))

    #enter username and password (don't worry I made this facebook account just for doing the scrawling and and collecting data)
    username.clear()
    username.send_keys("info.sensmart@gmail.com")
    password.clear()
    password.send_keys("19734682")

    driver.implicitly_wait(num)
    sleep(3)
    #target the login button and click it



def Collect(r,e):
    action_chain = webdriver.ActionChains(driver)
    refresh = driver.refresh()
    for b in e:

        for a in range(r*3):
            action_chain.key_down(Keys.END).perform()
            sleep(1)
        refresh
        sleep(5)
        love=driver.find_elements(By.CLASS_NAME, b)
        action_chain.key_down(Keys.END).perform()
        print(b + " exists")
        for a in love:
            ex = a.text
            if (ex not in post['details']):
                print(ex)
                print("---------------------------------------------------------------------------------------------------")
                time.sleep(2)
                post['details'].append(ex)
                print("\n")
            sleep(3)
 

def SaveJason():    
    a_file = open("data.json", "a", -1, 'utf-8')
    json.dump(post, a_file)
    a_file.close()

    print(">>>>>>>>>>>> HERE IS YOUR FILE <<<<<<<<<<<<\n\n"*5)
    a_file = open("data.json", "r",-1, 'utf-8')
    output = a_file.read()
    print(output)

    print("File saved successfully")

def GoDown( num):
    webdriver.ActionChains(driver).key_down(Keys.END).perform()
    sleep(num/2)


def FindText(t):
    ms=driver.find_elements(By.XPATH,('//*[contains(text(), "' + t + '")]'))
    sleep(3)
    for m in ms:
       print(m.text)
       print("\n")
       sleep(3)

