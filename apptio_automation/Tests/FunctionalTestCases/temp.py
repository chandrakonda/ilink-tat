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


# col1_id_list, col1_value_list = __local_tbm_page_obj.check_and_get_category_values(0)
# for x in range(0, len(col1_id_list)):
#     __local_col1_child1 = json_data["children"][x]
#     __local_tbm_page_obj.click_on_child_element(col1_id_list[x])  # click on child element
#     __local_tbm_page_obj.click_on_image_element_of_selected_category(col1_id_list[x])
#     time.sleep(1)
#     __local_tbm_page_obj.come_out_of_details_section(row_no)
#     time.sleep(1)
#     #__local_tbm_page_obj.click_on_child_element(col1_id_list[x])  # click on child element
#     col2_id_list, col2_value_list = __local_tbm_page_obj.check_and_get_category_values(1)  # check and get child count in col2 from app
#     __local_json_col2_child_list = __local_json_data_obj.get_child_names_in_list(__local_col1_child1)  # json child count in col2
#     print(col1_id_list[x])
#     # print("length of jsonlist and app in col2 {},{}".format(str(len(__local_json_col2_child_list)),str(len(col2_value_list))))
#     if __local_json_col2_child_list == col2_value_list and len(__local_json_col2_child_list) != 0 and len(col2_value_list) != 0:  # if child2 in json and app are matching
#         # print('\t\t' + "col2 values from application are matching with Json")
#         __local_tbm_page_obj.validate_children_of_each_category(col2_id_list, __local_col1_child1,2,row_no+1)
#     else:
#         if len(__local_json_col2_child_list) > len(col2_value_list):
#             pytest.fail("Json data have more values than application..Please check")
#         elif len(__local_json_col2_child_list) < len(col2_value_list):
#             pytest.fail("Application values in col2 are not matching with Json")
#         else:
#             print("No child present in col2 for given col1 value in Json and application")
# else:
#     print("there are no list values to run")


#
# @classmethod
# #def click_on_element_id_using_javascript1(cls, element_id_value):
# def click_on_element_id_in_columns(cls, element_id_value):
#     try:
#         #print(element_id_value)
#         script = "return document.getElementById('{}').getElementsByTagName('text');".format(element_id_value)
#         elements = cls.get_driver().execute_script(script)
#         browser =  cls.driver_type
#         if browser.lower() == 'firefox':
#             cls.get_driver().execute_script("arguments[0].scrollIntoView();", elements[0])
#             elements[0].click()
#         elif browser.lower() == 'chrome' or browser.lower() == "edge":
#             actions = action_chains.ActionChains(cls.get_driver())
#             actions.move_to_element_with_offset(elements[0],0,-250)
#             actions.click(elements[0]).perform()
#             __class_val = elements[0].get_attribute("class")
#             if __class_val =='atumLabel':
#                 pass
#             else:
#                 #pdb.set_trace()
#                 __tspan_elements = elements[0].find_elements_by_css_selector("tspan")
#                 if len(__tspan_elements)>1:
#                     if browser.lower() == 'chrome':
#                         #actions.move_to_element_with_offset(__tspan_elements[1],0,-250)
#                         #http://stackoverflow.com/questions/11908249/debugging-element-is-not-clickable-at-point-error
#                         cls.get_driver().execute_script(
#                             "var evt = document.createEvent('MouseEvents');" + "evt.initMouseEvent('click',true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0,null);" + "arguments[0].dispatchEvent(evt);",
#                             __tspan_elements[0])
#                         if elements[0].get_attribute("class") == 'atumLabel':
#                             pass
#                         else:
#                             cls.get_driver().execute_script(
#                                 "var evt = document.createEvent('MouseEvents');" + "evt.initMouseEvent('click',true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0,null);" + "arguments[0].dispatchEvent(evt);",
#                                 __tspan_elements[1])
#                     else:
#                         __tspan_elements[1].click()
#
#         #print("Click on element '{}' is successful ".format(element_identifier_name))
#     except webdriver_exceptions.NoSuchElementException as a:
#         raise a
#     except Exception as e:
#         raise e
# @classmethod
# def click_on_element_id_in_apptio_columns1(cls, element_id_value):
#     try:
#         # print(element_id_value)
#         get_text_elements_script = "return document.getElementById('{}').getElementsByTagName('text');".format \
#             (element_id_value)
#
#         script_edge = "return document.getElementsByClassName('details');"
#         elements = cls.get_driver().execute_script(get_text_elements_script)
#         browser = cls.driver_type
#
#         if browser.lower() == 'firefox':
#             cls.get_driver().execute_script("arguments[0].scrollIntoView();", elements[0])
#             elements[0].click()
#             script_val = "return document.getElementById('{}').getElementsByClassName('details');".format(
#                 element_id_value)
#             __elements = cls.get_driver().execute_script(script_val)
#         elif browser.lower() == 'chrome':
#             cls.get_driver().execute_script(
#                 "var evt = document.createEvent('MouseEvents');" + "evt.initMouseEvent('click',true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0,null);" + "arguments[0].dispatchEvent(evt);",
#                 elements[0])
#             script_val = "return document.getElementById('{}').getElementsByClassName('details');".format(
#                 element_id_value)
#             __elements = cls.get_driver().execute_script(script_val)
#         elif browser.lower() == "edge":
#             actions = action_chains.ActionChains(cls.get_driver())
#             actions.move_to_element_with_offset(elements[0] ,0 ,-250)
#             actions.move_to_element(elements[0])
#             actions.click(elements[0]).perform()
#             css_path = "#svgAtum_Level_0 g[id='{}'] g".format(element_id_value)
#             # pdb.set_trace()
#             __elements = cls.get_driver().find_elements_by_css_selector(css_path)
#             __class_val = elements[0].get_attribute("class")
#
#         if len(__elements) == 0:
#             __tspan_elements = elements[0].find_elements_by_css_selector("tspan")
#             if len(__tspan_elements) > 1:
#                 if browser.lower() == 'chrome':
#                     cls.get_driver().execute_script(
#                         "var evt = document.createEvent('MouseEvents');" + "evt.initMouseEvent('click',true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0,null);" + "arguments[0].dispatchEvent(evt);"
#                         ,__tspan_elements[0])
#                     script1 = "return document.getElementById('{}').getElementsByClassName('details');".format(
#                         element_id_value)
#                     __elements1 = cls.get_driver().execute_script(get_text_elements_script)
#                     if len(__elements1) == 0:
#                         cls.get_driver().execute_script(
#                             "var evt = document.createEvent('MouseEvents');" + "evt.initMouseEvent('click',true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0,null);" + "arguments[0].dispatchEvent(evt);"
#                             ,__tspan_elements[1])
#                 else:
#                     if __class_val != 'atumLabel':
#                         try:
#                             __scroll_script = "window.scrollTo({},{});".format(__tspan_elements[1].location["x"]
#                                                                                ,__tspan_elements[1].location["y"])
#                             print(__scroll_script)
#                             cls.get_driver().execute_script(__scroll_script)
#                         except Exception:
#                             pass
#                         cls.click_on_element_using_actions(__tspan_elements[1])
#
#                         # actions.move_to_element_with_offset(__tspan_elements[1],0,-250)
#                         # http://stackoverflow.com/questions/11908249/debugging-element-is-not-clickable-at-point-error
#                         # print("Click on element '{}' is successful ".format(element_identifier_name))
#     except webdriver_exceptions.NoSuchElementException as a:
#         raise a
#     except Exception as e:
#         raise e

