from apptio_automation.Framework.Extensions.Webdriverwait_extensions import WaitExtensions
from apptio_automation.Framework.Environment_setup import EnvironmentSetup as  Env_setup
import selenium.common.exceptions as webdriver_exceptions
from apptio_automation.Framework.Environment_setup import PageElements as Page_elements
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common import action_chains
from selenium.webdriver.remote import webelement
import pdb , time , logging
from datetime import datetime
import apptio_automation.Framework.Extensions.Custom_logger as  cl


import traceback
class ElementExtensions(Page_elements,WaitExtensions,Env_setup):
    log = cl.customLogger(logging.DEBUG)
    @classmethod
    def get_web_element(cls,element_identifier_name):
        try:
            by = Page_elements().get_element_identifier(element_identifier_name)
            by = eval(by)
            __obj_wait = WaitExtensions()
            __element = __obj_wait.Wait_for_element_visible(by, 1)
            cls.log.info(" '{}' Element is identified".format(element_identifier_name))
            return __element
            #return __obj_wait.Wait_for_element_visible(by,10) #  cls.Wait_for_element_visible()
        except webdriver_exceptions.NoSuchElementException as e:
            cls.log.exception("Exception thrown in 'get_web_element' method '{}' ".format(e))
            raise
        except webdriver_exceptions.WebDriverException as e:
            cls.log.exception("Exception thrown in 'get_web_element' method '{}' ".format(e))
            raise

    @classmethod
    def get_web_element_format(cls, element_identifier_name,value_to_format):
        try:
            __obj_wait_extensions = WaitExtensions()
            by = Page_elements().get_element_identifier(element_identifier_name)
            by = eval(by)
            __val2 = by[1]
            if value_to_format == None :
                pass
            else:
                by[1] = __val2.format(value_to_format)
            return __obj_wait_extensions.Wait_for_element_visible(by, 10)
        except webdriver_exceptions.NoSuchElementException as e:
            cls.log.exception("Exception thrown in 'get_web_element_format' method '{}' ".format(e))
            raise
        except webdriver_exceptions.WebDriverException as e:
            cls.log.exception("Exception thrown in 'get_web_element_format' method '{}' ".format(e))
            raise

    @classmethod
    def get_elements_in_list(cls, element_identifier_name, value_to_format=None):
        cls.log.info("Enter 'get_elements_in_list' method")
        try:
            by = Page_elements().get_element_identifier(element_identifier_name)
            by = eval(by)
            if value_to_format != None:
                __val2 = by[1]
                by[1] = __val2.format(value_to_format)
            elements = cls.get_driver().find_elements(eval(by[0]), by[1])
            return elements
        except webdriver_exceptions.NoSuchElementException as e:
            cls.log.exception("Exception thrown in 'get_elements_in_list' method {}".format(e))
            raise
        except Exception as g:
            cls.log.exception("Exception thrown in 'get_elements_in_list' method {}".format(g))
            raise

    ##############################

    ##############################

    @classmethod
    def set_text(cls,element_identifier_name,text_to_be_entered):
        try:
            local_element = cls.get_web_element(element_identifier_name)
            local_element.clear()
            local_element.send_keys(text_to_be_entered)
            cls.log.info("Input text '{}' in the field '{}' is successful ".format(text_to_be_entered,element_identifier_name))
        except webdriver_exceptions.NoSuchElementException as k:
            cls.log.exception("Exception thrown in 'set_text' method '{}' ".format(k))
            raise k
        except Exception as c:
            cls.log.exception("Exception thrown in 'set_text' method '{}' ".format(c))
            raise c

    @classmethod
    def get_text(cls,element_identifier_name):
        __var_val = None
        try:
            local_element = cls.get_web_element(element_identifier_name)
            __var_val = local_element.text
            cls.log.info("Value returned from the application is '{}'".format(__var_val))
            return __var_val
        except webdriver_exceptions.NoSuchElementException as e:
            cls.log.exception("Exception thrown in 'get_text' method '{}' ".format(e))
            raise e
        except Exception as c:
            cls.log.exception("Exception thrown in 'get_text' method '{}' ".format(c))
            raise c
    @classmethod
    def get_text_in_list(cls, element_identifier_name,format_value=None):
        __var_val = []
        try:
            local_element = cls.get_elements_in_list(element_identifier_name,format_value)
            for ele in local_element: # for each element in the list
                __var_val.append(ele.text)  # get the text of the element
            cls.log.info("Value returned from the application is '{}'".format(str(len(__var_val))))
            return __var_val
        except webdriver_exceptions.NoSuchElementException as e:
            cls.log.exception("Exception thrown in 'get_text' method '{}' ".format(e))
            raise e
        except Exception as c:
            cls.log.exception("Exception thrown in 'get_text' method '{}' ".format(c))
            raise c

    @classmethod
    def get_text_for_given_element(cls,web_element):
        try:
            __var_val = web_element.text
            cls.log.info("Value returned from the application is '{}'".format(__var_val))
            return __var_val
        except webdriver_exceptions.NoSuchElementException as e:
            cls.log.exception("Exception thrown in 'get_text_for_given_element' method '{}' ".format(e))
            raise e
        except Exception as c:
            cls.log.exception("Exception thrown in 'get_text_for_given_element' method '{}' ".format(c))
            raise c

    @classmethod
    def get_innerHtml_for_given_element(cls,web_element):
        try:
            __var_val = cls.get_driver().execute_script("return $(arguments[0]).text()",web_element)
            cls.log.info("Value returned from the application is '{}'".format(__var_val))
            return __var_val
        except webdriver_exceptions.NoSuchElementException as e:
            cls.log.exception("Exception thrown in 'get_innerHtml_for_given_element' method '{}' ".format(e))
            raise e
        except Exception as c:
            cls.log.exception("Exception thrown in 'get_innerHtml_for_given_element' method '{}' ".format(c))
            raise c

    @classmethod
    def get_innerHtml(cls, element_identifier_name):
        try:
            local_element = cls.get_web_element(element_identifier_name)
            __var_val = cls.get_driver().execute_script("return $(arguments[0]).innerHTML", local_element)
            cls.log.info("Value returned from the application is '{}' for web element '{}'".format(__var_val,element_identifier_name))
            return __var_val
        except webdriver_exceptions.NoSuchElementException as e:
            cls.log.exception("Exception thrown in 'get_innerHtml_for_given_element' method '{}' ".format(e))
            raise e
        except Exception as c:
            cls.log.exception("Exception thrown in 'get_innerHtml_for_given_element' method '{}' ".format(c))
            raise c



    @classmethod
    def click_on_element_format(cls,element_identifier_name,value_to_format=None):
        try:
            __obj_wait_extension = WaitExtensions()
            by = Page_elements().get_element_identifier(element_identifier_name)
            by = eval(by)
            __val2 = by[1]
            if value_to_format != None :
                by[1] = __val2.format(value_to_format)
                cls.log.info("Formatted value for the element '{}' is {}".format(element_identifier_name,by[1]))
            element = __obj_wait_extension.Wait_for_element_visible(by,10)
            if element != False:
                #element = cls.get_driver().find_element(eval(by[0]), by[1])  # find element
                # action_chains.ActionChains(Env_setup.get_driver()).move_to_element(element).perform()  #scroll to element
                # element.click() # click on element
                browser = cls.driver_type
                cls.click_on_element_based_on_browser(browser,element)
                cls.log.info("Click on element '{}' is successful ".format(element_identifier_name))
            else:
                cls.log.info("Element '{}' is not identified ".format(element_identifier_name))
        except webdriver_exceptions.NoSuchElementException as b:
            cls.log.exception("Exception thrown while finding element '{}' in 'click_on_element_format' method".format(element_identifier_name))
            raise b
        except Exception as f:
            raise f

    @classmethod
    def click_on_element_based_on_browser(cls,browser,web_element):
        try:
            if browser.lower() == 'firefox':
                web_element.click()
            elif browser.lower() == 'chrome':
                cls.get_driver().execute_script(
                    "var evt = document.createEvent('MouseEvents');" + "evt.initMouseEvent('click',true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0,null);" + "arguments[0].dispatchEvent(evt);",
                    web_element)
            elif browser.lower() == "edge":
                actions = action_chains.ActionChains(cls.get_driver())
                actions.move_to_element_with_offset(web_element, 0, -250)
                actions.move_to_element(web_element)
                actions.click(web_element).perform()
        except:
            raise

    @classmethod
    def click_on_element_format_javascript(cls, element_identifier_name, value_to_format=None):
        try:
            by = Page_elements().get_element_identifier(element_identifier_name)
            by = eval(by)
            __val2 = by[1]
            if value_to_format == None:
                pass
            else:
                by[1] = __val2.format(value_to_format)
            script = "return $('"+by[1]+"').get(0);"
            element_obj = cls.get_driver().execute_script(script)
            cls.click_on_element_using_actions(element_obj)
            cls.log.exception("Click on element using java script '{}' ".format(script))
        except webdriver_exceptions.NoSuchElementException as b:
            cls.log.exception("Exception thrown in 'click_on_element_format_javascript' method '{}' ".format(b))
            raise b
        except Exception as f:
            cls.log.exception("Exception thrown in 'click_on_element_format_javascript' method '{}' ".format(f))
            raise f
            #cls.get_driver().execute_script("arguments[0].scrollIntoView(true);", element_obj)
            #cls.get_driver().execute_script('window.scrollTo(0, '+ str(element_obj.location['y'])+ ');')

    @classmethod
    def click_on_element(cls,element_identifier_name):
        try:
            local_element = cls.get_web_element(element_identifier_name)
            if cls.driver_type.lower() != 'firefox':
                action_chains.ActionChains(Env_setup.get_driver()).move_to_element(local_element).perform()
            local_element.click()
            cls.log.info("Click on element '{}' is successful ".format(element_identifier_name))
            #print
        except webdriver_exceptions.NoSuchElementException as b:
            cls.log.exception("Exception thrown in 'click_on_element' method '{}' ".format(b))
            raise b
        except Exception as f:
            cls.log.exception("Exception thrown in 'click_on_element' method '{}' ".format(f))
            raise f

    @classmethod
    def click_on_element_using_javascript(cls, element_identifier_name):
        try:
            # print ("field is present in the application")
            element = cls.get_web_element(element_identifier_name)
            Env_setup.get_driver().execute_script("$(arguments[0]).click();", element)
            cls.log.info("Click on element '{}' is successful ".format(element_identifier_name))
        except webdriver_exceptions.NoSuchElementException as a:
            cls.log.exception("Exception thrown in 'click_on_element' method '{}' ".format(a))
            raise a
        except Exception as e:
            cls.log.exception("Exception thrown in 'click_on_element' method '{}' ".format(e))
            raise e


