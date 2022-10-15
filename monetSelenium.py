
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

#print(sys.argv[0])

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Monet

loginURL = "https://www.monetwfo-eu.com/Monet5/login/login.aspx"
manualURL = "https://monetanywhere.monetwfo-eu.com/Agent/ManualStatusChanging.aspx"

# Login information

comp = "Tek experts 1"
us = ""
pas = ""

#print(sys.argv[0])

# monet status

availableStatus = "01. Available/Case Work"
breakStatus = "02. Break"
lunchStatus = "03. Lunch"
endOfShiftStatus = "10. End of shift"


# Second Verification Variables

second_authentication_email_input_id = 'i0116'
second_authentication_pass_input_id = 'i0118'
second_authentication_acept_input_id = 'idSIButton9'


# Second Login Information

t_email = ''
t_pas = ''

# TIMEOUT

timeout = 60
timeoutAfter = 3

# ------- Methods ------- 

# this baby takes 3 input to login to the loginURL
def loginMonetFirst(company, username, password):

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
        companyInput.send_keys(company)
        usernameInput.send_keys(username)
        passwordInput.send_keys(password)
        companyInput.send_keys(Keys.ENTER)
    
    time.sleep(timeoutAfter)

# this one takes 2 input to access the second verification to the Tek-experts.com domain
def loginMonetSecond(email, password):
    # enter the email
    try:
        # wait until the input is loaded
        email_second_verification = WebDriverWait(driver,timeout).until(
            EC.presence_of_element_located((By.ID, second_authentication_email_input_id))
        )

    finally:
        # enter the value in the input element and continue
        email_second_verification.send_keys(email)
        email_second_verification.send_keys(Keys.ENTER)

        print('Email entered')

    # enter the password

    time.sleep(timeoutAfter)
    try:
        # wait until the input is loaded
        pas_second_verification = WebDriverWait(driver,timeout).until(
            EC.presence_of_element_located((By.ID, second_authentication_pass_input_id))
        )


    finally:
        # enter the value in the input element and continue
        pas_second_verification.send_keys(password)
        pas_second_verification.send_keys(Keys.ENTER)

        print('Password entered')

    time.sleep(timeoutAfter)

    # acept to remain loged in -> check box

    try:
        # wait until the button is loaded
        acept_second_verification = WebDriverWait(driver,timeout).until(
            EC.presence_of_element_located((By.ID, second_authentication_acept_input_id))
        )


    finally:
        # click the element to continue
        acept_second_verification.click()
        print('Acepted -> keep the session on')

    time.sleep(timeoutAfter)

def goToUrl(url):
    driver.get(url)
    try:
        WebDriverWait(driver,timeout).until(
            EC.url_to_be(url)
        )
    finally:
        print("We are in manual status selector")
    
    time.sleep(timeoutAfter)


# 
def selectAux(auxiliar):
    try: 
        selectTag = WebDriverWait(driver,timeout).until(
            EC.presence_of_element_located((By.ID, "drpActivityName"))
        )
        selectStatus = Select(selectTag)
        selectStatus.select_by_visible_text(auxiliar)

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
        print('Selected -> ', auxiliar)

# ------- Running Process ------- 

# open website

goToUrl(loginURL)

# Login to Monet

loginMonetFirst(comp, us, pas)

# Second Authentication

loginMonetSecond(t_email,t_pas)

# Select the sidebar and go to manual status change

goToUrl(manualURL)

# change Aux
'''
availableStatus = "01. Available/Case Work"
breakStatus = "02. Break"
lunchStatus = "03. Lunch"
endOfShiftStatus = "10. End of shift"
'''

selectAux(breakStatus)

# end the session :D
time.sleep(2)
print("Closing session")
driver.quit ()
