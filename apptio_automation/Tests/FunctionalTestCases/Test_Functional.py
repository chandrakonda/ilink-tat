'''
Test cases for Apptio
'''
# TODO : Need to check pytest.ini file
# TODO : Need to compare framework with Udemy framework and make improvements

# TODO # Need to create XL report
# Sathish
# TODO # Includes and excluded - need to check for headers - Complete - 22/1/2017
# TODO # Update data - come with plan
# 01/05/2017
# TODO # Select and unselect


import pytest,  traceback, time , pdb , csv
from pprint import pprint
from apptio_automation.Apptio.Json_Helpers.JsonHelpers import JsonHelpers
from apptio_automation.Apptio.Pages.Login_page import LoginPage
from apptio_automation.Apptio.Pages.TBMCouncil_page import TbmCouncilPage as tbmpage
from apptio_automation.Framework.Environment_setup import ConfigValuesToDictionary
import apptio_automation.Framework.Extensions.Custom_logger as  cl

from apptio_automation.Apptio.Common import Apptio_Common
from apptio_automation.Apptio.Common.Constants import Constant_Values
#--html=c:\workingdirectory\att\sample3.html --verbose --tb=short
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
        #pdb.set_trace()
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
###################################################################################################################################

    def test_3_validate_images_and_children_for_each_category(self,json_data):
        __local_tbm_page_obj = tbmpage()
        try:
            __local_tbm_page_obj.validate_cloud_details_images_and_children_for_category(json_data)
            results = getattr(__local_tbm_page_obj,"child_validation_results")
            #pdb.set_trace()
            val = [d["keyvalue"] for d in results if d["finalstatus"] == "Fail"]  # get the list of failed values from the results collected
            Apptio_Common.write_category_details_to_csv("childrenvalidationresults_",Constant_Values.children_validation_col_list,results) # write all the results in csv
            if len(val)>0: # if the length of failed list is > 1 , then fail the test case
                pytest.fail("Test case is failed")
        except Exception:
            raise
######################################################################################################################################################################################################################################################################

    def test_4_validate_description_details_of_each_category(self, json_data):
        __local_tbm_page_obj = tbmpage()
        try:
            __local_tbm_page_obj.validate_details_of_each_category_in_columns(json_data)
            results_list = getattr(Apptio_Common,"details_results_list")
            Apptio_Common.write_category_details_to_csv("Category_results",Constant_Values.detail_validation_col_list,results_list)
            fail_list = [d for d in results_list if d["Status"] =="Fail" ]
            if len(fail_list) >0:
                pytest.fail("Test case is failed")

        except:
            raise

    def test_5_Logout_from_application(self):
        obj_login_page = LoginPage()
        obj_login_page.logout()
############################################################################################################################################3
    ##########################TEMP###################################################
        # def test_5_validate_description_details_of_each_category(self,json_data):
        #     __local_tbm_page_obj = tbmpage()
        #     row_no = 0
        #     categorypage = CategoryDetailsPage()
        #     try:
        #         col1_id_list, col1_value_list = __local_tbm_page_obj.check_and_get_category_values(0)
        #         for x in range(0, len(col1_id_list)):
        #             __local_col1_child1 = json_data["children"][x]
        #             __local_tbm_page_obj.click_on_child_element(col1_id_list[x])  # click on child element
        #             col2_id_list, col2_value_list = __local_tbm_page_obj.check_and_get_category_values(1)  # check and get child count in col2 from application
        #             __local_tbm_page_obj.click_on_image_element_of_selected_category(col1_id_list[x])
        #             time.sleep(1)
        #             categorypage.compare_app_json_details_data(__local_col1_child1,col1_id_list[x])
        #             __local_tbm_page_obj.come_out_of_details_section(row_no)
        #             time.sleep(1)
        #             Test_Functional.first_col_value  = col1_id_list[x]
        #             if len(col2_value_list) != 0:  # if child are present
        #                 #__local_tbm_page_obj.validate_details_of_each_category_updated(col2_id_list, __local_col1_child1,2,row_no+1)
        #                 pass
        #
        #         else:
        #             print("there are no list values to run")
        #         __pass = getattr(categorypage, "pass_list")
        #         __pass_list = zip(*[d.values() for d in __pass])
        #         __fail = getattr(categorypage, "fail_list")
        #         with open("test.txt", "a") as myfile:
        #             myfile.write("\n pass "+str(__pass))
        #             myfile.write("\n fail " +str(__fail))
        #         with open(".\\Results\\test1.csv",'wb') as csvfile:
        #             fieldnames = ['firstcolvalue','currentkey','values','status']
        #             writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        #             writer.writerow(dict((fn, fn) for fn in fieldnames))
        #             #writer.writeheader()
        #             for row in __pass:
        #                 writer.writerow(row)
        #
        #
        #     except Exception:
        #         raise
        # def test_3_validate_child_values_for_parent_with_values_displayed_in_json(self, json_data):
        #     __local_tbm_page_obj = tbmpage()
        #     __local_json_data_obj = JsonHelpers()
        #     try:
        #         col1_id_list, col1_value_list = __local_tbm_page_obj.check_and_get_category_values(0)
        #         for x in range(0, len(col1_id_list)):
        #             __local_col1_child1 = json_data["children"][x]
        #             __local_tbm_page_obj.click_on_child_element(col1_id_list[x])  # click on child element
        #             __local_tbm_page_obj.check_image_for_category(col1_id_list[x]) # check image
        #             __local_tbm_page_obj.check_for_public_cloud_in_application_and_json(__local_col1_child1, col1_id_list[x]) # check cloud image
        #             col2_id_list, col2_value_list = __local_tbm_page_obj.check_and_get_category_values(1)  # check and get child count in col2 from app
        #             __local_json_col2_child_list = __local_json_data_obj.get_child_names_in_list(__local_col1_child1)  # json child count in col2
        #             print(col1_id_list[x])
        #             #print("length of jsonlist and app in col2 {},{}".format(str(len(__local_json_col2_child_list)),str(len(col2_value_list))))
        #             if __local_json_col2_child_list == col2_value_list and len(__local_json_col2_child_list) != 0 and len(col2_value_list) != 0:  # if child2 in json and app are matching
        #                 #print('\t\t' + "col2 values from application are matching with Json")
        #                 __local_tbm_page_obj.validate_col_values(col2_id_list, __local_col1_child1, 2)
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