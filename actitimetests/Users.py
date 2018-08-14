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
def createUser(self):
    status="Fail"
    ApplicationIndependent.writeLog("The createUser function has started execution at :" + ApplicationIndependent.getDateTime(), "info")
    try:
        self.oBrowser.find_element_by_xpath("//*[@id='topnav']/tbody/tr[1]/td[5]/a/div[2]").click()
        sleep(3)
        #self.oBrowser.find_element_by_id("gettingStartedShortcutsPanelId").click()
        #sleep(2)
        self.oBrowser.find_element_by_xpath("//div[text()='Add User']").click()
        sleep(2)
        self.oBrowser.find_element_by_name("firstName").send_keys(os.environ.get('FirstName', -1))
        sleep(1)
        self.oBrowser.find_element_by_name("lastName").send_keys(os.environ.get('LastName', -1))
        sleep(1)
        self.oBrowser.find_element_by_name("email").send_keys(os.environ.get('Email', -1))
        sleep(1)
        self.oBrowser.find_element_by_name("username").send_keys(os.environ.get('UserUsername', -1))
        sleep(1)
        self.oBrowser.find_element_by_name("password").send_keys(os.environ.get('UserPassword', -1))
        sleep(1)
        self.oBrowser.find_element_by_name("passwordCopy").send_keys(os.environ.get('UserRetypePassword', -1))
        sleep(1)
        self.oBrowser.find_element_by_xpath("//span[text()='Create User']").click()
        sleep(4)

        username = os.environ.get('LastName', -1) + ", " + os.environ.get('FirstName', -1)
        sleep(2)
        locatorname="XPATH"
        locatorvalue="//span[text()=\'" + username + "\']"
        if (ApplicationIndependent.isElementPresent(self,locatorname,locatorvalue)==True):
            status="Pass"
    except Exception as e:
        ApplicationIndependent.writeLog("There is an error raised during the execution of the Method createUser,Exception :" + e)
    ApplicationIndependent.writeLog("The createUser function has ended execution at :" + ApplicationIndependent.getDateTime(), "info")
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
def modifyUser(self):
    status="Fail"
    expected="actiTIME - User List"
    ApplicationIndependent.writeLog("The modifyUser function has started execution at :" + ApplicationIndependent.getDateTime(), "info")
    try:
        username = os.environ.get('LastName', -1) + ", " + os.environ.get('FirstName', -1)
        sleep(2)
        self.oBrowser.find_element_by_xpath("//span[text()=\'" + username + "\']").click()
        sleep(2)
        self.oBrowser.find_element_by_name("password").send_keys(os.environ.get('UserNewPassword', -1))
        sleep(2)
        self.oBrowser.find_element_by_name("passwordCopy").send_keys(os.environ.get('UserRetypeNewPassword', -1))
        sleep(3)
        self.oBrowser.find_element_by_xpath("//span[text()='Save Changes']").click()
        sleep(5)
        actual = self.oBrowser.title
        print(actual)
        if (ApplicationIndependent.stringCompare(expected, actual) == True):
            status = "Pass"
    except Exception as e:
        ApplicationIndependent.writeLog("There is an error raised during the execution of the Method modifyUser,Exception :" + e)
    ApplicationIndependent.writeLog("The modifyUser function has ended execution at :" + ApplicationIndependent.getDateTime(), "info")
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
def deleteUser(self):
    status="Fail"
    ApplicationIndependent.writeLog("The deleteUser function has started execution at :" + ApplicationIndependent.getDateTime(), "info")
    try:
        username = os.environ.get('LastName', -1) + ", " + os.environ.get('FirstName', -1)
        sleep(2)
        print(username)
        self.oBrowser.find_element_by_xpath("//span[text()=\'" + username + "\']").click()
        sleep(2)
        self.oBrowser.find_element_by_id("userDataLightBox_deleteBtn").click()
        sleep(2)
        if (ApplicationIndependent.isAlertPresent(self)==True):
            status="Pass"
        self.oBrowser.switch_to.alert.accept()
        sleep(2)
    except Exception as e:
        ApplicationIndependent.writeLog("There is an error raised during the execution of the Method deleteUser,Exception :" + e)
    ApplicationIndependent.writeLog("The deleteUser function has ended execution at :" + ApplicationIndependent.getDateTime(), "info")
    return status