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