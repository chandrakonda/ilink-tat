from apptio_automation.Framework.Extensions.Webdriveractions_extensions import ElementExtensions as element
import pdb,pytest,logging , sys
from apptio_automation.Apptio.Json_Helpers.JsonHelpers import JsonHelpers
import apptio_automation.Framework.Extensions.Custom_logger as  cl
from apptio_automation.Apptio.Common.Constants import Constant_Values
#from apptio_automation.Apptio.Json_Helpers.JsonHelpers import JsonHelpers





class CategoryDetailsPage(element):

    log = cl.customLogger(logging.DEBUG)
    constant = Constant_Values()
    def get_list_of_details_header_names(self):
        __header_list = []
        try:
            __list =  element.get_elements_in_list("h3_details_header")
            for x in range(0,len(__list)):
                __header_list.append(element.get_attribute_value_of_element(__list[x],"innerText"))
            self.log.info("Length of details header list is {} ".format(str(__list)))
            return __header_list
        except Exception as e:
            self.log.exception("Exception thrown in 'get_list_of_details_header_in_details' method as {}".format(e))
            raise


# for each tag get the child items from application

    def get_child_items_for_each_element(self,header_list):
        app_dict = {}
        for x in range(0,len(header_list)):
            __app_header_value = header_list[x]
            if __app_header_value =="":
                text_element = element.get_attribute_value("description_text1","innerHTML")
                app_dict["Description"] = unicode(text_element)
            elif __app_header_value in self.constant.app_to_json_mapping:
                __user_list = element.get_text_in_list("description_children_text_values", __app_header_value) # Need to check with constant dictionary
                app_dict[__app_header_value] = __user_list
            else:
                self.log.info("There are no matching values in dictionary")
            # elif __app_header_value == "Unit of Measure List":
            #     __m_list = element.get_text_in_list("description_children_text_values","Unit of Measure List")
            #     app_dict["Unit of Measure List"] = __m_list
            # elif __app_header_value == "Children":
            #     __c_list = element.get_text_in_list("description_children_text_values", "Children")
            #     app_dict["Children"] = __c_list
            # elif __app_header_value == "Service Offering Levers":
            #     __s_list = element.get_text_in_list("description_children_text_values", "Service Offering Levers")
            #     app_dict["Service Offering Levers"] = __s_list
            # elif __app_header_value == "Service Level KPIs":
            #     __k_list = element.get_text_in_list("description_children_text_values", "Service Level KPIs")
            #     app_dict["Service Level KPIs"] = __k_list

        return app_dict

    def get_child_items_for_each_element1(self, header_list):
        app_dict = {}
        for x in range(0, len(header_list)):
            __app_header_value = header_list[x]
            if __app_header_value == "":
                text_element = element.get_attribute_value("description_text1", "innerHTML")
                app_dict["Description"] = unicode(text_element)
            elif __app_header_value in self.constant.app_to_json_mapping:
                __user_list = element.get_text_in_list("description_children_text_values", __app_header_value)  # Need to check with constant dictionary
                app_dict[__app_header_value] = __user_list
            else:
                self.log.info("There are no matching values in dictionary")
        return app_dict

    def compare_app_json_details_data(self,json_data_object):
        __header_list = self.get_list_of_details_header_names()
        __json_obj = JsonHelpers()
        json_expected_details = __json_obj.get_atum_entry_details1(json_data_object,__header_list)
        app_details = self.get_child_items_for_each_element1(__header_list)
        added,removed,modified,same = self.compare_dict(json_expected_details,app_details)
        print("##########Values that are not matching##############33")
        print (modified)
        print("##########Values that are matching##############")
        print (same)
        # if json_expected_details == app_details:
        #     print("values are matching")
        # else:
        #     print ("value mismatch")
    def compare_dict(self,d1,d2):
        d1_keys = set(d1.keys())
        d2_keys = set(d2.keys())
        intersect_keys = d1_keys.intersection(d2_keys)
        added = d1_keys - d2_keys
        removed = d2_keys - d1_keys
        modified = {o: (d1[o], d2[o]) for o in intersect_keys if d1[o] != d2[o]}
        same = set(o for o in intersect_keys if d1[o] == d2[o])
        return added, removed, modified, same


# for each tag get child from json

# compare values between json and app

# store pas and fail list

