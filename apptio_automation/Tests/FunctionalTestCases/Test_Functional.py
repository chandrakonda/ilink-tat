'''
Test cases for Apptio
'''
# TODO : Need to check pytest.ini file
# TODO : Need to compare framework with Udemy framework and make improvements

import pytest,  traceback, time , pdb
from pprint import pprint
from apptio_automation.Apptio.Json_Helpers.JsonHelpers import JsonHelpers
from apptio_automation.Apptio.Pages.Login_page import LoginPage
from apptio_automation.Apptio.Pages.TBMCouncil_page import TbmCouncilPage as tbmpage
from apptio_automation.Framework.Environment_setup import ConfigValuesToDictionary
import apptio_automation.Framework.Extensions.Custom_logger as  cl

@pytest.mark.usefixtures("apptio_setup","function_setup","jsonfileversion")
class Test_Functional():


    def test_1_login_into_application(self,jsonfileversion):
        try:
            time.sleep(3)
            #pdb.set_trace()
            print (jsonfileversion)
            obj_login_page =  LoginPage()
            user_name = ConfigValuesToDictionary.get_key_value('loginuser')
            print ("user name value is {}".format(user_name))
            pass_word =  ConfigValuesToDictionary.get_key_value("loginpassword")
            print("Password value is entered")
            if obj_login_page.login(user_name,pass_word,jsonfileversion):
                pass
                time.sleep(5)
            else:
                status = "Failed"
        except Exception:
            traceback.print_stack()
            pytest.fail("Test case is failed")
            #pytest.fail("Login test case is failed")

    def test_2_validate_first_column_category_values_with_given_json(self,json_data):
        pdb.set_trace()
        __local_tbm_page_obj = tbmpage()
        _local_app_child_id_list,__local_app_first_child_label_list = __local_tbm_page_obj.check_and_get_category_values(0) # get first col values from application

        # get first child values from JSON
        __local_json_helper_class_obj = JsonHelpers()
        __local_json_first_child_label_list =__local_json_helper_class_obj.get_first_col_value(json_data)

        # comparing lists from application and json files
        if len(__local_json_first_child_label_list) == len(__local_app_first_child_label_list):
            assert __local_app_first_child_label_list == __local_json_first_child_label_list

        else:
            pytest.fail("Values in the first column are not matching.Test case is failed")


    #
    # def test_3_validate_child_values_for_parent_with_values_displayed_in_json(self, json_data):
    #     __local_tbm_page_obj = tbmpage()
    #     __local_json_data_obj = JsonHelpers()
    #     try:
    #         col1_id_list, col1_value_list = __local_tbm_page_obj.check_and_get_category_values(0)
    #         for x in range(0, len(col1_id_list)):
    #             __local_tbm_page_obj.click_on_child_element(col1_id_list[x])
    #             col2_id_list, col2_value_list = __local_tbm_page_obj.check_and_get_category_values(1)  # check and get child count in col2 from app
    #             __local_col1_child1 = json_data["children"][x]
    #             __local_json_col2_child_list = __local_json_data_obj.get_child_names_in_list(__local_col1_child1)  # json child count in col2
    #             print(col1_id_list[x])
    #             print("length of jsonlist and app in col2 {},{}".format(str(len(__local_json_col2_child_list)),str(len(col2_value_list))))
    #             if __local_json_col2_child_list == col2_value_list and len(__local_json_col2_child_list) != 0 and len(col2_value_list) != 0:  # if child2 in json and app are matching
    #                 print('\t\t' + "col2 values from application are matching with Json")
    #                 __local_tbm_page_obj.validate_col_values(col2_id_list,__local_col1_child1,2)
    #             else:
    #                 if len(__local_json_col2_child_list) > len(col2_value_list):
    #                     pytest.fail("Json data have more values than application..Please check")
    #                 elif len(__local_json_col2_child_list) < len(col2_value_list):
    #                     pytest.fail("Application values in col2 are not matching with Json")
    #                 else:
    #                     print("No child present in col2 for given col1 value in Json and application")
    #         else:
    #             print("there are no list values to run")
    #     except Exception:
    #         raise

    def test_3_validate_child_values_for_parent_with_values_displayed_in_json(self, json_data):
        __local_tbm_page_obj = tbmpage()
        __local_json_data_obj = JsonHelpers()
        try:
            col1_id_list, col1_value_list = __local_tbm_page_obj.check_and_get_category_values(0)
            for x in range(0, len(col1_id_list)):
                __local_col1_child1 = json_data["children"][x]
                __local_tbm_page_obj.click_on_child_element(col1_id_list[x])  # click on child element
                __local_tbm_page_obj.check_image_for_category(col1_id_list[x]) # check image
                __local_tbm_page_obj.check_for_public_cloud_in_application_and_json(__local_col1_child1, col1_id_list[x]) # check cloud image
                col2_id_list, col2_value_list = __local_tbm_page_obj.check_and_get_category_values(1)  # check and get child count in col2 from app
                __local_json_col2_child_list = __local_json_data_obj.get_child_names_in_list(__local_col1_child1)  # json child count in col2
                print(col1_id_list[x])
                #print("length of jsonlist and app in col2 {},{}".format(str(len(__local_json_col2_child_list)),str(len(col2_value_list))))
                if __local_json_col2_child_list == col2_value_list and len(__local_json_col2_child_list) != 0 and len(col2_value_list) != 0:  # if child2 in json and app are matching
                    #print('\t\t' + "col2 values from application are matching with Json")
                    __local_tbm_page_obj.validate_col_values(col2_id_list, __local_col1_child1, 2)
                else:
                    if len(__local_json_col2_child_list) > len(col2_value_list):
                        pytest.fail("Json data have more values than application..Please check")
                    elif len(__local_json_col2_child_list) < len(col2_value_list):
                        pytest.fail("Application values in col2 are not matching with Json")
                    else:
                        print("No child present in col2 for given col1 value in Json and application")
            else:
                print("there are no list values to run")
        except Exception:
            raise

    def test_4_validate_service_type_for_a_given_business_unit(self):
        obj_login_page = LoginPage()
        obj_login_page.logout()
        # pass
        # def test_4_validate_category_values1(self,json_data):
        #     __local_tbm_page_obj = tbmpage()
        #     __local_json_data_obj = JsonHelpers()
        #     try:
        #         __local_app_first_child_id, __local_app_first_child_value = __local_tbm_page_obj.get_category_values_from_application("column_element_list",0)
        #         for x in range(0,len(__local_app_first_child_id)):
        #             __local_tbm_page_obj.click_on_child_element(__local_app_first_child_id[x])
        #             __local_app_is_child_present_in_col2 = __local_tbm_page_obj.check_for_child_elements("column_0", 1)
        #             print(__local_app_first_child_id[x])
        #             if __local_app_is_child_present_in_col2:
        #                 #print("child present in col2")
        #                 __local_app_2_child_id_list, __local_app_2_child_value_list = __local_tbm_page_obj.get_category_values_from_application("column_element_list",1)
        #                 for y in range(0,len(__local_app_2_child_id_list)):
        #                     print('\t\t'+__local_app_2_child_id_list[y])
        #                     __local_tbm_page_obj.click_on_child_element(__local_app_2_child_id_list[y])
        #                     __local_app_is_child_present_in_col3 = __local_tbm_page_obj.check_for_child_elements("column_0", 2)
        #                     if __local_app_is_child_present_in_col3:
        #                         __local_app_3_child_id_list, __local_app_3_child_value_list = __local_tbm_page_obj.get_category_values_from_application("column_element_list",2)
        #                         for z in range(0,len(__local_app_3_child_id_list)):
        #                             print('\t\t\t' + __local_app_3_child_id_list[z])
        #                             __local_tbm_page_obj.click_on_child_element(__local_app_3_child_id_list[z])
        #                             __local_app_is_child_present_in_col4 = __local_tbm_page_obj.check_for_child_elements("column_0", 3)
        #                             if __local_app_is_child_present_in_col4:
        #                                 __local_app_4_child_id_list, __local_app_4_child_value_list = __local_tbm_page_obj.get_category_values_from_application("column_element_list",3)
        #                                 print(__local_app_4_child_id_list)
        #                             else:
        #                                 print('\t\t\t' +"no child present in col4 for given col3 value")
        #                             if z == (len(__local_app_3_child_id_list)-1):
        #                                 #pdb.set_trace()
        #                                 __local_tbm_page_obj.click_on_child_element(__local_app_2_child_id_list[y])
        #                     else:
        #                         print('\t\t'+"no child present in col3 for given col2 value")
        #
        #                     if y == (len(__local_app_2_child_id_list)-1):
        #                         __local_tbm_page_obj.click_on_child_element(__local_app_first_child_id[x])
        #
        #             else:
        #                 print('\t'+"no child present in col2 for given col1 value")
        #
        #     except Exception:
        #         raise
