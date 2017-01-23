from apptio_automation.Framework.Extensions.Webdriveractions_extensions import ElementExtensions as element
import pdb,pytest,logging , sys
from apptio_automation.Apptio.Json_Helpers.JsonHelpers import JsonHelpers
import apptio_automation.Framework.Extensions.Custom_logger as  cl
from apptio_automation.Apptio.Common.Constants import Constant_Values
from apptio_automation.Framework.Utils.Utilities import compare_dict,compare_list_of_dictionaries1
from apptio_automation.Apptio.Common.Apptio_Common import collect_details_results,write_category_details_in_log

#pytest.mark.usefixtures("pass_dict", "fail_dict")
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

    def compare_app_json_details_data(self,json_data_object,app_id_value,col1_parent_name):
        __json_obj = JsonHelpers()
        __header_list = self.get_list_of_details_header_names()
        json_expected_details = __json_obj.get_atum_entry_details1(json_data_object, __header_list)
        app_details = self.get_child_items_for_each_element(__header_list)
        added,removed,modified,same = compare_dict(json_expected_details,app_details)
        print("##########Values that are not matching##############33")
        print (modified)
        print("##########Values that are matching##############")
        print (same)
        if bool(modified):
            modified["child_name"] = app_id_value
            write_category_details_in_log("DataMismatch",modified)
        collect_details_results(modified,same,app_id_value,col1_parent_name)

    def get_child_items_for_each_element(self, header_list):
        app_dict = {}
        for x in range(0, len(header_list)):
            __app_header_value = header_list[x]
            if __app_header_value == "":
                description_value = element.get_attribute_value("description_text1", "innerHTML")
                if '<p>' not in description_value:
                    description_value = element.get_attribute_value("description_text1", "innerText")
                if "&amp;" in description_value:
                    description_value = unicode.replace(description_value, '&amp;', "&")
                app_dict["Description"] = unicode(description_value)
            elif __app_header_value == "Unit of Measure List":
                __uom_element_list = element.get_attribute_values_in_list("description_children_text_values", "innerHTML", __app_header_value)
                __uom_element_list = [val.replace("&amp;","&")for val in __uom_element_list]
                app_dict[__app_header_value] = __uom_element_list
            elif __app_header_value in self.constant.app_to_json_mapping:
                __user_list = element.get_text_in_list("description_children_text_values", __app_header_value)  # Need to check with constant dictionary
                app_dict[__app_header_value] = __user_list
            else:
                self.log.info("There are no matching values in dictionary")
        return app_dict

