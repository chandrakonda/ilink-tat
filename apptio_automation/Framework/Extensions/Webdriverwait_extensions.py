from selenium.webdriver.support.ui import WebDriverWait
import selenium.common.exceptions as seleniumexceptions
from selenium.webdriver.support import expected_conditions as EC
from apptio_automation.Framework.Environment_setup import EnvironmentSetup as  Env_setup
from datetime import datetime
from selenium.webdriver.common.by import By
import apptio_automation.Framework.Extensions.Custom_logger as  cl
import logging

class WaitExtensions(Env_setup):
    (by, value) = (None, None)
    log = cl.customLogger(logging.DEBUG)
    # wait for element to visible
    def Wait_for_element_visible(self,by,waitTime_seconds):
        try:
            driver = self.get_driver()
            wait  = WebDriverWait(driver,int(waitTime_seconds))
            return wait.until(EC.visibility_of_element_located((eval(by[0]),by[1])))
        except Exception:
            self.log.exception("'{}' Element is not visible so returning False".format(by))
            return False
    # Wait for text present in the element
    def Wait_for_text_present(self,element_to_be_visible,text_value, waitTime_InMilliseconds):
        try:
            wait = WebDriverWait(self.get_driver(), waitTime_InMilliseconds)
            return wait.until(EC.text_to_be_present_in_element(element_to_be_visible,text_value))
        except seleniumexceptions.NoSuchElementException as e:
            self.log.exception("Exception thrown 'Wait_for_text_present' ".format(e))
            raise
        except seleniumexceptions.StaleElementReferenceException as e:
            self.log.exception("Exception thrown 'Wait_for_text_present' ".format(e))
            raise

    # Wait for title contains
    def Wait_for_title_contains(self,waitTime_InMilliseconds,page_title ):
        try:
            wait = WebDriverWait(self.get_driver(),waitTime_InMilliseconds)
            return wait.until(EC.title_contains(page_title))
        except seleniumexceptions.NoSuchElementException as e:
            self.log.exception("Exception thrown 'Wait_for_title_contains' ".format(e))
            raise
        except seleniumexceptions.WebDriverException as e:
            self.log.exception("Exception thrown 'Wait_for_title_contains' ".format(e))
            raise

    def Wait_for_title_is(self, waitTime_InMilliseconds, page_title):
        try:
            wait = WebDriverWait(self.get_driver(), waitTime_InMilliseconds)
            return wait.until(EC.title_is(page_title))
        except seleniumexceptions.NoSuchElementException as e:
            self.log.exception("Exception thrown 'Wait_for_title_is' ".format(e))
            raise
        except seleniumexceptions.WebDriverException as b:
            self.log.exception("Exception thrown 'Wait_for_title_is' ".format(b))
            raise

    # Wait for alert present
    def Wait_for_alert_present(self,waitTime_InMilliseconds ):
        try:
            wait = WebDriverWait(self.get_driver(),waitTime_InMilliseconds)
            return wait.until(EC.alert_is_present())
        except seleniumexceptions.TimeoutException as e:
            self.log.exception("Exception thrown 'Wait_for_alert_present' ".format(e))
            return False
        except seleniumexceptions.WebDriverException as b:
            self.log.exception("Exception thrown 'Wait_for_alert_present' ".format(b))
            return False

    def Wait_for_element(self,element,waitTime_InMilliseconds):
        try:
            driver = self.get_driver()
            wait  = WebDriverWait(driver,10)
            return wait.until(EC.visibility_of(element))
        except Exception as v:
            self.log.exception("Exception thrown 'Wait_for_alert_present' ".format(v))
            return False








