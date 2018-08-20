from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import *
from time import *


class locators():
    # Loign page locators (eg: XPATHS, NAME, ID, LINKS etc.
    user_name = "//*[@id='login']"
    pass_word = "//*[@id='password']"
    login_button = "//input[@id='loginButton']"

    # Switch to GTN page
    SP_Team = "//a[@id='navmenu__user']"
    switch_to_GTN = "//a[@id='navmenu__switch to gtn nh']"

    # Shadow loin
    shadow_login = "//input[@id='loginAsField-input']"
    shadow_button = "//*[@id='gtn_auto_19']/tbody/tr[2]/td[2]/em/button"

    # customer selection
    customer_dropdown = "//input[@id='customerSelector-input']"
    select_customer = "//div/div[@role='listitem'][1]"















