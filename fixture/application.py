from selenium import webdriver

from fixture.project import ProjectHelper
from fixture.session import SessionHelper
from fixture.session import SessionHelper
from fixture.james import JamesHelper
from fixture.signup import SignupHelper
from fixture.mail import MailHelper
from fixture.soap import SoapHelper


import random, string

class Application:

    def __init__(self, browser, config):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.wd.implicitly_wait(5)
        self.session = SessionHelper(self)
        self.james = JamesHelper(self)
        self.signup = SignupHelper(self)
        self.mail = MailHelper(self)
        self.soap = SoapHelper(self)
        self.config = config
        self.project = ProjectHelper(self)
        self.baseurl = config['web']['baseUrl']
        self.user = config['web']['user']
        self.password = config['web']['password']

# method for fixture vitality validation
    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False


    def open_home_page(self):
        wd = self.wd
        wd.get(self.baseurl)

    @staticmethod
    def randomword(prefix, length):
        # letters = string.ascii_letters + string.digits + string.punctuation + " "*10
        # letters = string.ascii_letters + string.digits + " "*10
        letters = string.ascii_letters + string.digits + " "*10
        return prefix + ''.join([random.choice(letters) for i in range(random.randrange(length))])

    # def loop_is_text_present(self, text, max_attempts=3):
    #     attempt = 1
    #     while True:
    #         try:
    #             return self.is_text_present(text)
    #         except StaleElementReferenceException:
    #             if attempt == max_attempts:
    #                 raise
    #             attempt += 1
    #
    # def is_text_present(self, text):
    #     wd = self.wd
    #     element = wd.find_element_by_xpath("//*[contains(text(),'"+text+"')]")
    #     return element.text

    def destroy(self):
        self.wd.quit()