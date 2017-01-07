import os,traceback,pytest ,logging
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import selenium.common.exceptions as web_driver_exceptions
import apptio_automation.Framework.Extensions.Custom_logger as cl
from selenium import webdriver


class DriverSetup:
    # driver = None
    log = cl.customLogger(logging.DEBUG)

    def set_driver(self ,framework_path ,type_of_driver):
        driver = None
        print("Enter create_driver function for creating driver")
        driver_folder_path = os.path.normpath(os.path.join(framework_path, 'Drivers'))
        print("Driver folder path is '{}'".format(driver_folder_path))

        try:
            if type_of_driver.lower() == 'chrome':
                driver = webdriver.Chrome(os.path.normpath(os.path.join(driver_folder_path, "chromedriver.exe")))
                print("Creation of 'CHROME' driver is successful")
                self.log.info("Creation of 'CHROME' driver is successful")
            elif type_of_driver.lower() == 'firefox':
                firefox_capabilities = DesiredCapabilities.FIREFOX
                firefox_capabilities['marionette'] = True
                #firefox_capabilities['binary'] = 'C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe'
                driver = webdriver.Firefox(capabilities=firefox_capabilities)
                print("Creation of 'FIREFOX' driver is successful")
                self.log.info("Creation of 'FIREFOX' driver is successful")
            elif type_of_driver.lower() == 'edge':
                driver = webdriver.Edge(os.path.normpath(os.path.join(driver_folder_path, "MicrosoftWebDriver.exe")))
                print("Creation of 'EDGE' driver is successful")
                self.log.info("Creation of 'EDGE' driver is successful")
            elif type_of_driver.lower() == 'ie':
                driver = webdriver.Ie(os.path.normpath(os.path.join(driver_folder_path, "IEDriverServer.exe")),
                                      self.ie_options())
                print("Creation of 'IE' driver is successful")
                self.log.info("Creation of 'IE' driver is successful")
            elif type_of_driver.lower() == 'safari':
                # safari driver location : http://selenium-release.storage.googleapis.com/index.html?path=2.48/,
                # https://github.com/SeleniumHQ/selenium/wiki/SafariDriver#getting-started
                driver = webdriver.Safari()
                self.log.info("Creation of 'SAFARI' driver is successful")

            else:
                print(
                    "Given driver {} is not matching with chrome,ie,edge,firefox.Please provide valid value".format
                        (type_of_driver))
                self.log.warning("Given driver {} is not matching with chrome,ie,edge,firefox.Please provide valid value".format
                        (type_of_driver))
        except web_driver_exceptions.WebDriverException as e:
            traceback.print_exc()
            self.log.error("Creation of driver failed {}".format(e))
            pytest.fail("Creation of driver is failed")
        except Exception as ex:
            traceback.print_exc()  # print exception details
            self.log.error("Creation of driver failed {}".format(e))
            #self.log.err
            pytest.fail("Creation of driver is failed")
        return driver

    def ie_options(self):
        ie_options = DesiredCapabilities.INTERNETEXPLORER
        ie_options['ignoreProtectedModeSettings'] = True
        return ie_options

    # def chrome_options(self):
    #     chrome_options = Options()