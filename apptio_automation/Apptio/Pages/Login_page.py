from apptio_automation.Framework.Extensions.Webdriveractions_extensions import ElementExtensions as element
import time,pdb,logging
import apptio_automation.Framework.Extensions.Custom_logger as  cl

# https://google.github.io/styleguide/pyguide.html
# Naming conventios
# module_name, package_name, ClassName, method_name, ExceptionName, 
#function_name, GLOBAL_CONSTANT_NAME, global_var_name, instance_var_name,
#function_parameter_name, local_var_name
class LoginPage(element):
    cl.customLogger(logging.DEBUG)
    def login(self,user_name,pass_word,json_file_version):
        try:
            #pdb.set_trace()
            time.sleep(6)
            if json_file_version != '1' :
                element.click_on_element("circle_image")
            element.click_on_element("click_here_banner")
            element.set_text("user_name", user_name)
            element.set_text("password", pass_word)
            element.click_on_element("login_button")
            # verify image
            element.is_element_displayed("tbm_connect_image")
            # click on allow button
            element.click_on_element("tbm_allow_button")
            # verify page title 
            if (element.is_element_displayed("image_site_logo")):
                print ("value is present in the application")
                is_pass = True
            else:
                is_pass = False
            return is_pass

        except Exception as e:
            self.log.exception("Exception thrown in login page {} ".format(e))
            raise

    def logout(self):
        self.log.info("Enter logout method")
        try:
            element.click_on_element("user_profile_image")
            element.click_on_element("logout")
        except Exception as e:
            self.log.info("Exception thrown while logging out from application {}".format(e))
            raise Exception("Log out failed")





