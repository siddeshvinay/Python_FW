from selenium import webdriver
from selenium.webdriver.common.by import By
from TMS_SP import Locators
from time import sleep
from utility import ApplicationIndependent
from TMS_ProjectSpecificScripts import Login_scripts
import os

def Testcase1(self):
    Login_scripts.LaunchBrowser(self)
    sleep(3)
    Login_scripts.navigate(self)
    sleep(3)
    Login_scripts.Username(self).send_keys(os.environ.get('Username', -1))
    #Login_scripts.Username(self).send_keys("sp@gtnexus")
    sleep(2)
    Login_scripts.password(self).send_keys(os.environ.get('Password', -1))
    #Login_scripts.password(self).send_keys("bfqFDIZWkv6st@")
    sleep(2)
    Login_scripts.login_button(self)









