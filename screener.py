from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import os
import schedule
import time

next_button = '//*[@id="NextButton"]'
yes_to_ID = '//*[@id="QID2-1-label"]'
login_field = '//*[@id="username"]'
pass_field = '//*[@id="password"]'
login_user = 'username_placeholder' #Your NYU NetID goes here
login_pass = 'password_placeholder' #NYU password goes here
chromedriver_location = "./chromedriver"

def screener():
    driver = webdriver.Chrome(executable_path=chromedriver_location)
    driver.get('https://nyu.qualtrics.com/jfe/form/SV_ePNv0eXvGWgCxkq')
    driver.maximize_window()
    driver.implicitly_wait(3)
    driver.find_element_by_xpath(next_button).click()
    driver.implicitly_wait(3)
    driver.find_element_by_xpath(yes_to_ID).click()
    driver.find_element_by_xpath(next_button).click()
    driver.implicitly_wait(3)
    driver.find_element_by_xpath(login_field).send_keys(login_user)
    driver.find_element_by_xpath(pass_field).send_keys(login_pass, Keys.RETURN)
    driver.implicitly_wait(20)

screener()

#CODE FOR AUTOMATICALLY RUNNING THIS PROGRAM EVERYDAY AT 10 AM
#INVOLVES USING THE NOHUP COMMAND IN TERMINAL

#schedule.every().day.at("10:00").do(screener)

#while True:
    #schedule.run_pending()
    #time.sleep(60) # wait one minute