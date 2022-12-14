from selenium.webdriver.common.by import By


class PimLocators:

    PIM_LABEL = (By.XPATH, '//div[@class="oxd-sidepanel-body"]/ul/li[2]/a')
    ADD_EMPLOYEE_LABEL = (By.XPATH, '//header[@class="oxd-topbar"]/div[2]/nav/ul/li[3]/a')
    ADD_EMPLOYEE_FIRST_NAME = (By.XPATH, '//input[@name="firstName"]')
    ADD_EMPLOYEE_MIDDLE_NAME = (By.XPATH, '//input[@name="middleName"]')
    ADD_EMPLOYEE_LAST_NAME = (By.XPATH, '//input[@name="lastName"]')
    ADD_EMPLOYEE_SAVE_BUTTON = (By.XPATH, '//button[@type="submit"]')
    WAIT_UNTIL_PAGE_LOAD = (By.XPATH, '//div[@class="oxd-loading-spinner"]')
    SUCCESS_TEXT1 = (By.XPATH, '//p[text() = "Success"]')
    ADD_EMPLOYEE_NICK_NAME = (By.XPATH, '//label[text() = "Nickname"]/parent::div/parent::div//input')
    ADD_EMPLOYEE_OTHER_ID = (By.XPATH, '//label[text() = "Other Id"]/parent::div/parent::div//input')
    ADD_EMPLOYEE_DRIVERS_LICENSE_NUMBER = (By.XPATH, '//label[text()="Driver\'s License Number"]/parent::div/parent::div//input')
    ADD_EMPLOYEE_LICENSE_EXP_DATE = (By.XPATH, '//label[text()="License Expiry Date"]/parent::div/parent::div//input')
    ADD_EMPLOYEE_SELECT_LICENCE_EXP_DATE = (By.XPATH, '(//div[@class="oxd-date-wrapper"])[1]')
    ADD_EMPLOYEE_SSN_NUMBER = (By.XPATH, '//label[text() = "SSN Number"]/parent::div/parent::div//input')
    ADD_EMPLOYEE_SIN_NUMBER = (By.XPATH, '//label[text() = "SIN Number"]/parent::div/parent::div//input')
    HOVER_ON_NATIONALITY_DROPDOWN_TEXT = (By.XPATH, '//label[text()="Nationality"]')
    ADD_EMPLOYEE_NATIONALITY_DROPDOWN = (By.XPATH, '//label[text()="Nationality"]/parent::div/parent::div/div[2]/div/div/div[1]')
    ADD_EMPLOYEE_SELECT_NATIONALITY = (By.XPATH, '//span[text() = "Albanian"]')
    ADD_EMPLOYEE_MARITAL_STATUS_DROPDOWN = (By.XPATH, '//label[text()="Marital Status"]/parent::div/parent::div')
    ADD_EMPLOYEE_SELECT_MARRIED = (By.XPATH, '//span[text()="Married"]')
    ADD_EMPLOYEE_DOB = (By.XPATH, '//label[text()="Date of Birth"]/parent::div/parent::div//input')
 #  ADD_EMPLOYEE_SELECT_DOB = (By.XPATH, '(//div[@class="oxd-date-input"])[2]/input')
    ADD_EMPLOYEE_GENDER = (By.XPATH, '(//div[@class="oxd-radio-wrapper"]//label/span)[2]')
    ADD_EMPLOYEE_MILITARY_SERVICE = (By.XPATH, '//label[text()="Military Service"]/parent::div/parent::div//input')
    ADD_EMPLOYEE_SMOKER = (By.XPATH, '//label[text()="Yes"]')
    ADD_EMPLOYEE_SAVE1 = (By.XPATH, '(//button[@type="submit"])[1]')
    ADD_EMPLOYEE_BLOOD_TYPE_DROPDOWN = (By.XPATH, '(//div[@class="oxd-select-wrapper"])[3]')
    ADD_EMPLOYEE_SELECT_BLOOD_TYPE = (By.XPATH, '//span[text()="O+"]')
    ADD_EMPLOYEE_SAVE2 = (By.XPATH, '(//button[@type="submit"])[2]')
    ADD_ATTACHMENT_BUTTON = (By.XPATH, '//div[@class="orangehrm-action-header"]//button')
    #HOVER_ON_BROWSE_BUTTON = (By.XPATH, '//div[text()="Browse"]')
    BROWSE_BUTTON = (By.XPATH, '//div[text()="Browse"]')
    ADD_COMMENT_TEXTAREA = (By.XPATH, '//textarea[@placeholder="Type comment here"]')
    ADD_EMPLOYEE_SAVE3 = (By.XPATH, '(//button[@type="submit"])[3]')
    EMPLOYEE_LIST = (By.XPATH, '(//a[@class="oxd-topbar-body-nav-tab-item"])[1]')
    GET_TEXT_FROM_TABLE = (By.XPATH, '//div[@class="oxd-table-body"]')
    PAGINATION_RIGHT_ARROW = (By.XPATH, '//i[@class="oxd-icon bi-chevron-right"]')

