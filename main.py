from selenium import webdriver
import time
import chromedriver_autoinstaller
import os
from tkinter import *


chromedriver_autoinstaller.install()

path = os.getcwd()
f = open(path+"/"+"x.txt", "r", encoding='utf-8')
firstline = f.readlines()
array = ['','','','','','','','','','']
id_array = ['','','','','']
pw_array = ['','','','','']

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
        driver.get('https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EC%95%84%ED%82%A4%EC%97%90%EC%9D%B4%EC%A7%80')
        driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[1]/section[1]/div[2]/div[1]/div/div[2]/dl/div[5]/dd/a[2]').click()
        driver.close()
        driver.switch_to.window(driver.window_handles[0])

        if(driver.current_url != 'https://archeage.xlgames.com/?searchCookie=true'):
            driver.find_element_by_class_name('link-home').click()

        driver.find_element_by_xpath('/html/body/div[2]/section[2]/article/div/div[4]/div/div[2]/div[1]/a').click()
    
        driver.find_element_by_id('id_field').send_keys(id_array[i])
        driver.find_element_by_id('pw_field').send_keys(pw_array[i])
        driver.find_element_by_class_name('btn-login-form').click()
        time.sleep(1)

        if(driver.current_url == 'https://member.xlgames.com/user/mypage/changepassword?redirect=true'):
            time.sleep(1)
            driver.find_element_by_class_name('btn-cancel').click()

            time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[2]/section[2]/div[1]/div[1]/div/div[2]/div[4]/a').click()
        time.sleep(1)
        iframe = driver.find_element_by_id('eventFrame')
        driver.switch_to.frame(iframe)
        driver.find_element_by_class_name('link-gift ').click()
        time.sleep(1)
        driver.close()
    

main_start()

