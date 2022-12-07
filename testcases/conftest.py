from selenium import webdriver
import pytest


@pytest.fixture(scope='class',params=['chrome'])
def init_driver(request):
    web_driver = webdriver.Chrome(executable_path="C:/Users/poojama/PycharmProjects/TestProject1/src/drivers/chrome/chromedriver.exe")
    web_driver.maximize_window()
    web_driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    request.cls.driver = web_driver
    yield
    web_driver.close()
    web_driver.quit()

