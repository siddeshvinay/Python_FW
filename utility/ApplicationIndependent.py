import logging
import datetime
from selenium.webdriver.common.by import By
'''
Created By:
Created Date:
Reviewd By:
Modified By:
Parameters:
return Type:
Purpose:
'''
def stringCompare(expected,actual):
    if(expected==actual):
        return True
    else:
        return False


'''
Created By:
Created Date:
Reviewd By:
Modified By:
Parameters:
return Type:
Purpose:
'''
def isElementPresent(self,locatorname,locatorvalue):
    try:
        if (locatorname=="XPATH"):
            self.oBrowser.find_element(By.XPATH,locatorvalue)
        elif(locatorname=="ID"):
            self.oBrowser.find_element(By.ID, locatorvalue)
        elif (locatorname == "LINKTEXT"):
            self.oBrowser.find_element(By.LINK_TEXT, locatorvalue)
        else:
            return False
    except Exception as e:
        return False
    return True


'''
Created By:
Created Date:
Reviewd By:
Modified By:
Parameters:
return Type:
Purpose:
'''
def isAlertPresent(self):
    try:
        self.oBrowser.switch_to.alert
        return True
    except Exception as e:
        return False


'''
Created By:
Created Date:
Reviewd By:
Modified By:
Parameters:
return Type:
Purpose:
'''
def writeLog(message,loglevel):
    if (loglevel.lower()=="info"):
        logging.basicConfig(filename='E:/PYTHON/Browser Drivers/Final_Automation_FW/Results/Logs/ActiTimeLog.log', level=logging.INFO)
        logging.info(message)
    elif (loglevel.lower()=="error"):
        logging.basicConfig(filename='E:/PYTHON/Browser Drivers/Final_Automation_FW/Results/Logs/ActiTimeLog.log', level=logging.ERROR)
        logging.error(message)
    elif (loglevel.lower()=="debug"):
        logging.basicConfig(filename='E:/PYTHON/Browser Drivers/Final_Automation_FW/Results/Logs/ActiTimeLog.log', level=logging.ERROR)
        logging.error(message)
    else:
        logging.error("Invalid Log Level !!!!!!!!!!!!")


'''
Created By:
Created Date:
Reviewd By:
Modified By:
Parameters:
return Type:
Purpose:
'''
def getDateTime():
    strDate=datetime.datetime.now()
    return str(strDate)



'''
Created By:
Created Date:
Reviewd By:
Modified By:
Parameters:
return Type:
Purpose:
'''
def captureScreenShot(self,filename):
    self.oBrowser.save_screenshot(filename)