"""
Page : TBM Council page
"""
from apptio_automation.Framework.Extensions.Webdriveractions_extensions import ElementExtensions as element
import json,time,pdb,pytest,logging
from apptio_automation.Apptio.Json_Helpers.JsonHelpers import JsonHelpers
from apptio_automation.Apptio.Pages.Categorydetails_page import CategoryDetailsPage
import apptio_automation.Framework.Extensions.Custom_logger as  cl
#from apptio_automation.Apptio.Common.Apptio_Common import write_child_results

class TbmCouncilPage(element,JsonHelpers):
    log = cl.customLogger(logging.DEBUG)

    categorydetailspageobject = CategoryDetailsPage()
    col1_parent_name = None
    child_validation_results = []
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


    def come_out_of_details_section(self,row_no):
        try:
            self.click_on_element_format("come_out_of_details", row_no)
        except:
            raise

    def check_image_for_category(self,child_id):
        try:
            __is_displayed =element.is_element_displayed_format("image_element",child_id)
        except:
            raise
        return __is_displayed


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

    def check_for_public_cloud_in_application_and_json(self, json_object, col_id_value): # need to return only one value
        __jsonhelp = JsonHelpers()
        __cloud_json = __jsonhelp.check_for_public_cloud_in_json(json_object) # check json
        __cloud_app = element.is_element_displayed_format("cloud_image_element", col_id_value)

        if __cloud_json and __cloud_app:
            return True
        elif not __cloud_json and not __cloud_app:
            return True
        else:
            return False

################################3#######################################################################################
# Function to validate images and children for each category
################################3#######################################################################################

    def validate_cloud_details_images_and_children_for_category(self,json_data,col1_id_list):
        image_col_no = 0
        col_no = 0
        try:
            #col1_id_list, col1_value_list = self.check_and_get_category_values(col_no)
            self.validate_image_and_children(col1_id_list, json_data, col_no+1, image_col_no)
        except:
            raise

    def validate_image_and_children(self,col1_id_list,json_data,col_no,image_col_no):
        try:
            for x in range(0, len(col1_id_list)):
                __dic_ = {}
                __local_col1_child1 = json_data["children"][x]
                keyval = col1_id_list[x][4:]

                self.click_on_child_element(col1_id_list[x])  # click on child element
                ###################################################################################

                imagepresent =  self.check_image_for_category(col1_id_list[x])

                cloudimage = self.check_for_public_cloud_in_application_and_json(__local_col1_child1, col1_id_list[x])  # check for cloud image

                ###################################################################################
                ## Click on on next child item
                col2_id_list, col2_value_list = self.check_and_get_category_values(col_no)  # check and get child count in col2 from app
                __local_json_col2_child_list = self.get_child_names_in_list(__local_col1_child1)  # json child count in col2

                if self.check_count_of_children_in_json_app(__local_json_col2_child_list,col2_value_list) : #__local_json_col2_child_list == col2_value_list and len(__local_json_col2_child_list) != 0 and len(col2_value_list) != 0  # if child2 in json and app are matching
                    childlist = __local_json_col2_child_list
                    Childrenmatching = True
                    if Childrenmatching and cloudimage and imagepresent:
                        finalstatus = "Pass"
                    else:
                        finalstatus = "Fail"
                    __dic_ = self.add_values_to_dic(keyval=keyval,imagepresent=imagepresent,cloud=cloudimage,childrenmatching=Childrenmatching,finalstatus=finalstatus
                                                     ,child_list=childlist)
                    TbmCouncilPage.child_validation_results.append(__dic_)
                    #self.validate_image_and_children(col2_id_list, __local_col1_child1, col_no+1, image_col_no + 1)
                else:
                    self.compare_json_app_child_counts_in_else(__local_json_col2_child_list,col2_value_list,imagepresent,cloudimage,keyval)
        except:
            raise

    def check_count_of_children_in_json_app(self,__local_json_col2_child_list,col2_value_list):
       if __local_json_col2_child_list == col2_value_list and len(__local_json_col2_child_list) != 0 and len(col2_value_list) != 0: # if child2 in json and app are matching
           return True
       else:
           return False

    def compare_json_app_child_counts_in_else(self,__local_json_col2_child_list,col2_value_list,imagepresent,cloudimage,keyvalue):
        __child = None
        if len(__local_json_col2_child_list) > len(col2_value_list):
            __child = "Json children count is more than application children count"
            childmatching = False
            self.log.error(__local_json_col2_child_list + " " + col2_value_list)
        elif len(__local_json_col2_child_list) < len(col2_value_list):
            __child = "Application children count is more than json children count"
            childmatching = False
            self.log.error(__local_json_col2_child_list + " " + col2_value_list)
        else:
            __child = "No children present in json and application"
            childmatching = True

        if childmatching and imagepresent and cloudimage:
            finalstatus = "Pass"
        else:
            finalstatus = "Fail"
        __dic_ = self.add_values_to_dic(keyval=keyvalue,imagepresent=imagepresent,cloud=cloudimage,childrenmatching=childmatching,finalstatus=finalstatus,child_list=__child)
        TbmCouncilPage.child_validation_results.append(__dic_)
    #
    # def add_values_to_dic(self,val1,val2,val3,__dic_,child_list=None):
    #     __dic_["Key_value"] = val1
    #     __dic_["Imagepresent"] = val1
    #     __dic_["Cloudimagepresent"] = val2
        return __dic_

    def add_values_to_dic(self,keyval,imagepresent,cloud,childrenmatching,finalstatus,child_list=None):
        __dic_ = {}
        __dic_["Key_value"] = keyval
        __dic_["Imagepresent"] = imagepresent
        __dic_["Cloudimagepresent"] = cloud
        __dic_["Childlist"] = child_list
        __dic_["Childrenmatching"] = childrenmatching
        __dic_["FinalStatus"] = finalstatus
        return __dic_

