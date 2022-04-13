from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep
from openpyxl import Workbook,load_workbook


chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)


url = 'https://everytime.kr/login'
timetable = 'https://everytime.kr/timetable'
driver = webdriver.Chrome('C:/Users/maglo/OneDrive/Documents/chromedriver.exe',options=chrome_options)





def LogIn():
    driver.get(url)
    sleep(3)
    driver.find_element_by_name('userid').send_keys('201800071')
    driver.find_element_by_name('password').send_keys('magl0ire596')
    driver.find_element_by_xpath('//*[@id="container"]/form/p[3]/input').click()
    sleep(5)
    print("You are logged in")



LogIn()

def Findtimetable():

    a = driver.find_element_by_xpath('//*[@id="container"]/div[2]/div[1]/form/p[2]').text
    if (a == 'MUKENDI MAGLOIRE TSHIKULU'):
        print("You are already logged in ")
        driver.get(timetable)
        sleep(3)
        driver.find_element_by_xpath('//*[@id="container"]/ul/li[1]').click()

    else:
        print("You are not logged in yet ")
        LogIn()
        driver.get(timetable)
        sleep(3)
        driver.find_element_by_xpath('//*[@id="container"]/ul/li[1]').click()


Findtimetable()

class Course():

    def __init__(self, coursename=None, category=None, courseid=None, duration=None):
        self.coursename = coursename
        self.category = category
        self.courseid = courseid
        self.duration = duration


    

    result['CoursePl'].append(tds[0].text) #Course Plan
    result['Category'].append(tds[1].text) #Category
    result['Year'].append(tds[2].text) #Year
    result['CourseID'].append(tds[3].text) #Course Code
    result['CourseName'].append(tds[4].text) #Course Name
    result['Credit'].append(tds[5].text) #Credit
    result['Duration'].append(tds[6].text) #Duration
    result['Professor'].append(tds[7].text) #Professor Name
    result['Schedule'].append(tds[8].text) #Schedule
    result['CurrentStudents'].append(tds[10].text) #CurrentStudents
    result['TotalStudents'].append(tds[11].text) #TotalStudents
    result['Note'].append(tds[12].text) #Note
    results.append(result)