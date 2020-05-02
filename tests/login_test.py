import time

import allure
import moment
import pytest

from pages.homepage import Homepage
from pages.loginpage import Loginpage
from utils import utils as utils


@pytest.mark.usefixtures("test_setup")
class TestLogin():

    def test_login(self):
        driver = self.driver
        driver.get(utils.URL)
        login = Loginpage(driver)
        login.enter_username(utils.Username)
        login.enter_password(utils.Password)
        login.click_Login()
        time.sleep(5)

    def test_logout(self):
        try:
            driver = self.driver
            homepage = Homepage(driver)
            homepage.click_welcome()
            homepage.click_Logout()
            x = driver.title
            assert x == "ORANGEeHRM"

        except AssertionError as error:
            print("Assertion error occurred")
            print(error)
            currTime = moment.now().strftime("%d-%m-%Y_%H-%M-%S")
            testName = utils.whoami()
            screenshotName= testName+"_"+currTime
            allure.attach(self.driver.get_screenshot_as_png(),name=screenshotName,
                          attachment_type=allure.attachment_type.PNG)
            driver.get_screenshot_as_file("C:/Users/manikandan/PycharmProjects/AutomationFramework_1/screenshots/"
                                          + screenshotName+".png")

            raise

        except:
            print("There was an exception")
            currTime = moment.now().strftime("%d-%m-%Y_%H-%M-%S")
            testName = utils.whoami()
            screenshotName = testName + "_" + currTime
            allure.attach(self.driver.get_screenshot_as_png(), name=screenshotName,
                          attachment_type=allure.attachment_type.PNG)
            driver.get_screenshot_as_file("C:/Users/manikandan/PycharmProjects/AutomationFramework_1/screenshots/"
                                          + screenshotName + ".png")

            raise

        else:
            print("No exceptions occurred")



        finally:
            print("This block will always execute and Close DB")
