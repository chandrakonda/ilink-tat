from apptio_automation.Framework.Extensions.Webdriveractions_extensions import ElementExtensions as element
import pdb,pytest,logging , sys
from apptio_automation.Apptio.Json_Helpers.JsonHelpers import JsonHelpers
import apptio_automation.Framework.Extensions.Custom_logger as  cl
from apptio_automation.Apptio.Common.Constants import Constant_Values
from apptio_automation.Framework.Utils.Utilities import compare_dict
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
        __header_list = self.get_list_of_details_header_names()
        __json_obj = JsonHelpers()
        json_expected_details = __json_obj.get_atum_entry_details1(json_data_object,__header_list)
        app_details = self.get_child_items_for_each_element1(__header_list)
        added,removed,modified,same = compare_dict(json_expected_details,app_details)
        print("##########Values that are not matching##############33")
        print (modified)
        print("##########Values that are matching##############")
        print (same)
        if bool(modified):
            write_category_details_in_log("datamismatch",modified)
        collect_details_results(modified,same,app_id_value,col1_parent_name)

    def get_child_items_for_each_element1(self, header_list):
        app_dict = {}
        for x in range(0, len(header_list)):
            __app_header_value = header_list[x]
            if __app_header_value == "":
                # description_value = element.is_text_available("description_text1")
                description_value = element.get_attribute_value("description_text1", "innerHTML")
                if '<p>' not in description_value:
                    description_value = element.get_attribute_value("description_text1", "innerText")
                if "&amp;" in description_value:
                    description_value = unicode.replace(description_value, '&amp;', "&")
                # if "</p><p></p>" in description_value:
                #     description_value = unicode.replace(description_value,"</p><p></p>","<p>")
                app_dict["Description"] = unicode(description_value)
            # elif __app_header_value in self.constant.app_to_json_mapping:
            #     __uom_element_list = element.get_attribute_values_in_list("description_children_text_values","innerHTML",__app_header_value)
            #     app_dict[__app_header_value] = __uom_element_list
            elif __app_header_value == "Unit of Measure List":
                __uom_element_list = element.get_attribute_values_in_list("description_children_text_values", "innerHTML", __app_header_value)
                __uom_element_list = [val.replace("&amp;","&")for val in __uom_element_list]
                app_dict[__app_header_value] = __uom_element_list
            elif __app_header_value in self.constant.app_to_json_mapping:
                __user_list = element.get_text_in_list("description_children_text_values",
                                                       __app_header_value)  # Need to check with constant dictionary
                app_dict[__app_header_value] = __user_list
            else:
                self.log.info("There are no matching values in dictionary")
        return app_dict




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


