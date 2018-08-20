from selenium import webdriver
from selenium.webdriver.common.by import By
from TMS_SP import Locators
from time import sleep
from utility import ApplicationIndependent


oBrowser=webdriver.Chrome()
sleep(2)
oBrowser.get("https://network-rctp.qa.gtnexus.com/")
oBrowser.maximize_window()

def login_properties():
    status = "Fail"
    ApplicationIndependent.writeLog(
        "The createUser function has started execution at :" + ApplicationIndependent.getDateTime(), "info")
    try:
        user_name = oBrowser.find_element(By.XPATH, Locators.locators.user_name).clear()
        user_name=oBrowser.find_element(By.XPATH, Locators.locators.user_name).send_keys("sp@gtnexus")
        sleep(2)
        pass_word=oBrowser.find_element(By.XPATH, Locators.locators.pass_word).clear()
        pass_word = oBrowser.find_element(By.XPATH, Locators.locators.pass_word).send_keys("bfqFDIZWkv6st@")
        sleep(2)
        login_button=oBrowser.find_element(By.XPATH, Locators.locators.login_button).click()

    except Exception as e:
        ApplicationIndependent.writeLog(
            "There is an error raised during the execution of the Method createUser,Exception :" + e)
        ApplicationIndependent.writeLog(
            "The createUser function has ended execution at :" + ApplicationIndependent.getDateTime(), "info")
    return status



# def set_Username():
#     login_properties.user_name()
#
# def set_password():
#     login_properties.pass_word
#
# def click_loginButton():
#     login_properties.login_button







