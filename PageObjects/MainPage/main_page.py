"""This module is used for main page objects."""

import logging
from SupportLibraries.base_helpers import BaseHelpers
import FrameworkUtilities.logger_utility as log_utils

class MainPage(BaseHelpers):
    """This class defines the method and element identifications for main page."""

    log = log_utils.custom_logger(logging.INFO)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    number_firstpage = "//android.widget.TextView[@text='NUM 1']"
    number_secondpage = "//android.widget.TextView[@text='NUM 2']"
    start_scan_button = "//android.widget.Button[@text='START SCAN']"
    stop_scan_button = "//android.widget.Button[@text='STOP SCAN']"
    disconnect_button = "//android.widget.Button[@text='DISCONNECT']"
    connect_button = "//android.widget.Button[@text='CONNECT']"
    connected = "//android.widget.TextView[@text='Connected']"
    disconnected = "//android.widget.TextView[@text='Disconnected']"
    start_observing_button = "//android.widget.Button[@text='START OBSERVING']"
    test_cache = "//android.widget.Button[@text='TEST CACHE']"
    clear_cache = "//android.widget.Button[@text='CLEAR CACHE']"
    retrieve_new = "//android.widget.Button[@text='RETRIEVE NEW']"
    retrieve_all = "//android.widget.Button[@text='RETRIEVE ALL']"
    scanning = "//android.widget.TextView[@text='Scanning']"
    medical_device1 = "//android.widget.TextView=[@text='Contour7830H6086398 (54:6C:0E:CB:D5:E1)']"
    medical_device2 = "//android.widget.TextView[@text='meter+06647277 (10:CE:A9:3B:D7:57)']"
    bond_status1 = "//android.widget.TextView[@text='Bond Status: Not bonded']"
    bond_status2 = "//android.widget.TextView[@text='Bond Status: Bonded']"
    connection_status1 = "//android.widget.TextView=[@text='Connection Status: RxBleConnectionState{CONNECTING}']"
    connection_status2 = "//android.widget.TextView=[@text='Connection Status: RxBleConnectionState{DISCONNECTED}']"
    scroll_grey_screen = "//android.widget.ScrollView=[@text='']"
    pairing_request = "//android.widget.Button=[@text='OK']"

    @property
    def verify_main_screen_elements(self):
        """
        This function is used to verify all the elements present on the main screen
        :return: this function returns boolean status of element located
        """
        result = False
        _xpath_prop = "xpath"
        self.mouse_click_action_on_element_present(self.number_firstpage);
        self.mouse_click_action_on_element_present(self.number_secondpage);
        self.mouse_click_action_on_element_present(self.number_firstpage);
        self.mouse_click_action_on_element_present(self.start_scan_button)
        self.wait_for_element_to_be_clickable(self.start_scan_button);
        self.mouse_click_action_on_element_present(self.stop_scan_button)
        self.mouse_click_action_on_element_present(self.medical_device2);

        #self.wait_for_element_to_be_clickable(self.medical_device1);
        self.mouse_click_action_on_element_present(self.connect_button);
        #self.wait_for_element_to_be_clickable(self.pairing_request);
        self.mouse_click_action_on_element_present(self.pairing_request);

        #self.is_element_displayed(self.connected);
       # self.mouse_click_action_on_element_present(self.retrieve_new);
       # self.vertical_scroll(self.scroll_grey_screen)
        #self.mouse_click_action_on_element_present(self.disconnect_button);
        #self.is_element_displayed(self.disconnected);
        self.mouse_click_action_on_element_present(self.retrieve_new);
        self.device_back_button_click()



        if not result:
            self.log.error("Main screen element verification failed.")
        return result

