from selenium.webdriver.common.by import By


class LoginLocators:

    USERNAME = (By.XPATH, "//input[@name='username']")
    PASSWORD = (By.XPATH, "//input[@name='password']")
    LOGIN_BUTTON = (By.XPATH,"//button[@type='submit']")
    EMPLOYEENAME_DROPDOWN = (By.XPATH, "//span[@class='oxd-userdropdown-tab']")
    LOGOUT_BUTTON = (By.XPATH, "//a[text()='Logout']")
    ERROR_TEXT = (By.XPATH, "//div[@role='alert']//p")
    LOGIN_LABEL = (By.XPATH, '//div[@class="orangehrm-login-slot"]/h5')
    USERNAME_LABEL = (By.XPATH, '(//div[@class="oxd-form-row"])[1]//label')
    PASSWORD_LABEL = (By.XPATH, '(//label[@class="oxd-label"])[2]')
    FORGOT_PASSWORD_LABEL = (By.XPATH, '//div[@class="orangehrm-login-forgot"]/p')
    FOOTERLINK1 = (By.XPATH, '//div[@class="orangehrm-copyright-wrapper"]/p[1]')
    FOOTERLINK2 = (By.XPATH, '//div[@class="orangehrm-copyright-wrapper"]//p[2]' )
    ORANGEHRM_TITLE = (By.XPATH, '//img[@alt="company-branding"]')
    USERNAME_PLACEHOLDER = (By.XPATH, '//input[@name="username"]')
    PASSWORD_PLACEHOLDER = (By.XPATH, '//input[@name="password"]')
    REQUIRED_TEXT = (By.XPATH, '(//div[@class="oxd-form-row"]//span)[1]')
    RIGHTSIDE_LOGO = (By.XPATH, '//div[@class="orangehrm-login-logo"]/img')