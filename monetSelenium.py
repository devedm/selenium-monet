from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

import time

PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)

# Monet

loginURL = "https://www.monetwfo-eu.com/Monet5/login/login.aspx"
manualURL = "https://monetanywhere.monetwfo-eu.com/Agent/ManualStatusChanging.aspx"

# Login information

company = "Tek experts 1"
username = "eddy.mena@tek-experts.com"
password = "asdqwezxc19"

# monet status

availableStatus = "01. Available/Case Work"
breakStatus = "02. Break"
lunchStatus = "03. Lunch"
endOfShiftStatus = "10. End of shift"

# open website

driver.get(loginURL)

# select the inputs and enter the information to login
try:
    companyInput = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.NAME, "txtTenantId"))
    )
    usernameInput = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.NAME, "txtUserName"))
    )
    passwordInput = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.NAME, "txtPassword"))
    )

finally:
    companyInput.send_keys(company)
    usernameInput.send_keys(username)
    passwordInput.send_keys(password)
    companyInput.send_keys(Keys.ENTER)

time.sleep(4)


# select the sidebar and go to manual status change

driver.get(manualURL)

try:
    WebDriverWait(driver,10).until(
        EC.url_to_be(manualURL)
    )
finally:
    print("we are in manual status selector")



try: 
    selectTag = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.ID, "drpActivityName"))
    )
    selectStatus = Select(selectTag)
    selectStatus.select_by_visible_text(availableStatus)

finally:
    print("1. Available selected!")

time.sleep(2)

# Select the submit button

try:
    submitButton = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.NAME, "imgSubmitActivity"))
    )

finally:    
    submitButton.click()
    print("Status submited")




# selectElement = driver.find_element(By.ID,'drpActivityName')
# selectObject = Select(selectElement)

# allAvailableOptions = selectObject.options

# print(allAvailableOptions)

# 

# submitButton = driver.find_element_by_name("imgSubmitActivity")

# submitButton.click()

# labelStatus = driver.find_element_by_id("lblActivity")

# print(labelStatus)