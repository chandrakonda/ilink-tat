from apptio_automation.Framework.Extensions.Webdriveractions_extensions import ElementExtensions as element
import time,pdb,logging
import apptio_automation.Framework.Extensions.Custom_logger as  cl

# https://google.github.io/styleguide/pyguide.html
# Naming conventios
# module_name, package_name, ClassName, method_name, ExceptionName, 
#function_name, GLOBAL_CONSTANT_NAME, global_var_name, instance_var_name,
#function_parameter_name, local_var_name
class LoginPage(element):
    log = cl.customLogger(logging.DEBUG)
    def login(self,user_name,pass_word,json_file_version):

        self.log.info("##########################################################################")
        self.log.info("###################Enter Login page########################################")
        try:
            time.sleep(4)
            if json_file_version != '1' :
                element.click_on_element("circle_image")
            #pdb.set_trace()
            element.click_on_element_using_javascript("click_here_banner")
            time.sleep(3)
            element.set_text("user_name", user_name)
            element.set_text("password", pass_word)
            element.click_on_element("login_button")
            # verify image "TBM CONNECT"
            element.wait_for("tbm_allow_button")
            if element.is_element_displayed("tbm_connect_image"):
            # click on allow button
                element.click_on_element("tbm_allow_button")
                element.wait_for("image_site_logo")
                if (element.is_element_displayed_format("image_site_logo")):
                    self.log.info("'{}' Element present in the application ".format("image_site_logo"))
                    is_pass = True
                else:
                    is_pass = False
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
            self.log.info("###################Log out from application ########################################")
        except Exception as e:
            self.log.info("Exception thrown while logging out from application {}".format(e))
            raise Exception("Log out failed")