########################################################################################################################
# Functions to validate details for each category
################################3#######################################################################################

    def validate_details_of_each_category_in_columns(self,json_data,col1_id_list,col1_value_list):
        try:
            image_column_no = 0
            #col1_id_list, col1_value_list = self.check_and_get_category_values(0)
            for x in range(0, len(col1_id_list)):
                __local_col1_child1 = json_data["children"][x]
                self.click_on_child_element(col1_id_list[x])  # click on child element
                TbmCouncilPage.col1_parent_name = col1_value_list[x]
                col2_id_list, col2_value_list = self.check_and_get_category_values(1)  # check and get child count in col2 from application
                self.click_on_image_element_of_selected_category(col1_id_list[x])
                time.sleep(1)
                self.categorydetailspageobject.compare_app_json_details_data(__local_col1_child1,col1_id_list[x][4:],TbmCouncilPage.col1_parent_name)
                self.come_out_of_details_section(image_column_no)
                #time.sleep(1)
                if len(col2_value_list) != 0:  # if child are present
                    #self.validate_details_of_children(col2_id_list, __local_col1_child1,2,image_column_no+1)
                    pass
            else:
                print("there are no list values to run")
        except Exception as e:
            #self.log.exception("Exception #####  {} ".format(e))
            raise

    def validate_details_of_children(self, col1_id_list, json_data_obj,child_col_no,image_col_no):
        try:
            for x in range(0, len(col1_id_list)):
                print(col1_id_list[x])
                __local_col1_child = json_data_obj["children"][x]
                self.click_on_child_element(col1_id_list[x])
                self.click_on_image_element_of_selected_category(col1_id_list[x])
                time.sleep(1)
                __parent_name = TbmCouncilPage.col1_parent_name
                self.categorydetailspageobject.compare_app_json_details_data(__local_col1_child,col1_id_list[x][4:],__parent_name,"details")
                self.come_out_of_details_section(image_col_no)
                col_id_list, col_value_list = self.check_and_get_category_values(child_col_no)  # check and get child count in col2 from app
                if len(col_value_list) != 0:  # if child2 in json and app are matching
                    self.validate_details_of_children(col_id_list, __local_col1_child, child_col_no+1,image_col_no+1)
                #pass
        except:
            raise

