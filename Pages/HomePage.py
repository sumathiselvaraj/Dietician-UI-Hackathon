from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class HomePage:
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


  def __init__(self, driver):
        self.driver = driver

  def clickonLogin(self):
        self.driver.find_element_by_xpath(self.logo_xpath).is_displayed()

