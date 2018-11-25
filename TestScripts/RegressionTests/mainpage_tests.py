""" This module contains the all test cases."""
import logging
import unittest
import pytest
import allure
import sys
import string
import random
import FrameworkUtilities.logger_utility as log_utils
from PageObjects.MainPage.main_page import MainPage
from FrameworkUtilities.execution_status_utility import ExecutionStatus
from FrameworkUtilities.data_reader_utility import DataReader
from FrameworkUtilities.config_utility import ConfigUtility


@allure.story('[Conversation] - Automate  the  Signin  screen across all three apps')
@allure.feature('Web App SigninPage Tests')
@pytest.mark.usefixtures("get_driver")
class MainTest(unittest.TestCase):
    """
    This class contains the executable test cases.
    """

    data_reader = DataReader()
    config = ConfigUtility()
    log = log_utils.custom_logger(logging.INFO)

    def setUp(self):
        self.main_page = MainPage(self.driver)
        self.exe_status = ExecutionStatus(self.driver)
        self.prop = self.config.load_properties_file()

   # def tearDown(self):
      #  self.login_page.logout_from_app()


    def string_generator(self, string_size=8, chars=string.ascii_uppercase + string.digits):
        """
        This function is used to generate random string
        :return: it returns random string
        """
        return ''.join(random.choice(chars) for _ in range(string_size))

    @pytest.fixture(autouse=True)
    def class_level_setup(self, request):
        """
        This method is used for one time setup of test execution process.
        :return: it returns nothing
        """

        if self.data_reader.get_data(request.function.__name__, "Runmode") != "Y":
            pytest.skip("Excluded from current execution run.")

    @allure.testcase("Validate MainPage Elements")
    def test_validate_mainpage_elements(self):
        """
         This test is validating the successful login. (positive scenario)
        :return: return test status
        """
        test_name = sys._getframe().f_code.co_name

        self.log.info("###### TEST EXECUTION STARTED :: " + test_name + " ######")
        self.main_page.verify_main_screen_elements()


        # with allure.step("MainPage App"):
        #      self.login_page.login(self.data_reader.get_data(test_name, "Username"),
        #                           self.data_reader.get_data(test_name, "Password"))
        #
        #  with allure.step("Verify LoginPage Successful"):
        #     result = self.login_page.verify_login_successful()
        #      self.exe_status.mark_final(test_step="Verify LoginPage Successful", result=result)

        def test_pairing(self):
            """
             This test is validating the successful login. (positive scenario)
            :return: return test status
            """
            test_name = sys._getframe().f_code.co_name

            self.log.info("###### TEST EXECUTION STARTED :: " + test_name + " ######")
            self.main_page.verify_main_screen_elements()

            # with allure.step("MainPage App"):
            #      self.login_page.login(self.data_reader.get_data(test_name, "Username"),
            #                           self.data_reader.get_data(test_name, "Password"))
            #
            #  with allure.step("Verify LoginPage Successful"):
            #     result = self.login_page.verify_login_successful()
            #      self.exe_status.mark_final(test_step="Verify LoginPage Successful", result=result)

    if __name__ == '__main__':
        unittest.main(verbosity=2)