# get_details_class_elements = ["By.Java_script","return document.getElementsByClassName('details');"]
# scroll_to_element = ["By.Java_script","arguments[0].scrollIntoView();"]

#commented on 1/7/2016############################################################################################
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
###########################################################################################################################

# def test_3_validate_child_values_for_parent_with_values_displayed_in_json(self, json_data):
#     __local_tbm_page_obj = tbmpage()
#     __local_json_data_obj = JsonHelpers()
#     try:
#         col1_id_list, col1_value_list = __local_tbm_page_obj.check_and_get_category_values(0)
#         for x in range(0, len(col1_id_list)):
#             __local_tbm_page_obj.click_on_child_element(col1_id_list[x])
#             col2_id_list,col2_value_list = __local_tbm_page_obj.check_and_get_category_values(1) # check and get child count in col2 from app
#             __local_col1_child1 = json_data["children"][x]
#             __local_json_col2_child_list = __local_json_data_obj.get_child_names_in_list(__local_col1_child1) # json child count in col2
#             print(col1_id_list[x])
#             print ("length of jsonlist and app in col2 {},{}".format(str(len(__local_json_col2_child_list)),str(len(col2_value_list))))
#             pdb.set_trace()
#             if __local_json_col2_child_list == col2_value_list and len(__local_json_col2_child_list)!= 0 and len(col2_value_list) != 0:  # if child2 in json and app are matching
#                 print ('\t\t'+"col2 values from application are matching with Json")
#                 for y in range(0,len(col2_id_list)):
#                     print('\t'+col2_id_list[y])
#                     __local_tbm_page_obj.click_on_child_element(col2_id_list[y])  # click on child in col2
#                     col3_id_list,col3_value_list = __local_tbm_page_obj.check_and_get_category_values(2) # check and get child count in col3 from app
#                     __local_col2_child = __local_col1_child1["children"][y]
#                     __local_json_col3_child_list = __local_json_data_obj.get_child_names_in_list(__local_col2_child) # json child count in col3
#                     print ('\t\t\t'+"length of jsonlist and app in col3 {},{}".format(str(len(__local_json_col3_child_list)),str(len(col3_value_list))))
#                     if __local_json_col3_child_list == col3_value_list :
#                         print('\t\t\t'+"col3 values from application are matching with Json")
#                         for z in range(0,len(col3_id_list)):
#                             print('\t\t\t'+col3_id_list[z])
#                             __local_tbm_page_obj.click_on_child_element(col3_id_list[z]) # click on child in col3
#                             col4_id_list,col4_value_list = __local_tbm_page_obj.check_and_get_category_values(3) # check and get child count in col4 from app
#                             __local_col3_child = __local_col2_child["children"][z]
#                             __local_json_col4_child_list = __local_json_data_obj.get_child_names_in_list(__local_col3_child) # json child count in col4
#                             print ('\t\t\t\t'+"length of jsonlist and app in col4 {},{}".format(str(len(__local_json_col4_child_list)),str(len(col4_value_list))))
#                             if __local_json_col4_child_list == col4_value_list :
#                                 pass
#                                 print('\t\t\t\t\t'+"col4 values from application are matching with Json")
#                             else:
#                                 if len(__local_json_col4_child_list) > len(col4_value_list):
#                                     pytest.fail('\t\t\t\t'+ "Json data have more values than application..Please check ")
#                                 elif len(__local_json_col4_child_list) < len(col4_value_list):
#                                     pytest.fail('\t\t\t\t'+"Application values in col4 are not matching with Json")
#                                 else:
#                                     print('\t\t\t\t' + "No child present in col4 for given col3 value in Json and application")
#                     else:
#                         if len(__local_json_col3_child_list) > len(col3_value_list):
#                             pytest.fail("Json data have more values than application..Please check ")
#                         elif len(__local_json_col3_child_list) < len(col3_value_list):
#                             pytest.fail("Application values in col3 are not matching with Json")
#                         else:
#                             print('\t\t' + "No child present in col3 for given col2 value in Json and application")
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

