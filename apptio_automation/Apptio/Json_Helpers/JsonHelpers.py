import json
import apptio_automation.Framework.Extensions.Custom_logger as  cl
from apptio_automation.Apptio.Common.Constants import Constant_Values
class JsonHelpers():
    pass

    def get_first_col_value(self,json_data_object):
        __local_json_child = []
        for child in json_data_object["children"]:
            __local_json_child.append(child["name"])
        return __local_json_child

    def get_child_names_in_list(self,json_data_object):
        __local_json_child = []
        try:
            for child in json_data_object["children"]:
                __local_json_child.append(child["name"])
            return __local_json_child
        except Exception:
            return []

    def get_child_count(self,json_data_object):
        __local_json_child = []
        try:
            for child in json_data_object["children"]:
                __local_json_child.append(child["name"])
            return len(__local_json_child)
        except Exception:
            return 0
    def check_for_public_cloud_in_json(self,json_data_object):
        try:
            if "public_cloud" in  json_data_object["atum_entry"]:
                return True
        except:
            return False



    def get_atum_entry_details1(self, json_data_object, application_header_list_values):
        __json_atum_entry_values = {}
        const = Constant_Values()
        child = json_data_object["atum_entry"]
        try:
            for x in range(0, len(application_header_list_values)):  # need to change based on the constant file
                application_header_value = application_header_list_values[x]
                if application_header_value == "":
                    key_value = const.app_to_json_mapping["Description"]  # get the json key value from constant file
                    __json_atum_entry_values["Description"] = unicode(child[key_value])  # add the description details
                elif application_header_value in const.app_to_json_mapping:
                    __value_list = []
                    key_value = const.app_to_json_mapping[application_header_value]  # get the json key value from constant file
                    if key_value == 'target_users':
                        __value_list = [x.strip() for x in child[key_value][0]["users"]]
                    elif key_value == "uom_list":
                        for uomlist in child[key_value]:  # for each UOM dictionary in the UOM list
                            for k, v in uomlist.items():
                                __uom_val = k + ": " + v
                                __value_list.append(__uom_val.strip())
                    elif key_value == "children":
                        for children_name in json_data_object[key_value]:  # for each child in the list,
                            __value_list.append(children_name["label"])  # get label name
                    else:
                        __value_list = [x.strip() for x in child[key_value]]
                    __json_atum_entry_values[application_header_value] = __value_list  # add values to dictionary
                    # elif application_header_value == "Examples":
                    #     pass
                    #     # pending, need to know how to handle values like below. need to check
                    #     # "examples": [
                    #     #     "AWS \u2013 Lambda",
                    #     #     "Azure \u2013 Batch"
                    #     # ]
        except:
            raise
        return __json_atum_entry_values

    def get_keys(self,json_data_object):
        key=[]
        try:
            key = json_data_object.keys()
            return key
        except Exception:
            print("could not find keys")
            return 0

    def get_excludes_and_includes(self,json_data_object, application_header_list_values):
        __json_include_exclude_values = {}
        const = Constant_Values()
        child = json_data_object["atum_entry"]
        try:
            for x in range(0, len(application_header_list_values)):  # need to change based on the constant file
                application_header_value = application_header_list_values[x]

                if "Includes" in application_header_value:
                    __value_list = []
                    key = application_header_value.keys()
                    for includelist in child["includes"]:
                        __parentname = application_header_value[key[0]][1]
                        __name = application_header_value[key[0]][2]
                        if __parentname in includelist:
                            if includelist[__parentname] == __name:
                                __value_list = __value_list + includelist['list']

                    __json_include_exclude_values[application_header_value[key[0]][0]] = __value_list

                elif "Excludes" in application_header_value:
                    __value_list = []
                    key = application_header_value.keys()
                    for list in child["excludes"]:
                        __parentname = application_header_value[key[0]][1]
                        __name = application_header_value[key[0]][2]
                        if __parentname in list:
                            if list[__parentname] == __name:
                                __value_list = __value_list + list['list']

                    __json_include_exclude_values[application_header_value[key[0]][0]] = __value_list
        except:
            raise
        return __json_include_exclude_values

    def get_include_and_excludes_from_json(self,json_data_object):
        try:
            pass
            _include_list = json_data_object["atum_entry"]["includes"]
            _exlcude_list = json_data_object["atum_entry"]["excludes"]
            _include_list1 = _include_list + _exlcude_list
            return _include_list1
        except:
            return []