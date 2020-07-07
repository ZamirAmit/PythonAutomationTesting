from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import psutil
import traceback
import random
import string
import time
import datetime


def get_random_letters(number):
    enter = ""
    for x in range(number):
        enter += random.choice(string.ascii_letters)
    return enter

def get_random_phone():
    
    first = '%03d' % random.randint(0,999)
    second = '%02d' % random.randint(0,99)
    third = '%03d' % random.randint(0,999)
    phone = first + "-" + second + "-" + third
    return phone

# Define the URL's we will open and a few other variables
main_url = "C:\\Users\\Administrator\\Desktop\\Python\\form.html"  # URL A
chromedriver = "C:\\Users\\Administrator\\.vscode\\extensions\\chromedriver.exe"
# Open main window with URL A
browser = webdriver.Chrome(chromedriver)
browser.get(main_url)

# Input referance:
f_name = browser.find_element_by_name("fname")  # Text value
pwd = browser.find_element_by_name("pwd")  # Password value
gender = browser.find_elements_by_name(
    "gender")  # Opions value (3 combinations)
cars = browser.find_elements_by_xpath("//*[@type='checkbox']")
# Checkboxes value (8 combinations) - [0],[1],[2],[3],[1,2],[1,3],[2,3],[1,2,3]
birth = browser.find_element_by_id("birthday")  # Date value
bday = browser.find_element_by_id("bdaymonth")
qun = browser.find_element_by_id("quantity")  # Number value 0 <= x <= 5
search = browser.find_element_by_id("gsearch")  # Text value
rng = browser.find_element_by_id("vol")  # Range Value (50 combinations)
phone = browser.find_element_by_name("phone") # Phone value [3-2-3]
clock = browser.find_element_by_name("appt")
homepage = browser.find_element_by_id("homepage")
week = browser.find_element_by_id("week")
select = browser.find_elements_by_xpath("//*[@id='cars']/option")


# Data insertion:
number = 8
enter = get_random_letters(number)
f_name.send_keys(enter)
enter = get_random_letters(number)
pwd.send_keys(enter)
gender[0].click()
for car in cars:
    car.click()
birth.send_keys("12-13-2019")
bday.send_keys("12" + Keys.TAB + "1222")
qun.send_keys(3)
search.send_keys(enter)
repeat = 10
rng.send_keys(Keys.RIGHT * repeat)
phone_number = get_random_phone()
phone.send_keys(phone_number)
clock.send_keys("12" + "12" + "PM")
homepage.send_keys("http://www.ggg.com")
week.send_keys("12" + "2999")
select[1].click()

inputs = browser.find_elements_by_xpath("//form/*[@name]")
result = {}
for input in inputs:
    result[input.get_attribute('name')] = input.get_attribute('value')

# print(result)
# time.sleep(20)
# Submiting form:
submit = browser.find_element_by_xpath("//*[@type='submit']")
submit.click()
time.sleep(5)
if(main_url != browser.current_url):
    result["pass"] = "True"

browser.close()
print(result)