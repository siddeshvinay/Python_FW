from selenium import webdriver
from time import sleep
import os
from utility import ApplicationIndependent
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
        sleep(2)
        actual=self.oBrowser.title
        if (ApplicationIndependent.stringCompare(expected,actual)==True):
            status="Pass"
    except Exception as e:
        ApplicationIndependent.writeLog("There is an error raised during the execution of the Method navigate,Exception :"+e,"error")
    ApplicationIndependent.writeLog("The navigate function has ended execution at :" + ApplicationIndependent.getDateTime(),"info")
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
def closeApplication(self):
    status="Fail"
    ApplicationIndependent.writeLog("The closeApplication function has started execution at :" + ApplicationIndependent.getDateTime(),"info")
    try:
        self.oBrowser.close()
        status="Pass"
    except Exception as e:
        ApplicationIndependent.writeLog("There is an error raised during the execution of the Method closeApplication,Exception :" + e,"error")
    ApplicationIndependent.writeLog("The closeApplication function has started execution at :" + ApplicationIndependent.getDateTime(),"info")
    return status