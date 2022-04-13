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


#class for the posts
class_name = ["_4gus", "_1-sk", "_4guw", "_4gut", "_5rgt _5nk5 _5msi", "_il"]

post={
    'details': []
}


# list of the link for the Facebook groups
auto = ["https://mobile.facebook.com/groups/3323854697841336/?ref=group_browse",
"https://mobile.facebook.com/groups/2417749508533529/?ref=group_browse",
"https://mobile.facebook.com/groups/2396795340453227/?ref=group_browse",
"https://mobile.facebook.com/groups/2232354350372325/?ref=group_browse",
"https://mobile.facebook.com/groups/1856072608051143/?ref=group_browse",
"https://mobile.facebook.com/groups/1712424082372481/?ref=group_browse",
"https://mobile.facebook.com/groups/1606567199558157/?ref=group_browse",
"https://mobile.facebook.com/groups/1549030312003177/?ref=group_browse",
"https://mobile.facebook.com/groups/1050735792104175/?ref=group_browse",
"https://mobile.facebook.com/groups/557339772259465/?ref=group_browse",
"https://mobile.facebook.com/groups/494938151630057/?ref=group_browse",
"https://mobile.facebook.com/groups/485595848653433/?ref=group_browse",
"https://mobile.facebook.com/groups/434661027871196/?ref=group_browse",
"https://mobile.facebook.com/groups/427336388401184/?ref=group_browse",
"https://mobile.facebook.com/groups/352120431828349/?ref=group_browse",
"https://mobile.facebook.com/groups/296525075547264/?ref=group_browse",
"https://mobile.facebook.com/groups/283780253092282/?ref=group_browse",
"https://mobile.facebook.com/groups/261658928421492/?ref=group_browse",
"https://mobile.facebook.com/groups/193427604794787/?ref=group_browse",
"https://mobile.facebook.com/groups/174021326556602/?ref=group_browse",
"https://mobile.facebook.com/groups/157070304903101/?ref=group_browse",
"https://mobile.facebook.com/groups/114975699094438/?ref=group_browse",
"https://mobile.facebook.com/groups/3073972669330453/?ref=group_browse",
"https://mobile.facebook.com/groups/2932215260333602/?ref=group_browse",
"https://mobile.facebook.com/groups/2777314399147797/?ref=group_browse",
"https://mobile.facebook.com/groups/2267421523507404/?ref=group_browse",
"https://mobile.facebook.com/groups/2025771334359815/?ref=group_browse",
"https://mobile.facebook.com/groups/1994886254131045/?ref=group_browse",
"https://mobile.facebook.com/groups/630353667861611/?ref=group_browse",
"https://mobile.facebook.com/groups/575029336040752/?ref=group_browse",
"https://mobile.facebook.com/groups/480658072822702/?ref=group_browse",
"https://mobile.facebook.com/groups/377436819112288/?ref=group_browse",
"https://mobile.facebook.com/groups/304222654430887/?ref=group_browse",
"https://mobile.facebook.com/groups/178202949050334/?ref=group_browse",
"https://mobile.facebook.com/groups/123383601176136/?ref=group_browse",
"https://mobile.facebook.com/groups/4458091350904337/?ref=group_browse",
"https://mobile.facebook.com/groups/1659094737714974/?ref=group_browse"]




# tuple of the phone models
PHONE_MODEL = [
    ('--Phone model--', '--Phone model--'),
    ('Iphone 5', 'Iphone 5'),
    ('Iphone 6', 'Iphone 6'),
    ('Iphone 6+', 'Iphone 6+'),
    ('Iphone7' , 'Iphone7'),
    ('Iphone 7+', 'Iphone 7+'),
    ('Iphone 8','Iphone 8'),
    ('Iphone 8+', 'Iphone 8+'),			
    ('Iphone X','Iphone X'),				
    ('Iphone XR', 'Iphone XR'),				
    ('Iphone XS max', 'Iphone XS max'),			
    ('Iphone 11', 'Iphone 11'),
    ('Iphone 11 Pro', 'Iphone 11 Pro'),	
    ('Iphone 11 Pro Max', 'Iphone 11 Pro Max'),		
    ('Iphone 12', 'Iphone 12'),	
    ('Iphone 12 pro', 'Iphone 12 pro'),		
    ('Iphone 12 pro max', 'Iphone 12 pro max'),			
    ('Iphone 13', 'Iphone 13'),	
    ('Iphone 13 pro max', 'Iphone 13 pro max'),			
    ('Samsung s6', 'Samsung s6'),				
    ('Samsung s6 edge', 'Samsung s6 edge'),				
    ('Samsung s6 edge+', 'Samsung s6 edge+'),				
    ('Samsung s7', 'Samsung s7'),				
    ('Samsung s7 edge', 'Samsung s7 edge'),			
    ('Samsung s8', 'Samsung s8'),				
    ('Samsung s8 edge', 'Samsung s8 edge'),				
    ('Samsung s8 edge+', 'Samsung s8 edge+'),				
    ('Samsung s9', 'Samsung s9'),				
    ('Samsung s10', 'Samsung s10'),				
    ('Samsung s10+', 'Samsung s10+'),				
    ('Samsung Note 8', 'Samsung Note 8'),				
    ('Samsung Note 9,', 'Samsung Note 9'),			
    ('Samsung Note 9 Duos', 'Samsung Note 9 Duos'),			
    ('Samsung Note 10', 'Samsung Note 10'),			
    ('Techno Pop3', 'Techno Pop3'),					
    ('Techno Spark4', 'Techno Spark4'),				
    ('Techno Spark 5', 'Techno Spark 5'),				
    ('Techno Spark 5 Air', 'Techno Spark 5 Air'),				
    ('Techno Camon 16s', 'Techno Camon 16s'),				
    ('Techno Camo 16', 'Techno Camo 16'),				
    ('Techno Camon 15 Premier', 'Techno Camon 15 Premier')
]