#     # pass
#     # def test_4_validate_category_values1(self,json_data):
#     #     __local_tbm_page_obj = tbmpage()
#     #     __local_json_data_obj = JsonHelpers()
#     #     try:
#     #         __local_app_first_child_id, __local_app_first_child_value = __local_tbm_page_obj.get_category_values_from_application("column_element_list",0)
#     #         for x in range(0,len(__local_app_first_child_id)):
#     #             __local_tbm_page_obj.click_on_child_element(__local_app_first_child_id[x])
#     #             __local_app_is_child_present_in_col2 = __local_tbm_page_obj.check_for_child_elements("column_0", 1)
#     #             print(__local_app_first_child_id[x])
#     #             if __local_app_is_child_present_in_col2:
#     #                 #print("child present in col2")
#     #                 __local_app_2_child_id_list, __local_app_2_child_value_list = __local_tbm_page_obj.get_category_values_from_application("column_element_list",1)
#     #                 for y in range(0,len(__local_app_2_child_id_list)):
#     #                     print('\t\t'+__local_app_2_child_id_list[y])
#     #                     __local_tbm_page_obj.click_on_child_element(__local_app_2_child_id_list[y])
#     #                     __local_app_is_child_present_in_col3 = __local_tbm_page_obj.check_for_child_elements("column_0", 2)
#     #                     if __local_app_is_child_present_in_col3:
#     #                         __local_app_3_child_id_list, __local_app_3_child_value_list = __local_tbm_page_obj.get_category_values_from_application("column_element_list",2)
#     #                         for z in range(0,len(__local_app_3_child_id_list)):
#     #                             print('\t\t\t' + __local_app_3_child_id_list[z])
#     #                             __local_tbm_page_obj.click_on_child_element(__local_app_3_child_id_list[z])
#     #                             __local_app_is_child_present_in_col4 = __local_tbm_page_obj.check_for_child_elements("column_0", 3)
#     #                             if __local_app_is_child_present_in_col4:
#     #                                 __local_app_4_child_id_list, __local_app_4_child_value_list = __local_tbm_page_obj.get_category_values_from_application("column_element_list",3)
#     #                                 print(__local_app_4_child_id_list)
#     #                             else:
#     #                                 print('\t\t\t' +"no child present in col4 for given col3 value")
#     #                             if z == (len(__local_app_3_child_id_list)-1):
#     #                                 #pdb.set_trace()
#     #                                 __local_tbm_page_obj.click_on_child_element(__local_app_2_child_id_list[y])
#     #                     else:
#     #                         print('\t\t'+"no child present in col3 for given col2 value")
#     #
#     #                     if y == (len(__local_app_2_child_id_list)-1):
#     #                         __local_tbm_page_obj.click_on_child_element(__local_app_first_child_id[x])
#     #
#     #             else:
#     #                 print('\t'+"no child present in col2 for given col1 value")
#     #
#     #     except Exception:
#     #         raise