"""
Page : TBM Council page
"""
from apptio_automation.Framework.Extensions.Webdriveractions_extensions import ElementExtensions as element
import json,time,pdb,pytest,logging
from apptio_automation.Apptio.Json_Helpers.JsonHelpers import JsonHelpers
from apptio_automation.Apptio.Pages.Categorydetails_page import CategoryDetailsPage
import apptio_automation.Framework.Extensions.Custom_logger as  cl

class TbmCouncilPage(element,JsonHelpers):
    log = cl.customLogger(logging.DEBUG)

    category_details = CategoryDetailsPage()

    def check_and_get_category_values(self,format_value):
        __local_list_ids,__local_list_values= [],[]
        try:
            if self.check_for_child_elements("column_0",format_value):
                __local_list_ids = self.get_attribute_values_in_list("column_element_list","id",format_value)
                for x in range(0,len(__local_list_ids)):
                    __local_list_values.append(__local_list_ids[x][4:])
            else:
                __local_list_ids = []
                __local_list_values = []
            return __local_list_ids, __local_list_values
        except Exception as e:
            self.log.exception("Exception thrown in 'check_and_get_category_values' method {}".format(e))
            raise
        
            
    def click_on_child_element(self,child_id):
        try:
            element.click_on_element_id_in_apptio_columns(child_id)
        except Exception as e:
            self.log.exception("Exception thrown in 'click_on_child_element' method {}".format(e))
            raise

    def click_on_image_element_of_selected_category(self,child_id):
        if self.check_image_for_category(child_id):
            self.click_on_element_format("image_element",child_id)

    def check_image_for_category(self,child_id):
        try:
            __is_displayed =element.is_element_displayed_format("image_element",child_id)
        except:
            raise
        return __is_displayed

    def come_out_of_details_section(self,row_no):
        try:
            self.click_on_element_format("come_out_of_details", row_no)
        except:
            raise



    def check_image_for_category1(self,child_id):
        try:
            if element.is_element_displayed_format("image_element",child_id):
                print("image is present")
            else:
                print("image is not present")
        except:
            raise


    def check_for_child_elements(self,name,column_no):
        try:
            time.sleep(1)
            return element.is_element_displayed_format(name,column_no)
        except Exception:
            self.log.exception("Child elements are not displayed so returning False")
            return False

    def check_for_child_elements1(self,column_no):
        try:
            time.sleep(1)
            return element.is_element_displayed_format("column_0",column_no)
        except Exception:
            return False


    def get_headings_from_details_section_in_a_list(self):
        pass
        __h3_name_list =[]
        __local_elements_list = element.get_elements_in_list("get_all_header_elements")
        for x in range(1,len(__local_elements_list)):
            __h3_name_list.append((element.get_text_for_given_element(__local_elements_list[x])).strip())
        return __h3_name_list


    def validate_col_values(self,col1_id_list,json_data_obj,n):
        for x in range(0, len(col1_id_list)):
            print (col1_id_list[x])
            __local_col1_child = json_data_obj["children"][x]
            self.click_on_child_element(col1_id_list[x])
            self.check_image_for_category(col1_id_list[x])
            col_id_list, col_value_list = self.check_and_get_category_values(n)  # check and get child count in col2 from app
            __local_json_col_child_list = self.get_child_names_in_list(__local_col1_child)  # json child count in col2
            self.check_for_public_cloud_in_application_and_json(__local_col1_child,col1_id_list[x])
            #print("length of jsonlist and app in col2 {},{}".format(str(len(__local_json_col_child_list)),str(len(col_value_list))))
            if __local_json_col_child_list == col_value_list and len(__local_json_col_child_list) != 0 and len(col_value_list) != 0:  # if child2 in json and app are matching
                self.validate_col_values(col_id_list,__local_col1_child,n+1)
            else:
                if len(__local_json_col_child_list) > len(col_value_list):
                    pytest.fail("Json data have more values than application..Please check ")
                elif len(__local_json_col_child_list) < len(col_value_list):
                    pytest.fail("Application values in col3 are not matching with Json")
                else:
                    print('\t\t' + "No child present for a given value in Json and application")

    def validate_details_of_each_category(self, col1_id_list, json_data_obj, n,row_no):
        for x in range(0, len(col1_id_list)):
            print(col1_id_list[x])
            __local_col1_child = json_data_obj["children"][x]
            self.click_on_child_element(col1_id_list[x])
            self.click_on_image_element_of_selected_category(col1_id_list[x])
            time.sleep(1)
            self.category_details.compare_app_json_details_data(__local_col1_child)
            time.sleep(1)
            self.come_out_of_details_section(row_no)
            col_id_list, col_value_list = self.check_and_get_category_values(n)  # check and get child count in col2 from app
            __local_json_col_child_list = self.get_child_names_in_list(__local_col1_child)  # json child count in col2
            self.check_for_public_cloud_in_application_and_json(__local_col1_child, col1_id_list[x])
            if __local_json_col_child_list == col_value_list and len(__local_json_col_child_list) != 0 and len(col_value_list) != 0:  # if child2 in json and app are matching
                self.validate_details_of_category(col_id_list, __local_col1_child, n + 1,row_no+1)
            else:
                if len(__local_json_col_child_list) > len(col_value_list):
                    pytest.fail("Json data have more values than application..Please check ")
                elif len(__local_json_col_child_list) < len(col_value_list):
                    pytest.fail("Application values in col3 are not matching with Json")
                else:
                    print('\t\t' + "No child present for a given value in Json and application")


    def check_for_public_cloud_in_application_and_json(self,json_object,col_id_value):
        __jsonhelp = JsonHelpers()
        if __jsonhelp.check_for_public_cloud_in_json(json_object):
            print("public cloud is present in json for id '{}'".format(col_id_value))
            if element.is_element_displayed_format("cloud_image_element",col_id_value):
                print("Cloud image is present in application for id '{}'".format(col_id_value))
            else:
                print("Cloud image is not present in application for id '{}'".format(col_id_value))
                self.log.error("################### cloud image is displayed #########################")
        else:
            print("public cloud is not present in json for id '{}'".format(col_id_value))
            pass



    def validate_description_values(self,col1_id_list,json_data_obj,n):
        for x in range(0, len(col1_id_list)):
            print (col1_id_list[x])
            __local_col1_child = json_data_obj["children"][x]
            self.click_on_child_element(col1_id_list[x])

            col_id_list, col_value_list = self.check_and_get_category_values(n)  # check and get child count in col2 from app
            __local_json_col_child_list = self.get_child_names_in_list(__local_col1_child)  # json child count in col2

            #print("length of jsonlist and app in col2 {},{}".format(str(len(__local_json_col_child_list)),str(len(col_value_list))))
            if __local_json_col_child_list == col_value_list and len(__local_json_col_child_list) != 0 and len(col_value_list) != 0:  # if child2 in json and app are matching
                self.validate_col_values(col_id_list,__local_col1_child,n+1)
            else:
                if len(__local_json_col_child_list) > len(col_value_list):
                    pytest.fail("Json data have more values than application..Please check ")
                elif len(__local_json_col_child_list) < len(col_value_list):
                    pytest.fail("Application values in col3 are not matching with Json")
                else:
                    print('\t\t' + "No child present for a given value in Json and application")

