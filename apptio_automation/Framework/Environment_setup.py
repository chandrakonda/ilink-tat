from selenium import webdriver
import os,traceback, pdb
from datetime import datetime
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import selenium.common.exceptions as web_driver_exceptions
import xml.etree.cElementTree  as ET
from apptio_automation.Framework.Utils import Utilities
from apptio_automation.Framework.Extensions.Driver_extensions import DriverSetup
import pytest, sys, logging
import apptio_automation.Framework.Extensions.Custom_logger as  cl

class EnvironmentSetup(object):

    #__var_parent_folder_path = (os.path.normpath(os.path.join(os.getcwdb())))
    #sys.path.append("C:\\Workingdirectory\\python\\sublime_projects\\Autoforms_pytest")
    log = cl.customLogger(logging.DEBUG)
    var_parent_folder_path =  os.path.abspath(os.path.join(os.path.dirname("__file__")))
    __var_framework_path = (os.path.normpath(os.path.join(var_parent_folder_path, 'Framework')))
    var_dynamic_name = datetime.now().strftime("%Y%m%d%H%M%S")
    var_today_date = datetime.now().strftime("%Y%m%d")  # current system date
    driver_type = None
    dict_config_values = None
    __driver = None

    def load_config_file(self):
        self.log.info("Read config data")
        print ("Read config data")
        var_config_class = ConfigValuesToDictionary()
        var_config_class.load_dictionary()

    @classmethod
    def get_parent_folder_path(cls):
        return cls.var_parent_folder_path

    @classmethod
    def get_framework_path(cls):
        return cls.__var_framework_path

    @classmethod
    def get_dynamic_name(cls):
        return cls.var_dynamic_name

    @classmethod
    def get_todays_date(cls):
        return cls.var_today_date

    #region driver
    # Creates a driver object and returns that object

    def setup(self):
        self.log.info("##########  Enter Set Up ####################3")
        self.load_config_file()  # load configuration file
        EnvironmentSetup.driver_type = ConfigValuesToDictionary.get_key_value('browser')
        __var_d = DriverSetup()
        EnvironmentSetup.__driver = __var_d.set_driver(EnvironmentSetup.__var_framework_path,EnvironmentSetup.driver_type)
        EnvironmentSetup.__driver.maximize_window()

    @classmethod
    def open_new_browser_session(cls):
        __val = None
        try:
            #cls.driver_type = ConfigValuesToDictionary.get_key_value('browser')
            if cls.driver_type.upper() == 'CHROME':
                __val = 'chrome'
            elif cls.driver_type.upper() == 'IE':
                __val = 'internet explorer'
            elif cls.driver_type.upper() == 'INTERNET EXPLORER':
                __val = 'internet explorer'
            elif cls.driver_type.upper() == 'FIREFOX':
                __val = 'firefox'

            EnvironmentSetup.get_driver().start_session(
                    desired_capabilities = {
                    'browserName': __val
                    })
        except Exception as e:
            raise e


    @classmethod
    def get_driver(cls):
        return EnvironmentSetup.__driver

    @classmethod
    def quit_driver(cls):
        print("Entered quit driver function")
        # global driver
        EnvironmentSetup.get_driver().quit()

    @classmethod
    def go_to_url(cls):
        __url = ConfigValuesToDictionary.get_key_value('url')
        print("Given URL in config file is '{}' ".format(__url) )
        EnvironmentSetup.get_driver().get(__url)

    @classmethod
    def go_to_other_url(cls,key_value):
        __url = ConfigValuesToDictionary.get_key_value(key_value)
        print("Given URL in config file is '{}' ".format(__url) )
        EnvironmentSetup.get_driver().get(__url)

    @classmethod
    def take_screen_shots(cls, filename_and_path):
        EnvironmentSetup.get_driver().save_screenshot(filename_and_path)
    #end  region

