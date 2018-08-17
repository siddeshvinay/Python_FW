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
def createCustomer(self):
    status='Fail'
    ApplicationIndependent.writeLog("The Create Customer execution is started:" + ApplicationIndependent.getDateTime(), "info")
    try:
        self.oBrowser.find_element_by_xpath("//*[@id='topnav']/tbody/tr[1]/td[3]/a").click()
        sleep(2)
        self.oBrowser.find_element_by_xpath("//*[@id='cpTreeBlock']/div[2]/div[1]/div[2]/div").click()
        sleep(3)
        self.oBrowser.find_element_by_xpath("/html/body/div[12]/div[1]").click()
        sleep(2)
        self.oBrowser.find_element_by_xpath("//*[@id='customerLightBox_nameField']").send_keys(os.environ.get('NewCustomer', -1))
        sleep(2)
        self.oBrowser.find_element_by_xpath("//*[@id='customerLightBox_descriptionField']").send_keys(os.environ.get('CustomerDiscrption', -1))
        sleep(2)
        self.oBrowser.find_element_by_xpath("//div[@id='customerLightBox_commitBtn']/div/span[text()= 'Create Customer']").click()
        sleep(3)
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
def modifyCustomer(self):
    status='Fail'
    ApplicationIndependent.writeLog("The Created Customer is to be modified:" + ApplicationIndependent.getDateTime(), "info")
    try:
        self.oBrowser.find_element_by_xpath("//table[@class='containerTable']/tbody/tr/td/div/input[@placeholder='Start typing name ...']").send_keys(os.environ.get('NewCustomer', -1))
        sleep(2)
        self.oBrowser.find_element_by_xpath("//div[@class='node customerNode selected']/div[4][@class='editButton available']").click()
        sleep(3)
        self.oBrowser.find_element_by_xpath("//div[@class='statusButton']/div/div[@class='active']").click()
        sleep(3)
        self.oBrowser.find_element_by_xpath("//div[@class='dropdownContainer customerStatusMenu active']/div[@class='item archivedContainer']/div").click()
        sleep(3)
    except Exception as e:
        ApplicationIndependent.writeLog("There is an error raised during the execution of the Method createUser,Exception :" + e)
    ApplicationIndependent.writeLog("The modifyCustomer function has ended execution at :" + ApplicationIndependent.getDateTime(), "info")
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
def deleteCustomer(self):
    status='Fail'
    ApplicationIndependent.writeLog("To Delete the customer if it is archived" + ApplicationIndependent.getDateTime() +"info")
    try:
        self.oBrowser.find_element_by_xpath("//table[@class='containerTable']/tbody/tr/td/div/input[@placeholder='Start typing name ...']").send_keys(os.environ.get('NewCustomer', -1))
        sleep(2)
        isarchived=self.oBrowser.find_element_by_xpath("//*[@id='cpTreeBlock']/div[2]/div[2]/div/div[3]/div/div[1]/div[2]/div[2]/div/span[@class='archived']").get_attribute()
        if isarchived=='archived':
            # then customer should delete
            self.oBrowser.find_element_by_xpath("//*[@id='cpTreeBlock']/div[2]/div[2]/div/div[3]/div/div[1]/div[2]/div[2]/div[4]").clcick()
            sleep(3)
            self.oBrowser.find_element_by_xpath("//div[@class='actions']/div/div[@class='actionButton']").click()
            sleep(2)
            self.oBrowser.find_element_by_xpath("//div[@class='deleteButton']/div[text()='Delete']").click()
            sleep(2)
            self.oBrowser.find_element_by_xpath("//span[@id='customerPanel_deleteConfirm_submitTitle']").click()
            sleep(3)
        else:
            ApplicationIndependent.writeLog("The customer is not archived, hence could not delete" + ApplicationIndependent.getDateTime() + "info")
    except Exception as e:
        ApplicationIndependent.writeLog(
            "There is an error raised during the execution of the Method Delete Customer,Exception :" + e)
    ApplicationIndependent.writeLog("The DeleteCustomer function has ended execution at :" + ApplicationIndependent.getDateTime(), "info")
    return status

