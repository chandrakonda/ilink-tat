from  apptio_automation.Framework.extensions.Webdriverwait_extensions import WaitExtensions
from  apptio_automation.Framework.Environment_setup import EnvironmentSetup
import selenium.common.exceptions as exception
from selenium.webdriver.common.alert import  Alert

import logging
import apptio_automation.Framework.Extensions.Custom_logger as  cl

class AlertWindow(EnvironmentSetup):
    log = cl.customLogger(logging.DEBUG)
    def is_alert_present(self,time_to_wait):  
        try:
            wait_ext = WaitExtensions()
            if wait_ext.Wait_for_alert_present(time_to_wait):
                EnvironmentSetup.get_driver().switch_to_alert()
                self.log.info("Switch to Alert is executed, so returning 'True' value")
                return True
        except exception.NoAlertPresentException:
            self.log.warning("Given alert is not present, so returning 'False' value")
            return False
    def get_text_in_alert(self):
        var_text = Alert(EnvironmentSetup.get_driver()).text
        self.log.info("Text from the Alert is '{}'".format(var_text))
        return var_text
    def accept_alert(self):
        Alert(EnvironmentSetup.get_driver()).accept()

    def dismiss_alert(self):
        Alert(EnvironmentSetup.get_driver()).dismiss()
