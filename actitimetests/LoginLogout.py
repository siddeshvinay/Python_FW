from selenium import webdriver
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
def login(self):
    status="Fail"
    ApplicationIndependent.writeLog("The login function has started execution at :" + ApplicationIndependent.getDateTime(),"info")
    try:
        self.oBrowser.find_element_by_id("username").send_keys(os.environ.get('Username', -1))
        self.oBrowser.find_element_by_name("pwd").send_keys(os.environ.get('Password', -1))
        self.oBrowser.find_element_by_xpath("//*[@id='loginButton']/div").click()
        sleep(4)
        locatorname="XPATH"
        locatorvalue="//td[text()='Enter Time-Track']"
        if (ApplicationIndependent.isElementPresent(self,locatorname,locatorvalue)==True):
            status="Pass"
    except Exception as e:
        ApplicationIndependent.writeLog("There is an error raised during the execution of the Method login,Exception :" + e,"error")
    ApplicationIndependent.writeLog("The login function has ended execution at :" + ApplicationIndependent.getDateTime(),"info")
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
def logout(self):
    status="Fail"
    expected = "actiTIME - Login"
    try:
        ApplicationIndependent.writeLog("The logout function has started execution at :" + ApplicationIndependent.getDateTime(),"info")
        self.oBrowser.find_element_by_link_text("Logout").click()
        sleep(4)
        actual = self.oBrowser.title
        if (ApplicationIndependent.stringCompare(expected, actual) == True):
            status = "Pass"
    except Exception as e:
        ApplicationIndependent.writeLog("There is an error raised during the execution of the Method logout,Exception :" + e,"error")
    ApplicationIndependent.writeLog("The logout function has ended execution at :" + ApplicationIndependent.getDateTime(),"info")
    return status