from subprocess import CREATE_NO_WINDOW
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import chromedriver_autoinstaller
import os
from tkinter import *


chromedriver_autoinstaller.install()

path = os.getcwd()
f = open(path+"/"+"x.txt", "r", encoding='utf-8')
firstline = f.readlines()
array = ['','']
id_array = ['']
pw_array = ['']

i=0

for line in firstline:
    line = line.strip()
    array[i] = line
    i += 1
f.close()

id_num = 0
pw_num = 0

for j in range(0,len(array)):
    if (j % 2 == 0):
        id_array[id_num] = array[j]
        id_num += 1
    else:
        pw_array[pw_num] = array[j]
        pw_num += 1

def main_start():
    
    for i in range(0,len(id_array)):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        driver = webdriver.Chrome(options=options)
        driver.set_window_size(1440,900)
        driver.get('https://archeage.xlgames.com/')
        time.sleep(1)
        if(driver.current_url != 'https://archeage.xlgames.com/'):
            driver.find_element_by_xpath('/html/body/div/div/a').click()
        driver.find_element_by_xpath('/html/body/div[2]/section[2]/article/div/div[4]/div/div[2]/div[1]/a').click()
    
        driver.find_element_by_id('id_field').send_keys(id_array[i])
        driver.find_element_by_id('pw_field').send_keys(pw_array[i])
        driver.find_element_by_class_name('btn-login-form').click()
        time.sleep(1)

        if(driver.current_url == 'https://member.xlgames.com/user/mypage/changepassword?redirect=true'):
            time.sleep(1)
            driver.find_element_by_class_name('btn-cancel').click()

            time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[2]/section[2]/div[2]/a/img').click()
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/a').click()
        time.sleep(1)
        driver.close()
    

main_start()

