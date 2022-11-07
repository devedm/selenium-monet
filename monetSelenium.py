from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

from varAuth import *
from varSelection import *
import time

# Web Driver setup 
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# ------- Methods ------- 

# this baby takes 3 input to login to the loginURL
def loginMonet(company, username, password):

    # select the inputs and enter the information to login
    try:
        companyInput = WebDriverWait(driver,timeout).until(
            EC.presence_of_element_located((By.ID, IDMonetLoginInputCompany))
        )
        usernameInput = WebDriverWait(driver,timeout).until(
            EC.presence_of_element_located((By.ID, IDMonetLoginInputUsername))
        )
        passwordInput = WebDriverWait(driver,timeout).until(
            EC.presence_of_element_located((By.ID, IDMonetLoginInputPassword))
        )

    finally:
        companyInput.send_keys(company)
        usernameInput.send_keys(username)
        passwordInput.send_keys(password)
        companyInput.send_keys(Keys.ENTER)
        print('Monet Login Completed')
    
    time.sleep(timeoutAfter)

# this one takes 2 input to access the second verification to the Tek-experts.com domain
def loginTek(email, password):
    # enter the email
    try:
        # wait until the input is loaded
        email_second_verification = WebDriverWait(driver,timeout).until(
            EC.presence_of_element_located((By.ID, IDTekLoginInputEmail))
        )

    finally:
        # enter the value in the input element and continue
        email_second_verification.send_keys(email)
        email_second_verification.send_keys(Keys.ENTER)

        print('Tek Email entered')

    # enter the password

    time.sleep(timeoutAfter)
    try:
        # wait until the input is loaded
        pas_second_verification = WebDriverWait(driver,timeout).until(
            EC.presence_of_element_located((By.ID, IDTekLoginInputPassword))
        )


    finally:
        # enter the value in the input element and continue
        pas_second_verification.send_keys(password)
        pas_second_verification.send_keys(Keys.ENTER)

        print('Tek Password entered')

    time.sleep(timeoutAfter)

    # acept to remain loged in -> check box

    try:
        # wait until the button is loaded
        persist_login = WebDriverWait(driver,timeout).until(
            EC.presence_of_element_located((By.ID, IDTekLoginButtonPersistLogin))
        )
        
    finally:
        # click the element to continue
        persist_login.click()
        print('Acepted -> Tek keep the session on')

    time.sleep(timeoutAfter)


def goToUrl(url):
    driver.get(url)
    try:
        WebDriverWait(driver,timeout).until(
            EC.url_to_be(url)
        )
    finally:
        print(f"We went to {url}")
    
    time.sleep(timeoutAfter)


def clickOnId(id):
    try:
        redirectButton = WebDriverWait(driver,timeout).until(
            EC.presence_of_element_located((By.ID, id))
        )

    finally:
        redirectButton.click()
        print(f'Clicked on Id: {id}')
    
    time.sleep(timeoutAfter)

# Select Aux in the New Portal
def selectAux(auxiliar):
    try: 
        selectTag = WebDriverWait(driver,timeout).until(
            EC.presence_of_element_located((By.ID, IDAuxDropDown))
        )
        selectStatus = Select(selectTag)
        selectStatus.select_by_visible_text(auxiliar)

    finally:
        print(f"The auxiliar : {auxiliar} has been selected")

    # Select the submit button

    try:
        submitButton = WebDriverWait(driver,timeout).until(
            EC.presence_of_element_located((By.ID, IDSubmitAuxiliarButton))
        )

    finally:
        submitButton.click()
        print("Submit button clicked")

    print(f"The aux {auxSelected} was changed succesfully")

# -- Workflow --

# go to Monet URL
goToUrl(monetURL)

# Login to Monet
loginMonet(company, userName, passCode)

# Login with Tek Account
loginTek(userName, passCode)

# Redirecting to New Portal
clickOnId(IDRedirectLink)

selectAux(auxSelected)

print("The session is closing")
driver.quit()