login_credential = {'email': 'info.sensmart@gmail.com',
                    'password': '19734682' }
sec= int(input("input the processing time: "))
scroll=int(input("input the number of time you want to scroll: "))

words=[]
#listnum = int(input("How many word in the list: "))
def WordList(mot,o):
    n = 1
    while(n>0):
        new = str(input("Insert the keyword #" + str(n) + ": "))
        if new == '0':
            break
        else:
            mot.append(new)
            n+=1
        

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)


#specify the path to chromedriver.exe (download and save on your computer)
driver = webdriver.Chrome('C:/Users/maglo/OneDrive/Documents/chromedriver.exe',options=chrome_options)

wait = WebDriverWait(driver, 2)
#open the webpage ( I am using the mobile.facebook because it has less functionalilty so it will be "harder" for facebook bot to track us?!)




def OpenLink(li, num):
        print("Now processing Page: "+"\n"+ li)
        driver.get(li)
        print(">>>Please wait!<<<")

def FbLogin(num):

    #click the login button
    Clikclogin = button = WebDriverWait(driver, num).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[role='button']"))).click()
    driver.implicitly_wait(num)

    #target username
    username = WebDriverWait(driver, num).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='email']")))
    password = WebDriverWait(driver, num).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='pass']")))

    #enter username and password (don't worry I made this facebook account just for doing the scrawling and and collecting data)
    username.clear()
    username.send_keys(login_credential['email'])
    password.clear()
    password.send_keys(login_credential['password'])

    driver.implicitly_wait(num)
    #target the login button and click it
    button = WebDriverWait(driver, num).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='button']"))).click()

love =[]

print("Now collecting the data", end="")
time.sleep(2)
for e in range(3):
    print('.', end="")
    time.sleep(2)
print('\n')

def Collect(r):
    action_chain = webdriver.ActionChains(driver)
    refresh = driver.refresh()
    for b in class_name:

        for a in range(r*3):
            action_chain.key_down(Keys.END).perform()
            time.sleep(1)
        refresh
        time.sleep(5)
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
        time. sleep(3)
        




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
    time.sleep(num/2)


###def FindText(t):
    ###ms=driver.find_elements(By.XPATH,('//*[contains(text(), "' + t + '")]'))
    ###time.sleep(3)
    ###for m in ms:
       ### print(m.text)
        ###print("\n")
        ###time.sleep(3)###

for n in  range(len(auto)):
    OpenLink(auto[n], sec)
    time.sleep(sec)
    l = driver.find_elements(By.ID,"mobile_login_bar")
    s = len(l)
    if(s>0):
        print(">>>Login barrier exists <<<\n")
        FbLogin(sec)
        time.sleep(3)
        print("logged in Successfully\n")
        for p in range(sec):
            GoDown(p)
        Collect(sec)
        SaveJason()
        print("successfully scrapped")

    else:
        print(">>>Login barrier does not exist <<<")
        time.sleep(2)
        print("\n You can scroll safely")
        GoDown(sec)
        for p in range(sec):
            time.sleep(sec)
            GoDown(p)
        Collect(sec)
        SaveJason()
    print("successfully scrapped")


driver.close()  
print("Driver is closed\n")
SaveJason()




##title = "class _4gus "
##state = "_4gut"
##price = "_4guw"

##content="_il"
