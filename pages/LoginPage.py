from pages.BaseElement import BaseElement
from locators.LoginLocators import LoginLocators
from config.config import Config

class LoginPage(BaseElement):

    def __init__(self,driver):
        super().__init__(driver)

    def do_login(self, username, password):
        self.send_keys_to_element(LoginLocators.USERNAME, username)
        self.send_keys_to_element(LoginLocators.PASSWORD, password)
        self.click_element(LoginLocators.LOGIN_BUTTON)

    def verify_login_error(self, error_text):
        get_error_text = self.get_text_from_element(LoginLocators.ERROR_TEXT)
        assert get_error_text == error_text

    def do_logout(self):
        self.click_element(LoginLocators.EMPLOYEENAME_DROPDOWN)
        self.click_element(LoginLocators.LOGOUT_BUTTON)

    def verify_login_page_elements(self):
        get_login_label = self.get_text_from_element(LoginLocators.LOGIN_LABEL)
        assert get_login_label == Config.LOGIN_LABEL_TEXT, 'actual and expected doesnot match.actual was {a} and expected was {e}'.format(a=get_login_label, e = Config.LOGIN_LABEL_TEXT)
        get_username_label = self.get_text_from_element(LoginLocators.USERNAME_LABEL)
        assert get_username_label == Config.USERNAME_LABEL_TEXT, 'actual and expected doesnot match.actual was {a} and expected was {e}'.format(a=get_username_label, e = Config.USERNAME_LABEL_TEXT)
        get_password_label = self.get_text_from_element(LoginLocators.PASSWORD_LABEL)
        assert get_password_label == Config.PASSWORD_LABEL_TEXT, 'actual and expected doesnot match.actual was {a} and expected was {e}'.format(a=get_password_label, e = Config.PASSWORD_LABEL_TEXT)
        forget_Password_text = self.get_text_from_element(LoginLocators.FORGOT_PASSWORD_LABEL)
        assert forget_Password_text == Config.FORGET_PASSWORD_LABEL, 'actual and expected doesnot match.actual was {a} and expected was {e}'.format(a=forget_Password_text, e = Config.FORGET_PASSWORD_LABEL)
        footer_text1_label = self.get_text_from_element(LoginLocators.FOOTERLINK1)
        assert footer_text1_label == Config.FOOTER_TEXT1_LABEL, 'actual and expected doesnot match.actual was {a} and expected was {e}'.format(a=footer_text1_label, e = Config.FOOTER_TEXT1_LABEL)
        footer_text2_label = self.get_text_from_element(LoginLocators.FOOTERLINK2)
        assert footer_text2_label == Config.FOOTER_TEXT2_LABEL, 'actual and expected doesnot match.actual was {a} and expected was {e}'.format(a=footer_text2_label, e = Config.FOOTER_TEXT2_LABEL)
        get_attribute_name = self.get_attribute_from_element(LoginLocators.ORANGEHRM_TITLE, Config.ATTRIBUTE_NAME)
        assert Config.ORANGE_HRM_LOGO in get_attribute_name, 'actual and expected doesnot match.actual was {a} and expected was {e}'.format(a=get_attribute_name, e = Config.ORANGE_HRM_LOGO)
        get_attribute_name = self.get_attribute_from_element(LoginLocators.USERNAME_PLACEHOLDER, Config.USER_ATTRIBUTE_NAME)
        assert get_attribute_name == Config.USER_ATTRIBUTE_VALUE, 'actual and expected doesnot match.actual was {a} and expected was {e}'.format(a=get_attribute_name, e=Config.USER_ATTRIBUTE_VALUE)
        get_attribute_name = self.get_attribute_from_element(LoginLocators.PASSWORD_PLACEHOLDER, Config.PASS_ATTRIBUTE_NAME)
        assert get_attribute_name == Config.PASS_ATTRIBUTE_VALUE, 'actual and expected doesnot match.actual was {a} and expected was {e}'.format(a=get_attribute_name, e = Config.PASS_ATTRIBUTE_VALUE)
        self.click_element(LoginLocators.LOGIN_BUTTON)
        get_required_text = self.get_text_from_element(LoginLocators.REQUIRED_TEXT)
        assert get_required_text == Config.REQUIRED_TEXT, 'actual and expected doesnot match.actual was {a} and expected was {e}'.format(a=get_required_text, e = Config.REQUIRED_TEXT)
        get_attribute_name = self.get_attribute_from_element(LoginLocators.RIGHTSIDE_LOGO, Config.ATTRIBUTE_NAME)
        assert Config.HR_FOR_ALL in get_attribute_name, 'actual and expected doesnot match.actual was {a} and expected was {e}'.format(a=get_attribute_name, e = Config.HR_FOR_ALL)





