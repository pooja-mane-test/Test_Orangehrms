import pytest
from pages.BaseTest import BaseTest
from pages.PimPage import PimPage
from pages.LoginPage import LoginPage
from config.config import Config
from config.pimconfig import Pimconfig


class TestPim(BaseTest):

    @pytest.mark.sanity
    def test_add_employee(self):
        self.login = LoginPage(self.driver)
        self.pim = PimPage(self.driver)
        self.login.do_login(Config.USERNAME, Config.PASSWORD)
        self.pim.verify_add_employee()

    @pytest.mark.regression
    def test_search_employee(self):
        self.login = LoginPage(self.driver)
        self.pim = PimPage(self.driver)
        self.login.do_login(Config.USERNAME, Config.PASSWORD)
        self.pim.verify_add_employee()
        self.pim.search_employee(Pimconfig.FIRST_NAME)