# actions.move_to_element_with_offset(__tspan_elements[1],0,-250)
# http://stackoverflow.com/questions/11908249/debugging-element-is-not-clickable-at-point-error
# print("Click on element '{}' is successful ".format(element_identifier_name))
##
    @classmethod
    def click_on_element_id_in_apptio_columns(cls, element_id_value):
        try:
            category_element = cls.get_web_element_format("category_text_element",element_id_value)
            image_element_for_selected_category = "g[id='{}'] g".format(element_id_value)
            browser = cls.driver_type
            cls.click_on_element_based_on_browser(browser, category_element)
            __val1 = "g[id='{}'] rect".format(element_id_value)
            __element_class_value = cls.get_driver().find_element_by_css_selector(__val1).get_attribute("class")
            cls.log.info("Attribute value of the class is '{}'".format(__element_class_value))
            if __element_class_value != 'atumRectSelected':
                __tspan_elements = category_element.find_elements_by_css_selector("tspan")
                if len(__tspan_elements) > 1:
                    if browser.lower() == 'chrome':
                        cls.get_driver().execute_script(
                            "var evt = document.createEvent('MouseEvents');" + "evt.initMouseEvent('click',true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0,null);" + "arguments[0].dispatchEvent(evt);",
                            __tspan_elements[0])
                        __element_class_value1 = cls.get_driver().find_element_by_css_selector(__val1).get_attribute("class")
                        if __element_class_value1 != 'atumRectSelected':
                            cls.get_driver().execute_script(
                                "var evt = document.createEvent('MouseEvents');" + "evt.initMouseEvent('click',true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0,null);" + "arguments[0].dispatchEvent(evt);",
                                __tspan_elements[1])
                    else:
                        __scroll_script = "window.scrollTo({},{});".format(__tspan_elements[1].location["x"], __tspan_elements[1].location["y"])
                        cls.get_driver().execute_script(__scroll_script)
                        cls.click_on_element_using_actions(__tspan_elements[1])

        except webdriver_exceptions.NoSuchElementException as a:
            cls.log.exception("Exception thrown in 'click_on_element_id_in_apptio_columns1' method '{}' ".format(a))
            raise a
        except Exception as e:
            cls.log.exception("Exception thrown in 'click_on_element_id_in_apptio_columns1' method '{}' ".format(e))
            raise e

    # select check box
    @classmethod
    def select_check_box_format(cls, element_identifier_name,state,value_to_format):
        is_selected = False
        try:
            __obj_wait_extension = WaitExtensions()
            by = Page_elements().get_element_identifier(element_identifier_name)
            by = eval(by)
            __val2 = by[1]
            if value_to_format == None : # check if there is an option to format
                pass
            else:
                by[1] = __val2.format(value_to_format)

            if (__obj_wait_extension.Wait_for_element_visible(by, 10)):
                ele = Env_setup.get_driver().find_element(eval(by[0]), by[1])
                action_chains.ActionChains(Env_setup.get_driver()).move_to_element(ele).perform()
                if (state.upper() == "ON"):
                    if ele.is_selected() :
                        cls.log.info("Check box selection is successful '{}'".format(element_identifier_name))
                        is_selected = True
                    else:
                        ele.click()          # if check box is not selected, then select
                        is_selected = True
                else:                       # to un select check box
                    ele.click()
                    cls.log.info("Check box is unselected {}".format(element_identifier_name))
        except webdriver_exceptions.NoSuchElementException as e:
            cls.log.exception("Exception thrown in 'select_check_box_format' method '{}' ".format(e))
            raise e
        except Exception as a:
            cls.log.exception("Exception thrown in 'select_check_box_format' method '{}' ".format(a))
            raise a
        cls.log.exception("Value of 'is_selected' is '{}' ".format(is_selected))
        return is_selected

    # Select methods
    @classmethod
    def select_element_by_value(cls,element_identifier_name,value_tobe_selected):
        try:
            local_element = cls.get_web_element(element_identifier_name)
            Select(local_element).select_by_value(value_tobe_selected)
            cls.log.info(" Value '{}' is selected in the drop down '{}'".format(value_tobe_selected,element_identifier_name))
        except webdriver_exceptions.NoSuchElementException as e:
            cls.log.exception("Exception thrown in 'select_check_box_format' method '{}' ".format(e))
            raise e
        except Exception as a:
            cls.log.exception("Exception thrown in 'select_check_box_format' method '{}' ".format(a))
            raise a

    @classmethod
    def select_element_by_id(cls, element_identifier_name, value_tobe_selected):
        try:
            local_element = cls.get_web_element(element_identifier_name)
            Select(local_element).select_by_index(value_tobe_selected)
            cls.log.info(
                " Value '{}' is selected in the drop down '{}'".format(value_tobe_selected, element_identifier_name))
        except webdriver_exceptions.NoSuchElementException as e:
            cls.log.exception("Exception thrown in 'select_element_by_id' method '{}' ".format(e))
            raise e
        except Exception as e:
            cls.log.exception("Exception thrown in 'select_element_by_id' method '{}' ".format(e))
            raise e

    @classmethod
    def get_selected_value_from_drop_down(cls,element_identifier_name):
        try:
            local_element = cls.get_web_element(element_identifier_name)
            __val = Select(local_element).first_selected_option
            cls.log.info(
                "Value from the drop down is '{}' ".format(element_identifier_name))
        except webdriver_exceptions.NoSuchElementException as e:
            cls.log.exception("Exception thrown in 'get_selected_value_from_drop_down' method '{}' ".format(e))
            raise e
        except Exception as a:
            cls.log.exception("Exception thrown in 'get_selected_value_from_drop_down' method '{}' ".format(a))
            raise a
        return __val

    #
    # @classmethod
    # def get_all_options_in_drop_down(cls, web_element_name):
    #     option_text_list = []
    #     try:
    #         local_element = cls.get_web_element(web_element_name)
    #         select = Select(local_element)
    #         for option in select.options:
    #                 #print (option.text)
    #             option_text_list.append(option.text)
    #         print ("count of options is {}".format(str(len(option_text_list))))
    #         return option_text_list
    #     except webdriver_exceptions.NoSuchElementException as a:
    #         raise a
    #     except Exception as e:
    #         raise e

    @classmethod
    def click_on_menu(cls,element_identifier_name):
        element = cls.get_web_element(element_identifier_name)
        action_chains.ActionChains(Env_setup.get_driver()).move_to_element(element).perform()
        cls.log.info("Click on menu item '{}'".format(element_identifier_name))

    @classmethod
    def scroll_to_element(cls,element_identifier_name):
        element = cls.get_web_element(element_identifier_name)
        action_chains.ActionChains(Env_setup.get_driver()).move_to_element(element).perform()
        cls.log.info("Scroll to element '{}'".format(element_identifier_name))

    @classmethod
    def wait_for(cls,element_identifier_name):
        try:
            element = cls.get_web_element(element_identifier_name)
            __obj_wait = WaitExtensions()
            cls.log.info("Waiting for the object.... '{}'".format(element_identifier_name))
            if __obj_wait.Wait_for_element(element,10):
                pass
            else:
                raise webdriver_exceptions.NoSuchElementException
        except Exception as e:
            cls.log.exception("Exception thrown in 'Wait_for' method '{}'".format(e))
            raise e

    @classmethod
    def close_browser(cls):
        Env_setup.get_driver().close()

    def refresh_page(self):
        Env_setup.get_driver().refresh()

    @classmethod
    def get_current_window_handle(cls,handle_number):
        return Env_setup.get_driver().window_handles[handle_number]

    @classmethod
    def switch_to_give_window_handle(cls,window_handle):
        Env_setup.get_driver().switch_to.window(window_handle)

    @classmethod
    def is_element_displayed(cls,element_identifier_name):
        try:
            element = cls.get_web_element(element_identifier_name)
            cls.log.info("Element is displayed so returning True")
            return element.is_displayed()
        except Exception:
            cls.log.exception("Element is not displayed so returning False")
            return False

    @classmethod
    def is_element_displayed_format(cls,element_identifier_name,value_to_format = None):
        cls.log.info("Enter 'is_element_displayed_format' method")
        try:
            by = Page_elements().get_element_identifier(element_identifier_name)
            by = eval(by)
            __val2 = by[1]
            if value_to_format == None :
                cls.log.info("Identifier value is..".format(__val2))
            else:
                by[1] = __val2.format(value_to_format)
                cls.log.info("Formatted value of the by is '{}' ".format(by[1]))
            element = cls.get_driver().find_element(eval(by[0]), by[1])
            __is_displayed =  element.is_displayed()
            cls.log.info("'Is displayed' value of '{}' is '{}'".format(element_identifier_name,__is_displayed))
            return __is_displayed
        except Exception:
            cls.log.exception("Element is not displayed so returning False")
            return False

    @classmethod
    def is_element_enabled(cls,element_identifier_name):
        try:
            element = cls.get_web_element(element_identifier_name)
            return element.is_enabled()
        except Exception:
            cls.log.info("Element is not enabled so returning False")
            return False
    @classmethod
    def get_attribute_value(cls,element_identifier_name,attribute_name):
        try:
            element = cls.get_web_element(element_identifier_name)
            __val=  element.get_attribute(attribute_name)
            #cls.log.info("Attribute value of the element is '{}' ".format(__val))
            return __val
        except Exception as e:
            cls.log.exception("Exception thrown while getting attribute value for an element {}".format(e))
            raise

    @classmethod
    def get_attribute_value_of_element(cls,web_element,attribute_name):
        try:
            return web_element.get_attribute(attribute_name)
        except Exception as e:
            cls.log.exception("Exception thrown in 'get_attribute_value_of_element' method {}".format(e))
            raise

    @classmethod
    def get_attribute_values_in_list(cls, element_identifier_name,attribute_name,value_to_format):
        __local_value_list = []
        try:
            by = Page_elements().get_element_identifier(element_identifier_name)
            by = eval(by)
            __val2 = by[1]
            if value_to_format != None :
                by[1] = __val2.format(value_to_format)
                elements = cls.get_driver().find_elements(eval(by[0]),by[1])
                for element in elements:
                    __local_value_list.append(element.get_attribute(attribute_name))
            return __local_value_list
        except webdriver_exceptions.NoSuchElementException as e:
            cls.log.exception("Exception thrown in 'get_attribute_value_of_element' method {}".format(e))
            raise
        except Exception as e:
            cls.log.exception("Exception thrown in 'get_attribute_value_of_element' method {}".format(e))
            raise



    @classmethod
    def click_on_element_using_actions(cls,web_element):
        cls.log.info("Enter 'click_on_element_using_actions' method")
        actions = action_chains.ActionChains(cls.get_driver())
        actions.move_to_element(web_element)
        actions.click(web_element).perform()

    @classmethod
    def move_with_offset_and_click_on_element_using_actions(cls, web_element):
        cls.log.info("Enter 'move_with_offset_and_click_on_element_using_actions' method")
        actions = action_chains.ActionChains(cls.get_driver())
        actions.move_to_element_with_offset(web_element, 0, -250)
        actions.click(web_element).perform()
        #__class_val = web_element.get_attribute("class")


    # @classmethod
    # def get_attribute_value_in_list1(cls,element,attribute_name):
    #     __local_value_list = []
    #     elements = []
    #     try:
    #         elements = element.find_elements("By.XPATH","/g")
    #         print (len(elements))
    #         for element in elements:
    #             __local_value_list.append(element.get_attribute('id'))
    #         print(len(__local_value_list))
    #         return __local_value_list
    #     except webdriver_exceptions.NoSuchElementException:
    #         raise
    #     except Exception:
    #         raise



