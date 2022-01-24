import sys
import time
import time
import random
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.common.keys import Keys
import selenium.common.exceptions

#place the same chrome driver version as of your browser version
driver=webdriver.Chrome(executable_path=r'C:\Users\91739\Documents\chromedriver.exe')




def send_message():   
    '''Find message button'''
    message = driver.find_element_by_class_name('xWeGp ')
    message.click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[1]/div[3]/div/div/div/div/div[1]').click()
    time.sleep(1)
    #import text from a file
    l=['Random message','hi','how are you?']
    for x in range(100):
        mbox = driver.find_element_by_tag_name('textarea')
        mbox.send_keys(random.choice(l))
        mbox.send_keys(Keys.RETURN)
        time.sleep(1.2)


def Spammer_Bot(user,passw):
    #login
    driver.get('https://www.instagram.com/')
    time.sleep(4) 
    username=driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
    password=driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
    #enter creds
    username.send_keys(user)
    time.sleep(1)
    password.send_keys(passw)
    time.sleep(1)

    #click login button
    login_button=driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div')
    login_button.click()
    time.sleep(4)

    not_now=driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
    not_now.click()
    notNowButton = WebDriverWait(driver, 15).until(
        lambda d: d.find_element_by_xpath('//button[text()="Not Now"]')
    )
    notNowButton .click()
    time.sleep(2)
    send_message()
    time.sleep(1)

    send_text=driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
    send_text.send_keys('Hello')


Spammer_Bot('YOUR USERNAME','PASSWORD')

