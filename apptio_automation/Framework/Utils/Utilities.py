import os,traceback,configparser
#from Framework.Environment_setup import EnvironmentSetup

from selenium.webdriver.common.by import *
from selenium import webdriver

# get page elements from a text file given in application folders using config parser

#end region
import apptio_automation.Framework.Extensions.Custom_logger as  cl

class Return_parser():

    def return_config_parser(self):
        var_parser = configparser.RawConfigParser()
        return var_parser


#########################################
# Function to read load data from text file into dictionary
##########################################
def load_data_into_dict(project_folder,application_folder_name,folder_name,file_name,given_section_name= None):
    __dict_elements = {}
    try:
        var_parser_file = os.path.normpath(os.path.join(project_folder,application_folder_name, folder_name, file_name + ".txt"))
        print "config file path is ",var_parser_file
        __read_file = Return_parser()
        __var_Parser= __read_file.return_config_parser()
        __var_Parser.read(var_parser_file)
        for section_name in __var_Parser.sections():  # for every section in the config file
            if (given_section_name == None):
                for name, value in __var_Parser.items(section_name): # for every key value in the config file
                    __dict_elements[name] = value
            elif (section_name==given_section_name): # get only key - values in a given section
                for name, value in __var_Parser.items(section_name): # for every key value in the config file
                    __dict_elements[name] = value
        #print len(__dict_elements)
        return __dict_elements
    except IndexError:
        print("error thrown we cannot proceed with loading of page elements")
        raise
    except Exception:
        print("error thrown we cannot proceed with loading of page elements")
        raise

def get_test_case_name(instance):
    return instance.__name__


def compare_dict(d1, d2):
    d1_keys = set(d1.keys())
    d2_keys = set(d2.keys())
    intersect_keys = d1_keys.intersection(d2_keys)
    added = d1_keys - d2_keys
    removed = d2_keys - d1_keys
    modified = {o: (d1[o], d2[o]) for o in intersect_keys if d1[o] != d2[o]}
    same = set(o for o in intersect_keys if d1[o] == d2[o])
    return added, removed, modified, same