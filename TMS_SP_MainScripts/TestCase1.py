from selenium import webdriver
from selenium.webdriver.common.by import By
from TMS_SP import Locators
from time import sleep
from utility import ApplicationIndependent
from TMS_ProjectSpecificScripts import Login_scripts


def Testcase():

    Login_scripts.login_properties()


Testcase()