class ConfigValuesToDictionary:
    dict_config_values = {}
    log = cl.customLogger(logging.DEBUG)
    def load_dictionary(self):
        #global dict_config_values
        self.log.info("Current folder path is '{}'".format(EnvironmentSetup.get_parent_folder_path()))
        var_parent_folder_path = EnvironmentSetup.get_parent_folder_path()
        self.xml_file = (os.path.normpath(os.path.join(var_parent_folder_path,"Framework", 'config.xml')))  # Load xml file
        self.log.info("Config file {} ".format(self.xml_file))
        try:
            tree = ET.ElementTree(file=self.xml_file)
            root = tree.getroot()
            for child in root:
                self.dict_config_values[child.tag] = child.text
        except Exception as e:
            self.log.exception("Exception thrown while loading config file. Please check file in given path ",e)
        self.log.info("Config values are loaded in dictionary and count is {}".format(len(self.dict_config_values)))

    @classmethod
    def get_key_value(cls,key_value):
        global dict_config_values
        if (key_value in cls.dict_config_values):
            cls.log.info("Get key value for the key '{}'".format(key_value))
            return cls.dict_config_values[key_value]
        else:
            cls.log.Error("Given key '{}' is not present in the dictionary. Please give a valid key value".format(key_value))
            pytest.fail( "Given key '{}' is not present in the dictionary. Please give a valid key value".format(key_value))
#
class LoadTestData():
    __dict_test_data = {}
    log = cl.customLogger(logging.DEBUG)
    def load_data(self, folder_name, file_name,section_name = None):
        __project_folder = EnvironmentSetup.get_parent_folder_path()
        __application_folder_name = ConfigValuesToDictionary.get_key_value('projectfoldername')
        if (section_name == None):
            LoadTestData.__dict_test_data = Utilities.load_data_into_dict(__project_folder, __application_folder_name,folder_name, file_name)
        else:
            LoadTestData.__dict_test_data = Utilities.load_data_into_dict(__project_folder, __application_folder_name,
                                                                            folder_name, file_name,section_name)
    @classmethod
    def get_data_using_key(cls,key_value):
        __var_key_value = None
        if key_value in LoadTestData.__dict_test_data:
            __var_key_value = LoadTestData.__dict_test_data.get(key_value)
            cls.log.info("Value of the give key '{}' is '{}'".format(key_value,__var_key_value))
        else:
            cls.log.info("Given '{}' is not present in dictionary. Please check give key value".format(key_value))
            pytest.fail("Given '{}' is not present in dictionary. Please check give key value".format(key_value))
        return __var_key_value

class PageElements():
    log = cl.customLogger(logging.DEBUG)
    __dict_page_elements = {}
    def __init__(self):
        self.__project_folder = EnvironmentSetup.get_parent_folder_path()
        #self.__application_folder_name = ConfigValuesToDictionary.get_key_value('projectfoldername')

    def load_page_elements(self,file_name):
        __application_folder_name = ConfigValuesToDictionary.get_key_value('projectfoldername')
        try:
            PageElements.__dict_page_elements = Utilities.load_data_into_dict(self.__project_folder,__application_folder_name,"Page_Elements",file_name)
            self.log.info("length of page elements dictionary is "+format(str(len(PageElements.__dict_page_elements))))
        except:
            raise
    def get_element_identifier_dict(self):
        return PageElements.__dict_page_elements

    @classmethod
    def get_element_identifier(cls , name):
       if name in cls.__dict_page_elements:
           __var_element_value = cls.__dict_page_elements[name]
           cls.log.info("Value returned from page element dictionary is '{}'".format(__var_element_value))
       else:
            #print ("Key error is thrown in the get_element_identifier function. Please check given key value '{}'".format(name))
            raise("Key error is thrown in the get_element_identifier function. Please check given key value '{}'".format(name))
       return __var_element_value


def dict_cleanup():
    LoadTestData.__dict_test_data = None
    PageElements.__dict_page_elements = None