#
# ########################################################################################################################
# # Get include and exclude values from the application and compare values
# ########################################################################################################################

    def compare_exclude_and_include_in_app_and_json(self,json_data_object,app_id_value,col1_parent_name):
        __json_obj = JsonHelpers()
        json_expected_details = __json_obj.get_include_and_excludes_from_json(json_data_object)
        app_details = self.get_include_and_exclude_details_from_application()
        # write data to notepad for reference
        write_category_details_in_log("ExcludeandIncludeData", app_id_value)
        write_category_details_in_log("ExcludeandIncludeData",json_expected_details)
        write_category_details_in_log("ExcludeandIncludeData", app_details)

        # Compare data between application and Json
        diffvalues,samevalues= compare_list_of_dictionaries1(json_expected_details,app_details)
        # write data to notepad for reference
        if len(diffvalues) >= 1:
            write_category_details_in_log("ExcludeDataMismatch", app_id_value)
            write_category_details_in_log("ExcludeDataMismatch", diffvalues)

        collect_details_results(diffvalues,samevalues,app_id_value,col1_parent_name)

    def get_include_and_exclude_details_from_application(self):
        try:
            __include_list = self._get_include_and_exclude_from_application("include_elements","include_header1","include_list1")
            __exclude_list = self._get_include_and_exclude_from_application("exclude_elements","exclude_header1","exclude_list1")
            __include_list = __include_list + __exclude_list
            return __include_list
        except:
            return []

    def _get_include_and_exclude_from_application(self,parent_element,span_element_name,li_element_name):
        _val_list = []
        try:
            __list__div_elements = element.get_elements_in_list(parent_element)
            x= 0
            for div_element in __list__div_elements:
                _dic_1 = {}
                _list_val = []
                x = x+1
                element.scroll_to_web_element_location(div_element)
                _span_element = element.get_web_element_format(span_element_name,x)
                parent_name = unicode(element.get_attribute_value_of_element(_span_element,"parentname"))
                _name = unicode(element.get_attribute_value_of_element(_span_element, "name"))
                if parent_name == "cost_pools":
                    parent_name = parent_name[:-1]
                _dic_1[parent_name] = _name
                _ul_element = element.get_elements_in_list(li_element_name,x)
                for ele in _ul_element:
                    element.scroll_to_web_element_location(ele)
                    __val1 = element.get_attribute_value_of_element(ele,"innerText")
                    _list_val.append(__val1)
                _dic_1["list"] = _list_val
                _val_list.append(_dic_1)
            return _val_list
        except:
            #raise
            return _val_list





            # def collect_results(self,modified,same,current_category_value,):
    #     #__val = TbmCouncilPage.col1_parent_name
    #     #__val = getattr(tbmpage,"col1_parent_name")
    #     __val = 1
    #     if bool(modified):
    #         fail_dict ={}
    #         fail_dict["firstcolvalue"] = __val
    #         fail_dict["currentkey"] = current_category_value
    #         fail_dict["values"] = modified
    #         fail_dict["status"] = "Fail"
    #         CategoryDetailsPage.fail_list.append(fail_dict)
    #     elif bool(same):
    #         pass_dict = {}
    #         pass_dict["firstcolvalue"] = __val
    #         pass_dict["currentkey"] = current_category_value
    #         pass_dict["values"] = same
    #         pass_dict["status"] = "Pass"
    #         CategoryDetailsPage.pass_list.append(pass_dict)




# for each tag get child from json

# compare values between json and app

# store pas and fail list

        # with open(".\\Results\\differencedata.txt", "a") as myfile:
        #     myfile.write("\n")
        #     myfile.write(app_id_value)
        #     myfile.write("\n Header list from application ")
        #     myfile.write(str(header_list))
        #     myfile.write("\n Header values that are not matching")
        #     myfile.write("\n")
        #     myfile.write(str(modified))

#
# def get_atum_entry_details(self, json_data_object, application_header_list_values):
#     __json_atum_entry_values = {}
#     const = Constant_Values()
#     child = json_data_object["atum_entry"]
#     try:
#         for x in range(0, len(application_header_list_values)):  # need to change based on the constant file
#             application_header_value = application_header_list_values[x]
#             if application_header_value == "":
#                 key_value = const.app_to_json_mapping["Description"]  # get the json key value from constant file
#                 __json_atum_entry_values["Description"] = unicode(child[key_value])  # add the description details
#             elif application_header_value == "Target Users":
#                 key_value = const.app_to_json_mapping["Target Users"]  # get the json key value from constant file
#                 __users_list = [x.strip() for x in child[key_value][0]["users"]]  # trim the extra spaces in the list
#                 __json_atum_entry_values["Target Users"] = __users_list  # add the list to the json dictionary
#             elif application_header_value == "Unit of Measure List":
#                 __uom_list = []
#                 key_value = const.app_to_json_mapping[
#                     "Unit of Measure List"]  # get the json key value from constant file
#                 for uomlist in child[key_value]:  # for each UOM dictionary in the UOM list
#                     for k, v in uomlist.items():
#                         __uom_list.append(k + ": " + v)
#                 __json_atum_entry_values["Unit of Measure List"] = __uom_list
#             elif application_header_value == "Children":
#                 __child_label_list = []
#                 key_value = const.app_to_json_mapping["Children"]  # get the json key value from constant file
#                 for children_name in json_data_object[key_value]:  # for each child in the list,
#                     __child_label_list.append(children_name["label"])  # get label name
#                 __json_atum_entry_values["Children"] = __child_label_list  # add values to dictionary
#             elif application_header_value == "Service Offering Levers":
#                 key_value = const.app_to_json_mapping[
#                     "Service Offering Levers"]  # get the json key value from constant file
#                 __services_list = [x.strip() for x in child[key_value]]
#                 __json_atum_entry_values["Service Offering Levers"] = __services_list  # add values to dictionary
#             elif application_header_value == "Service Level KPIs":
#                 key_value = const.app_to_json_mapping["Service Level KPIs"]  # get the json key value from constant file
#                 __kpi_list = [x.strip() for x in child[key_value]]
#                 __json_atum_entry_values["Service Level KPIs"] = __kpi_list  # add values to dictionary
#                 # elif application_header_value == "Examples":
#                 #     pass
#                 #     # pending, need to know how to handle values like below. need to check
#                 #     # "examples": [
#                 #     #     "AWS \u2013 Lambda",
#                 #     #     "Azure \u2013 Batch"
#                 #     # ]
#     except:
#         raise
#     return __json_atum_entry_values