########################################################################################################################
# Functions to validate exclude and include details for each category
################################3#######################################################################################

    def validate_exclude_and_include_of_each_category(self, json_data,col1_id_list,col1_value_list):
        try:
            image_column_no = 0
            #col1_id_list, col1_value_list = self.check_and_get_category_values(0)
            for x in range(0, len(col1_id_list)):
                __local_col1_child1 = json_data["children"][x]
                self.click_on_child_element(col1_id_list[x])  # click on child element
                TbmCouncilPage.col1_parent_name = col1_value_list[x]
                col2_id_list, col2_value_list = self.check_and_get_category_values(1)  # check and get child count in col2 from application
                self.click_on_image_element_of_selected_category(col1_id_list[x])
                time.sleep(1)
                self.categorydetailspageobject.compare_exclude_and_include_in_app_and_json(__local_col1_child1, col1_id_list[x][4:], TbmCouncilPage.col1_parent_name)
                self.come_out_of_details_section(image_column_no)
                # time.sleep(1)
                if len(col2_value_list) != 0:  # if child are present
                   # self.validate_exclude_and_include_of_children(col2_id_list, __local_col1_child1,2,image_column_no+1)
                    pass
            else:
                print("there are no list values to run")
        except Exception as e:
            # self.log.exception("Exception #####  {} ".format(e))
            raise

    def validate_exclude_and_include_of_children(self, col1_id_list, json_data_obj, n,row_no):
        for x in range(0, len(col1_id_list)):
            print(col1_id_list[x])
            __local_col1_child = json_data_obj["children"][x]
            self.click_on_child_element(col1_id_list[x])
            col_id_list, col_value_list = self.check_and_get_category_values(n)  # check and get child count in col2 from app
            __local_json_col_child_list = self.get_child_names_in_list(__local_col1_child)  # json child count in col2
            self.click_on_image_element_of_selected_category(col1_id_list[x])
            time.sleep(1)
            self.categorydetailspageobject.compare_exclude_and_include_in_app_and_json(__local_col1_child,
                                                                                       col1_id_list[x][4:],
                                                                                       TbmCouncilPage.col1_parent_name)
            self.come_out_of_details_section(row_no)
            if len(col_value_list) != 0:  # if child2 in json and app are matching
                self.validate_exclude_and_include_of_children(col_id_list, __local_col1_child, n + 1,row_no+1)
            else:
                if len(__local_json_col_child_list) > len(col_value_list):
                    pytest.fail("Json data have more values than application..Please check ")
                elif len(__local_json_col_child_list) < len(col_value_list):
                    pytest.fail("Application values in col3 are not matching with Json")
                else:
                    print('\t\t' + "No child present for a given value in Json and application")

# def validate_description_values(self,col1_id_list,json_data_obj,n):
#     for x in range(0, len(col1_id_list)):
#         print (col1_id_list[x])
#         __local_col1_child = json_data_obj["children"][x]
#         self.click_on_child_element(col1_id_list[x])
#
#         col_id_list, col_value_list = self.check_and_get_category_values(n)  # check and get child count in col2 from app
#         __local_json_col_child_list = self.get_child_names_in_list(__local_col1_child)  # json child count in col2
#
#         #print("length of jsonlist and app in col2 {},{}".format(str(len(__local_json_col_child_list)),str(len(col_value_list))))
#         if __local_json_col_child_list == col_value_list and len(__local_json_col_child_list) != 0 and len(col_value_list) != 0:  # if child2 in json and app are matching
#             self.validate_col_values(col_id_list,__local_col1_child,n+1)
#         else:
#             if len(__local_json_col_child_list) > len(col_value_list):
#                 pytest.fail("Json data have more values than application..Please check ")
#             elif len(__local_json_col_child_list) < len(col_value_list):
#                 pytest.fail("Application values in col3 are not matching with Json")
#             else:
#                 print('\t\t' + "No child present for a given value in Json and application")
