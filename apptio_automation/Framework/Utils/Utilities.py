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
        print ("config file path is ",var_parser_file)
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

def compare_list_symmetric(list1,list2):
    same = {}
    modified = set(list1).symmetric_difference(set(list2))
    if bool(modified):
        return modified,same
    else:
        return modified,same
def compare_list_of_dictionaries(list1,list2):
    pair = zip(list1,list2)
    diff = [[(k) for k in x if x[k] != y[k]] for x, y in pair if x != y]
    pair1 = zip(list1,list2)
    same = [[(k, x[k], y[k]) for k in x if x[k] == y[k]] for x, y in pair1 if x == y]
    return diff , same

def compare_list_of_dictionaries1(list1,list2):
    same_list = []
    modified_list = []
    if len(list1) == len(list2):
        for x in range(0,len(list1)):
            added, removed, modified, same= compare_dict(list1[x],list2[x])
            if bool(modified):
                modified_list.append(modified)
            same_list.append(same)
        return modified_list,same_list
    else:
        pass
