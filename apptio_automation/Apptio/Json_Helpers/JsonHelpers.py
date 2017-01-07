import json
import apptio_automation.Framework.Extensions.Custom_logger as  cl
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




