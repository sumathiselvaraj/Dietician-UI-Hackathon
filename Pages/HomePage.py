from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from Pages.Base import BasePage

class HomePage(BasePage):

  logo_xpath = "//img[@alt='logo']"
  product_xpath="//span[contains(text(),'product')]"
  about_xpath = "//span[contains(text(),'About')]"
  clients_xpath = "//span[contains(text(),'clients')]"
  team_xpath = "//span[contains(text(),'team')]"
  register_xpath = "//span[contains(text(),'register')]"
  featured_xpath = "//span[contains(text(),'featured')]"
  blog_xpath = "//span[contains(text(),'blog')]"
  contactus_xpath = "//span[contains(text(),'contactus')]"
  searchicon_className = "search"
  signin_className = "signin"

  "constructor"
  def __init__(self, driver):
        super()._init_(driver)

  def logo_displayed(self,by_locator):
        return self.is_visible(self.logo_xpath)

  def get_title(self,title):
      return self.get_title(title)

  def do_product_link_click(self,by_locator):
      self.do_click(self.product_xpath)

  def do_client_link_click(self,by_locator):
      self.do_click(self.clients_xpath)

  def do_team_click_link(self,by_locator):
      self.do_click(self,team_xpath)

  def do_blog_click_link(self,by_locator):
      self.do_click(self.blog_xpath)

  def do_about_click_link(self, by_locator):
    self.do_click(self.about_xpath)

  def do_featured_click_link(self, by_locator):
      self.do_click(self.featured_xpath)

  def do_register_click_link(self, by_locator):
      self.do_click(self.register_xpath)

  def do_contactus_click_link(self, by_locator):
      self.do_click(self.contactus_xpath)

  def do_check_searchicon_displayed(self,by_locator):
      return self.is_displayed(self.searchicon_className)

  def do_check_signin_displayed(self,by_locator):
      return self.is_displayed(self.signin_className)
