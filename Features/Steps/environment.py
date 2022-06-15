import logging
from selenium import webdriver
import selenium
from webdriver_manager.chrome import ChromeDriverManager
from behave import *
from Utils.customLogger import LogGen
from Utils.readProperty import ReadConfig
import time

baseURL = ReadConfig.getURL()
mylogger = LogGen.loggen()

def before_all(context):
     print("Executing before all")

     context.driver = webdriver.Chrome(ChromeDriverManager().install())
     mylogger.info("************ Driver initialized***************")
     context.driver.get(baseURL)
     mylogger.info("************ Driver Launched***************")

def before_feature(context, feature):
     print("Before feature\n")
     # Create logger
     context.logger = logging.getLogger('automation_tests')
     context.logger.setLevel(logging.DEBUG)

def before_scenario(context, scenario):
    print("User data:", context.config.userdata)

def after_scenario(context, scenario):
    print("scenario status" + scenario.status)
    context.browser.quit()
