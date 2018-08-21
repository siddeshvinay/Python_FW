from selenium import webdriver
from selenium.webdriver.common.by import By
from TMS_SP import Locators
from time import sleep
from utility import ApplicationIndependent
import os


'''
Created By:
Created Date:
Reviewd By:
Modified By:
Parameters:
return Type:
Purpose:
'''

def LaunchBrowser(self):
    status="Fail"
    ApplicationIndependent.writeLog("The LaunchBrowser function has started execution at :"+ApplicationIndependent.getDateTime(),"info")
    try:
        self.oBrowser = webdriver.Chrome()
        status="Pass"
        self.oBrowser.maximize_window()
    except Exception:
        ApplicationIndependent.writeLog("The Driver Object has not created successfully!!!!","error")
    ApplicationIndependent.writeLog("The LaunchBrowser function has ended execution at :" + ApplicationIndependent.getDateTime(),"info")
    return status


'''
Created By:
Created Date:
Reviewd By:
Modified By:
Parameters:
return Type:
Purpose:
'''
def navigate(self):
    status="Fail"
    expected="actiTIME - Login"
    ApplicationIndependent.writeLog("The navigate function has started execution at :" + ApplicationIndependent.getDateTime(),"info")
    try:
        self.oBrowser.get(os.environ.get('URL', -1))
        #self.oBrowser.get("https://network-rctp.qa.gtnexus.com/")
        sleep(2)
        actual=self.oBrowser.title
        if (ApplicationIndependent.stringCompare(expected,actual)==True):
            status="Pass"
    except Exception as e:
        ApplicationIndependent.writeLog("There is an error raised during the execution of the Method navigate,Exception :","error")
    ApplicationIndependent.writeLog("The navigate function has ended execution at :" + ApplicationIndependent.getDateTime(),"info")
    return status

# oBrowser=webdriver.Chrome()
# sleep(2)
# oBrowser.get("https://network-rctp.qa.gtnexus.com/")
# oBrowser.maximize_window()


def Username(self):
    status = "Fail"
    User_name=""
    ApplicationIndependent.writeLog(
        "The createUser function has started execution at :" + ApplicationIndependent.getDateTime(), "info")
    try:
        #self.oBrowser.find_element(By.XPATH, Locators.locators.user_name).clear()
        # user_name = oBrowser.find_element(By.XPATH, Locators.locators.user_name).send_keys(os.environ.get('Username', -1))
        User_name=self.oBrowser.find_element(By.XPATH, Locators.locators.user_name)
    except Exception as e:
        ApplicationIndependent.writeLog(
            "There is an error raised during the execution of the Method createUser,Exception :","error")
        ApplicationIndependent.writeLog(
            "The createUser function has ended execution at :" + ApplicationIndependent.getDateTime(), "info")
    return User_name



def password(self):
    status = "Fail"
    Pass_word=""
    ApplicationIndependent.writeLog(
        "The createUser function has started execution at :" + ApplicationIndependent.getDateTime(), "info")
    try:
        #self.oBrowser.find_element(By.XPATH, Locators.locators.pass_word).clear()
        Pass_word=self.oBrowser.find_element(By.XPATH, Locators.locators.pass_word)
    except Exception as e:
        ApplicationIndependent.writeLog("There is an error raised during the execution of the Method createUser,Exception :","error")
        ApplicationIndependent.writeLog(
            "The createUser function has ended execution at :" + ApplicationIndependent.getDateTime(), "info")
    return Pass_word


def login_button(self):
    status = "Fail"
    ApplicationIndependent.writeLog(
        "The createUser function has started execution at :" + ApplicationIndependent.getDateTime(), "info")
    try:
        self.oBrowser.find_element(By.XPATH, Locators.locators.login_button).click()
    except Exception as e:
        ApplicationIndependent.writeLog(
            "There is an error raised during the execution of the Method createUser,Exception :","error")
        ApplicationIndependent.writeLog(
            "The createUser function has ended execution at :" + ApplicationIndependent.getDateTime(), "info")


'''
Created By:
Created Date:
Reviewd By:
Modified By:
Parameters:
return Type:
Purpose:
'''
def closeApplication(self):
    status="Fail"
    ApplicationIndependent.writeLog("The closeApplication function has started execution at :" + ApplicationIndependent.getDateTime(),"info")
    try:
        self.oBrowser.close()
        status="Pass"
    except Exception as e:
        ApplicationIndependent.writeLog("There is an error raised during the execution of the Method closeApplication,Exception :","error")
    ApplicationIndependent.writeLog("The closeApplication function has started execution at :" + ApplicationIndependent.getDateTime(),"info")
    return status






# def login_properties():
#     status = "Fail"
#     ApplicationIndependent.writeLog(
#         "The createUser function has started execution at :" + ApplicationIndependent.getDateTime(), "info")
#     try:
#         user_name = oBrowser.find_element(By.XPATH, Locators.locators.user_name).clear()
#         #user_name = oBrowser.find_element(By.XPATH, Locators.locators.user_name).send_keys(os.environ.get('Username', -1))
#         user_name=oBrowser.find_element(By.XPATH, Locators.locators.user_name).send_keys("sp@gtnexus")
#         sleep(2)
#         pass_word=oBrowser.find_element(By.XPATH, Locators.locators.pass_word).clear()
#         pass_word = oBrowser.find_element(By.XPATH, Locators.locators.pass_word).send_keys("bfqFDIZWkv6st@")
#         #pass_word = oBrowser.find_element(By.XPATH, Locators.locators.pass_word).send_keys(os.environ.get('Password', -1))
#
#         sleep(2)
#         login_button=oBrowser.find_element(By.XPATH, Locators.locators.login_button).click()
#
#     except Exception as e:
#         ApplicationIndependent.writeLog(
#             "There is an error raised during the execution of the Method createUser,Exception :" + e)
#         ApplicationIndependent.writeLog(
#             "The createUser function has ended execution at :" + ApplicationIndependent.getDateTime(), "info")
#     #return status


