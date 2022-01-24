import sys
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#place the same chrome driver version as of your browser version

def Download_CSV(path):
    driver=webdriver.Chrome(executable_path=r'C:\Users\91739\Documents\chromedriver.exe')
    driver.get(path)

    search_item=driver.find_element_by_xpath('//*[@id="Term"]')
    search_item.send_keys('wells Fargo')
    search_button=driver.find_element_by_xpath('//*[@id="btnSubmit"]')

    search_button.click()
    time.sleep(5)
    ##button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.dismiss')))
    ##button.click()
    button = driver.find_element_by_id(u"btnDownload")
    button.click()


Download_CSV('https://www.ffiec.gov/npw/')

