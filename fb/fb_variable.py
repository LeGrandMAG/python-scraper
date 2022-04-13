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


class_list = ["_4gus", "_1-sk", "_4guw", "_4gut", "_5rgt _5nk5 _5msi", "_il"]

post={
    'details': []
}
auto= ["https://mobile.facebook.com/groups/3323854697841336/?ref=group_browse",
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

words=[]
#listnum = int(input("How many word in the list: "))

sec= int(input("input the processing time: "))
scroll=int(input("input the number of time you want to scroll: "))


chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)


#specify the path to chromedriver.exe (download and save on your computer)
driver = webdriver.Chrome('C:/Users/maglo/OneDrive/Documents/chromedriver.exe',options=chrome_options)

wait = WebDriverWait(driver, 2)
#open the webpage ( I am using the mobile.facebook because it has less functionalilty so it will be "harder" for facebook bot to track us?!)