#     def get_list_exclude_includes_header_names(self):
#         __exclude_header_list = []
#         try:
#             __includelist = element.get_elements_in_list("includes_header")
#             __excludelist = element.get_elements_in_list("excludes_header")
#             for y in range(0, len(__includelist)):
#                 __includelist_name = str("Includes-"+element.get_attribute_value_of_element(__includelist[y],"innerHTML"))
#                 __attributelist = []
#                 __attributelist.append(__includelist_name)
#                 __attributelist.append(str(element.get_attribute_value_of_element(__includelist[y],"parentname")))
#                 __attributelist.append(str(element.get_attribute_value_of_element(__includelist[y], "name")))
#                 __exclude_header_list.append({'Includes':__attributelist})
#
#             for z in range(0, len(__excludelist)):
#                 __excludelist_name = str("Excludes-"+element.get_attribute_value_of_element(__excludelist[z],"innerHTML"))
#                 __attributelist = []
#                 __attributelist.append(__excludelist_name)
#                 __attributelist.append(str(element.get_attribute_value_of_element(__excludelist[z],"parentname")))
#                 __attributelist.append(str(element.get_attribute_value_of_element(__excludelist[z], "name")))
#                 __exclude_header_list.append({'Excludes':__attributelist})
#             return __exclude_header_list
#         except Exception as e:
#             self.log.exception("Exception thrown in 'get_list_of_details_header_in_details' method as {}".format(e))
#             raise
#
#     # def get_include_exclude_details(self,header_list):
#     #     app_dict_ = {}
#     #     for x in range(0, len(header_list)):
#     #         __app_header_value = header_list[x]
#     #         if "Includes" in __app_header_value:
#     #             key = __app_header_value.keys()
#     #             __header_value = __app_header_value[key[0]][0].replace("Includes-", "")
#     #             __user_list = element.get_text_in_list("includes_children_text_values", __header_value)  # Need to check with constant dictionary
#     #             app_dict_[__app_header_value[key[0]][0]] = __user_list
#     #         elif "Excludes" in __app_header_value:
#     #             key = __app_header_value.keys()
#     #             __header_value = __app_header_value[key[0]][0].replace("Excludes-", "")
#     #             __user_list = element.get_text_in_list("excludes_children_text_values", __header_value)  # Need to check with constant dictionary
#     #             app_dict_[__app_header_value[key[0]][0]] = __user_list
#     #         elif __app_header_value in self.constant.app_to_json_mapping:
#     #             __user_list = element.get_text_in_list("description_children_text_values", __app_header_value)  # Need to check with constant dictionary
#     #             app_dict_[__app_header_value] = __user_list
#     #         else:
#     #             self.log.info("There are no matching values in dictionary")
#     #     return app_dict_