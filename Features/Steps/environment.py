import logging
from selenium import webdriver
import selenium
from webdriver_manager.chrome import ChromeDriverManager
from behave import *
from Utils.customLogger import LogGen
from Utils.readProperty import ReadConfig
from Pages.HomePage import HomePage
from Pages.Base import BasePage
import time

baseURL = ReadConfig.getURL()
mylogger = LogGen.loggen()

class enivronment(BasePage):


    def before_all(self):
     print("Executing before all")

     self.driver = webdriver.Chrome(ChromeDriverManager().install())
     mylogger.info("************ Driver initialized***************")
     self.driver.get(baseURL)
     mylogger.info("************ Driver Launched***************")

    def before_feature(self, feature):
         print("Before feature\n")
     # Create logger
         self.logger = logging.getLogger('automation_tests')
         self.logger.setLevel(logging.DEBUG)

    def before_scenario(self, scenario):
         print("User data:", self.config.userdata)

    def after_scenario(self, scenario):
        print("scenario status" + scenario.status)
        self.browser.quit()
