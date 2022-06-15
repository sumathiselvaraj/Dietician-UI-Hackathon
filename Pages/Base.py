"""This class is the parent of all pages """


def __init__(self, driver):
    self.driver=driver

def do_click(self,by_locator):
    WebDriverWait(self.driver,10).until(EC.Visibility_of_element_locator(by_locator)).click()