##########################Autforms specific########################################
    @classmethod
    def get_preceding_sibling_count_ingrid_byXpath(cls,element_identifier_name,col_name = None):

        try:
            by = Page_elements().get_element_identifier(element_identifier_name)
            by = eval(by)
            __val2 = by[1]
            if col_name == None :
                __val1 = __val2
            else:
                __val1 = __val2.format(col_name)
            print ("Formated column xpath value is '{}'".format(__val1))
            __element_list = []
            __element_list = cls.get_driver().find_elements_by_xpath(__val1)
            return __element_list.__len__()
        except webdriver_exceptions.NoSuchElementException as e:
            raise e

    def get_column_value(self,element_identifier_name,index_value):
        try:
            by = Page_elements().get_element_identifier(element_identifier_name)
            by = eval(by)
            __val1 = by[1].format(index_value)
            #print (__val1)
            #element = Env_setup.get_driver().find_element(eval(by[0]), str(__val1))
            element = Env_setup.get_driver().find_element_by_xpath(__val1)
            action_chains.ActionChains(Env_setup.get_driver()).move_to_element(element).perform()
            return element.text
        except webdriver_exceptions.NoSuchElementException as e:
            #traceback.print_exc()
            raise e

    @classmethod
    def get_row_count_in_table(self,element_identifier_name):
        __element_list = []
        try:
            by = Page_elements().get_element_identifier(element_identifier_name)
            by = eval(by)
            __element_list = Env_setup.get_driver().find_elements_by_xpath(by[1])
            return __element_list.__len__()
        except webdriver_exceptions.NoSuchElementException as e:
            raise e
##########################Autforms specific########################################


    












