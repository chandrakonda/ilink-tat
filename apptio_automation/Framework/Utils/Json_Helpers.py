import json
import apptio_automation.Framework.Extensions.Custom_logger as  cl
from apptio_automation.Apptio.Common.Constants import Constant_Values
class JsonHelpers():
    child_names_list = []
    def get_first_col_value(self, json_data_object):
        __local_json_child = []
        for child in json_data_object["children"]:
            __local_json_child.append(child["name"])
        return __local_json_child


    def get_child_names_in_list(self, json_data_object):
        __local_json_child = []
        try:
            for child in json_data_object["children"]:
                __local_json_child.append(child["name"])
            return __local_json_child
        except Exception:
            return []

    def get_value_of_key_for_given_list_dictionary_key(self,json_data_object,list_dictionary_key,dic_key):
        __local_json_child = []
        try:
            for child in json_data_object[list_dictionary_key]:
                __local_json_child.append(child[dic_key])
            return __local_json_child
        except Exception:
            return []


    def get_child_ids_recursively_list(self,json_data1,name):
        val = json_data1["children"]
        for x in range(0,len(val)):
            if "children" in val[x]:
                child_name = name+val[x]["id"]+","
                JsonHelpers.child_names_list.append(child_name)
                print(child_name)
                if len(val[x]["children"])>0:
                    self.get_child_ids_recursively_list(val[x],child_name)



