from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

import time
import os
import sys

print(sys.argv[0])

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Monet

loginURL = "https://www.monetwfo-eu.com/Monet5/login/login.aspx"
manualURL = "https://monetanywhere.monetwfo-eu.com/Agent/ManualStatusChanging.aspx"

# Login information

comp = "Tek experts 1"
us = "eddy.mena@tek-experts.com"
pas = sys.argv[0]

print(sys.argv[0])

# monet status

availableStatus = "01. Available/Case Work"
breakStatus = "02. Break"
lunchStatus = "03. Lunch"
endOfShiftStatus = "10. End of shift"

# TIMEOUT

timeout = 60

# open website

driver.get(loginURL)

# select the inputs and enter the information to login
try:
    companyInput = WebDriverWait(driver,timeout).until(
        EC.presence_of_element_located((By.NAME, "txtTenantId"))
    )
    usernameInput = WebDriverWait(driver,timeout).until(
        EC.presence_of_element_located((By.NAME, "txtUserName"))
    )
    passwordInput = WebDriverWait(driver,timeout).until(
        EC.presence_of_element_located((By.NAME, "txtPassword"))
    )

finally:
    companyInput.send_keys(comp)
    usernameInput.send_keys(us)
    passwordInput.send_keys(pas)
    companyInput.send_keys(Keys.ENTER)

time.sleep(4)


# select the sidebar and go to manual status change

driver.get(manualURL)

try:
    WebDriverWait(driver,timeout).until(
        EC.url_to_be(manualURL)
    )
finally:
    print("we are in manual status selector")



try: 
    selectTag = WebDriverWait(driver,timeout).until(
        EC.presence_of_element_located((By.ID, "drpActivityName"))
    )
    selectStatus = Select(selectTag)
    selectStatus.select_by_visible_text(availableStatus)

finally:
    print("1. Available selected!")

time.sleep(2)

# Select the submit button

try:
    submitButton = WebDriverWait(driver,timeout).until(
        EC.presence_of_element_located((By.NAME, "imgSubmitActivity"))
    )

finally:    
    submitButton.click()
    print("Status submited")
