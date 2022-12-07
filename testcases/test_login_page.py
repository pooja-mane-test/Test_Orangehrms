from config.config import Config
from pages.BaseTest import BaseTest
from pages.LoginPage import LoginPage
from utility.RunLogs import RunLogs

class TestLogin(BaseTest):

    log = RunLogs.start_logs()
    #scenario1: Testing login with valid username and valid password
    def test_valid_login(self):
        self.log.info("===================================Testcase start=========================================")
        self.login = LoginPage(self.driver)
        self.login.do_login(Config.USERNAME, Config.PASSWORD)
        self.login.do_logout()
        self.log.info("===================================Testcase end=========================================")

    #scenario2: Test invalid credentials
    def test_invalid_login(self):
        self.login = LoginPage(self.driver)
        self.login.do_login(Config.USERNAME, Config.INVALID_PASSWORD)
        self.login.verify_login_error(Config.ERROR_TEXT)

    #scenario3: Verify the login label
    def test_login_label(self):
        self.login = LoginPage(self.driver)
        self.login.verify_login_page_elements()

