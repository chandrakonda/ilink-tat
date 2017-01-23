import pytest,pdb,csv
from apptio_automation.Framework.Utils.Json_Helpers import JsonHelpers
class Test_temp():
    #pdb.set_trace()
    # def test_1_sample(self):
    #     print("test1")
    #
    # def test_2_sample(self):
    #     print("test1")
    #
    #
    # def test_3_sample(self):
    #     print("test1")


    def test_get_json_data(self,json_data):
        a = JsonHelpers()
        val = json_data["children"]
        name = ""
        for x in range(0,len(val)):
            name = val[x]["id"] + ","
            if "children" in val[x]:
                print(name)
                if len(val[x]["children"]) > 0:
                    a.get_child_ids_recursively_list(val[x],name)
            name = ""
        final_name_list = getattr(a,"child_names_list")
        with open('.\\Results\\filename6.csv', 'wb') as myfile:
            wr = csv.writer(myfile,delimiter = ',')
            for row in final_name_list:
                wr.writerows([x.split(',') for x in row])




# import pytest, traceback, time, pdb
# from pprint import pprint
# from apptio_automation.Apptio.Json_Helpers.JsonHelpers import JsonHelpers
# from apptio_automation.Apptio.Pages.Login_page import LoginPage
# from apptio_automation.Apptio.Pages.TBMCouncil_page import TbmCouncilPage as tbmpage
# from apptio_automation.Framework.Environment_setup import ConfigValuesToDictionary
#
#
# class Test_temp:
#     def test_1_login_into_application(self, apptio_setup, function_setup):
#         # pass
#         try:
#             time.sleep(3)
#             obj_login_page = LoginPage()
#             user_name = ConfigValuesToDictionary.get_key_value('loginuser')
#             print ("user name value is {}".format(user_name))
#             pass_word = ConfigValuesToDictionary.get_key_value("loginpassword")
#             print("Password value is entered")
#             if obj_login_page.login(user_name, pass_word):
#                 pass
#                 time.sleep(5)
#             else:
#                 raise Exception("Test case filed")
#         except Exception:
#             traceback.print_stack()
#             pytest.fail("Login test case is failed")
#
#     def test_2_validate_first_column_category_values_with_given_json(self):
#         __local_app_values_list, __local_json_first_child_label_list = [], []  # app values list
#         parent = {}
#         __local_tbm_page_obj = tbmpage()
#         parent["name"] = "autum"
#         parent["id"] = 0
#         parent["children"] = []
#         id_list, value_list = __local_tbm_page_obj.check_and_get_category_values(0)
#         for x in range(0,len(id_list)):
#
#
#
#     # def test_3_validate_child_values_for_parent_with_values_displayed_in_json(self, json_data):
#     #     __local_tbm_page_obj = tbmpage()
#     #     __local_json_data_obj = JsonHelpers()
#     #     try:
#     #         col1_id_list, col1_value_list = __local_tbm_page_obj.check_and_get_category_values(0)
#     #         for x in range(0, len(col1_id_list)):
#     #             __local_tbm_page_obj.click_on_child_element(col1_id_list[x])
#     #             col2_id_list, col2_value_list = __local_tbm_page_obj.check_and_get_category_values(
#     #                 1)  # check and get child count in col2 from app
#     #             __local_col1_child1 = json_data["children"][x]
#     #             __local_json_col2_child_list = __local_json_data_obj.get_child_names_in_list(
#     #                 __local_col1_child1)  # json child count in col2
#     #             print(col1_id_list[x])
#     #             print ("length of jsonlist and app in col2 {},{}".format(str(len(__local_json_col2_child_list)),
#     #                                                                      str(len(col2_value_list))))
#     #             if __local_json_col2_child_list == col2_value_list:  # if child2 in json and app are matching
#     #                 print ('\t\t' + "col2 values from application are matching with Json")
#     #                 for y in range(0, len(col2_id_list)):
#     #                     print('\t' + col2_id_list[y])
#     #                     __local_tbm_page_obj.click_on_child_element(col2_id_list[y])  # click on child in col2
#     #                     col3_id_list, col3_value_list = __local_tbm_page_obj.check_and_get_category_values(
#     #                         2)  # check and get child count in col3 from app
#     #                     __local_col2_child = __local_col1_child1["children"][y]
#     #                     __local_json_col3_child_list = __local_json_data_obj.get_child_names_in_list(
#     #                         __local_col2_child)  # json child count in col3
#     #                     print ('\t\t\t' + "length of jsonlist and app in col3 {},{}".format(
#     #                         str(len(__local_json_col3_child_list)), str(len(col3_value_list))))
#     #                     if __local_json_col3_child_list == col3_value_list:
#     #                         print('\t\t\t' + "col3 values from application are matching with Json")
#     #                         for z in range(0, len(col3_id_list)):
#     #                             print('\t\t\t' + col3_id_list[z])
#     #                             __local_tbm_page_obj.click_on_child_element(col3_id_list[z])  # click on child in col3
#     #                             col4_id_list, col4_value_list = __local_tbm_page_obj.check_and_get_category_values(
#     #                                 3)  # check and get child count in col4 from app
#     #                             __local_col3_child = __local_col2_child["children"][z]
#     #                             __local_json_col4_child_list = __local_json_data_obj.get_child_names_in_list(
#     #                                 __local_col3_child)  # json child count in col4
#     #                             print ('\t\t\t\t' + "length of jsonlist and app in col4 {},{}".format(
#     #                                 str(len(__local_json_col4_child_list)), str(len(col4_value_list))))
#     #                             if __local_json_col4_child_list == col4_value_list:
#     #                                 pass
#     #                                 print('\t\t\t\t\t' + "col4 values from application are matching with Json")
#     #                             else:
#     #                                 if len(__local_json_col4_child_list) > len(col4_value_list):
#     #                                     pytest.fail(
#     #                                         '\t\t\t\t' + "Json data have more values than application..Please check ")
#     #                                 elif len(__local_json_col4_child_list) < len(col4_value_list):
#     #                                     pytest.fail(
#     #                                         '\t\t\t\t' + "Application values in col4 are not matching with Json")
#     #                                 else:
#     #                                     print(
#     #                                     '\t\t\t\t' + "No child present in col4 for given col3 value in Json and application")
#     #
#     #                     else:
#     #                         if len(__local_json_col3_child_list) > len(col3_value_list):
#     #                             pytest.fail("Json data have more values than application..Please check ")
#     #                         elif len(__local_json_col3_child_list) < len(col3_value_list):
#     #                             pytest.fail("Application values in col3 are not matching with Json")
#     #                         else:
#     #                             print('\t\t' + "No child present in col3 for given col2 value in Json and application")
#     #             else:
#     #                 if len(__local_json_col2_child_list) > len(col2_value_list):
#     #                     pytest.fail("Json data have more values than application..Please check")
#     #                 elif len(__local_json_col2_child_list) < len(col2_value_list):
#     #                     pytest.fail("Application values in col2 are not matching with Json")
#     #                 else:
#     #                     print("No child present in col2 for given col1 value in Json and application")
#     #         else:
#     #             print("there are no list values to run")
#     #     except Exception:
#     #         raise
#
#
#
#     def test_6_validate_service_type_for_a_given_business_unit(self):
#         obj_login_page = LoginPage()
#         obj_login_page.logout()
#         # pass
#
#
#
#
#
#
#         # def test_4_validate_category_values1(self,json_data):
#         #     __local_tbm_page_obj = tbmpage()
#         #     __local_json_data_obj = JsonHelpers()
#         #     try:
#         #         __local_app_first_child_id, __local_app_first_child_value = __local_tbm_page_obj.get_category_values_from_application("column_element_list",0)
#         #         for x in range(0,len(__local_app_first_child_id)):
#         #             __local_tbm_page_obj.click_on_child_element(__local_app_first_child_id[x])
#         #             __local_app_is_child_present_in_col2 = __local_tbm_page_obj.check_for_child_elements("column_0", 1)
#         #             print(__local_app_first_child_id[x])
#         #             if __local_app_is_child_present_in_col2:
#         #                 #print("child present in col2")
#         #                 __local_app_2_child_id_list, __local_app_2_child_value_list = __local_tbm_page_obj.get_category_values_from_application("column_element_list",1)
#         #                 for y in range(0,len(__local_app_2_child_id_list)):
#         #                     print('\t\t'+__local_app_2_child_id_list[y])
#         #                     __local_tbm_page_obj.click_on_child_element(__local_app_2_child_id_list[y])
#         #                     __local_app_is_child_present_in_col3 = __local_tbm_page_obj.check_for_child_elements("column_0", 2)
#         #                     if __local_app_is_child_present_in_col3:
#         #                         __local_app_3_child_id_list, __local_app_3_child_value_list = __local_tbm_page_obj.get_category_values_from_application("column_element_list",2)
#         #                         for z in range(0,len(__local_app_3_child_id_list)):
#         #                             print('\t\t\t' + __local_app_3_child_id_list[z])
#         #                             __local_tbm_page_obj.click_on_child_element(__local_app_3_child_id_list[z])
#         #                             __local_app_is_child_present_in_col4 = __local_tbm_page_obj.check_for_child_elements("column_0", 3)
#         #                             if __local_app_is_child_present_in_col4:
#         #                                 __local_app_4_child_id_list, __local_app_4_child_value_list = __local_tbm_page_obj.get_category_values_from_application("column_element_list",3)
#         #                                 print(__local_app_4_child_id_list)
#         #                             else:
#         #                                 print('\t\t\t' +"no child present in col4 for given col3 value")
#         #                             if z == (len(__local_app_3_child_id_list)-1):
#         #                                 #pdb.set_trace()
#         #                                 __local_tbm_page_obj.click_on_child_element(__local_app_2_child_id_list[y])
#         #                     else:
#         #                         print('\t\t'+"no child present in col3 for given col2 value")
#         #
#         #                     if y == (len(__local_app_2_child_id_list)-1):
#         #                         __local_tbm_page_obj.click_on_child_element(__local_app_first_child_id[x])
#         #
#         #             else:
#         #                 print('\t'+"no child present in col2 for given col1 value")
#         #
#         #     except Exception:
#         #         raise
