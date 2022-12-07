import time
from pages.BaseElement import BaseElement
from locators.PimLocators import PimLocators
from config.pimconfig import Pimconfig
from selenium.common.exceptions import NoSuchElementException


class PimPage(BaseElement):

    def __init__(self, driver):
        super().__init__(driver)

    def verify_add_employee(self):
        self.click_element(PimLocators.PIM_LABEL)
        self.click_element(PimLocators.ADD_EMPLOYEE_LABEL)
        time.sleep(1)
        self.send_keys_to_element(PimLocators.ADD_EMPLOYEE_FIRST_NAME, Pimconfig.FIRST_NAME)
        self.send_keys_to_element(PimLocators.ADD_EMPLOYEE_MIDDLE_NAME, Pimconfig.MIDDLE_NAME)
        self.send_keys_to_element(PimLocators.ADD_EMPLOYEE_LAST_NAME, Pimconfig.LAST_NAME)
        self.click_element(PimLocators.ADD_EMPLOYEE_SAVE_BUTTON)
        time.sleep(1)
        get_success_label1 = self.get_text_from_element(PimLocators.SUCCESS_TEXT1)
        assert get_success_label1 == Pimconfig.SUCCESS_LABEL_TEXT, 'actual and expected doesnot match.actual was{a} and expected was {e}'.format(a=get_success_label1, e=Pimconfig.SUCCESS_LABEL_TEXT)
        self.wait_until_page_load(PimLocators.WAIT_UNTIL_PAGE_LOAD)
        time.sleep(1)
        self.send_keys_to_element(PimLocators.ADD_EMPLOYEE_NICK_NAME, Pimconfig.NICK_NAME)
        self.send_keys_to_element(PimLocators.ADD_EMPLOYEE_OTHER_ID, Pimconfig.OTHER_ID)
        self.send_keys_to_element(PimLocators.ADD_EMPLOYEE_DRIVERS_LICENSE_NUMBER, Pimconfig.LICENCE_NUMBER)
        self.send_keys_to_element(PimLocators.ADD_EMPLOYEE_LICENSE_EXP_DATE, Pimconfig.LICENCE_EXP_DATE)
        self.send_keys_to_element(PimLocators.ADD_EMPLOYEE_SSN_NUMBER, Pimconfig.SSN_NUMBER)
        self.send_keys_to_element(PimLocators.ADD_EMPLOYEE_SIN_NUMBER, Pimconfig.SIN_NUMBER)
        self.hover_to_element(PimLocators.HOVER_ON_NATIONALITY_DROPDOWN_TEXT)
        self.click_element(PimLocators.ADD_EMPLOYEE_NATIONALITY_DROPDOWN)
        self.click_element(PimLocators.ADD_EMPLOYEE_SELECT_NATIONALITY)
        self.click_element(PimLocators.ADD_EMPLOYEE_MARITAL_STATUS_DROPDOWN)
        self.click_element(PimLocators.ADD_EMPLOYEE_SELECT_MARRIED)
        self.send_keys_to_element(PimLocators.ADD_EMPLOYEE_DOB, Pimconfig.DOB)
        self.click_element(PimLocators.ADD_EMPLOYEE_GENDER)
        self.send_keys_to_element(PimLocators.ADD_EMPLOYEE_MILITARY_SERVICE, Pimconfig.MILITARY_SERVICE)
        self.click_element(PimLocators.ADD_EMPLOYEE_SMOKER)
        self.click_element(PimLocators.ADD_EMPLOYEE_SAVE1)
        self.click_element(PimLocators.ADD_EMPLOYEE_BLOOD_TYPE_DROPDOWN)
        self.click_element(PimLocators.ADD_EMPLOYEE_SELECT_BLOOD_TYPE)
        self.click_element(PimLocators.ADD_EMPLOYEE_SAVE2)
        self.click_element(PimLocators.ADD_ATTACHMENT_BUTTON)
        #self.hover_to_element(PimLocators.HOVER_ON_BROWSE_BUTTON)
        #self.send_keys_to_element(PimLocators.BROWSE_BUTTON, Pimconfig.ADD_ATTACHMENT_IMAGE)
        self.send_keys_to_element(PimLocators.ADD_COMMENT_TEXTAREA, Pimconfig.ADD_COMMENT_AREA)
        self.click_element(PimLocators.ADD_EMPLOYEE_SAVE3)

    def search_employee(self, empname):
        self.click_element(PimLocators.PIM_LABEL)
        self.click_element(PimLocators.EMPLOYEE_LIST)
        for i in range(1,100):
            get_text = self.get_text_from_element(PimLocators.GET_TEXT_FROM_TABLE)
            if(empname in get_text):
                assert True
                break
            else:
                try:
                    self.click_element(PimLocators.PAGINATION_RIGHT_ARROW)
                    time.sleep(2)
                except:
                    raise AssertionError("empname not found")
            continue








