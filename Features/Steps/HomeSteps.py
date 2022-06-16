from behave import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from Utils.customLogger import LogGen
from Utils.readProperty import ReadConfig
from Pages.HomePage import HomePage
from Pages.Base import BasePage
from TestData.TestData import TestData
from parse_type import TypeBuilder
import time

baseURL=ReadConfig.getURL()
mylogger=LogGen.loggen()


class HomeSteps(BasePage):

    def __init__(self, driver):
        super()._init_(driver)

    @given(u'User is on Dietician Website')
    def step_impl(self):
        self.driver=webdriver.Chrome(ChromeDriverManager().install())
        mylogger.info("************ Driver initialized***************")
        self.driver.get(baseURL)
        mylogger.info("************ Driver Launched***************")

    @when(u'User is on Home page')
    def step_impl(self):
        mylogger.info("********* Dietician home Page********")

    @then(u'User should see the title of the page as details in excel HomePage and RowNUmber 0')
    def step_impl(self):
        title=self.homePage.get_title(TestData.expected_Title)
        assert title == TestData.expected_Title

    @then(u'User should see a logo with the company name on the Home Page')
    def step_impl(self):
        flag=self.homePage.logo_displayed()
        assert flag

    @when(u'User clicks on PRODUCT Link on  Home Page')
    def step_impl(self):
        self.homePage.do_product_link_click()

    @then(u'User should see the title of the page as details in excel HomePage and RowNUmber 1')
    def step_impl(self):
        actual_title=self.homePage.get_title()
        expected="product"
        assert actual_title == expected

    @when(u'User clicks on client Link on  Home Page')
    def step_impl(self):
        self.homePage.do_client_link_click()

    @then(u'User should see the title of the page as details in excel HomePage and RowNUmber 2')
    def step_impl(self):
        actual_title=self.homePage.get_title()
        expected="client"
        assert actual_title == expected

    @when(u'User clicks on Team Link on  Home Page')
    def step_impl(self):
        self.homePage.do_team_click_link()

    @then(u'User should see the title of the page as details in excel HomePage and RowNUmber 3')
    def step_impl(self):
        actual_title=self.homePage.get_title()
        expected="team"
        assert actual_title == expected

    @when(u'User clicks on Register Link on  Home Page')
    def step_impl(self):
        self.homePage.do_register_click_link()

    @then(u'User should see the title of the page as details in excel HomePage and RowNUmber 4')
    def step_impl(self):
        actual_title=self.homePage.get_title()
        expected="Register"
        assert actual_title == expected

    @when(u'User clicks on About Link on  Home Page')
    def step_impl(self):
        self.homePage.do_about_click_link()

    @then(u'User should see the title of the page as details in excel HomePage and RowNUmber 5')
    def step_impl(self):
        actual_title=self.homePage.get_title()
        expected="About"
        assert actual_title == expected

    @when(u'User clicks on Featured Link on  Home Page')
    def step_impl(self):
        self.homePage.do_featured_click_link()

    @then(u'User should see the title of the page as details in excel HomePage and RowNUmber 6')
    def step_impl(context):
        actual_title=self.homePage.get_title()
        expected="Featured content"
        assert actual_title == expected

    @when(u'User clicks on Blog Link on  Home Page')
    def step_impl(self):
        self.homePage.do_blog_click_link()


@then(u'User should see the title of the page as details in excel HomePage and RowNUmber 7')
def step_impl(self):
    actual_title=self.homePage.get_title()
    expected="blog"
    assert actual_title == expected


@when(u'User clicks on Contact Link on Home Page')
def step_impl(self):
    self.homePage.do_contactus_click_link()


@then(u'User should see the title of the page as details in excel HomePage and RowNUmber 8')
def step_impl(self):
    actual_title=self.homePage.get_title()
    expected="contact Us"
    assert actual_title == expected
