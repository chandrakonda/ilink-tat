from time import localtime, strftime
import pytest,traceback,time
from  apptio_automation.Framework.Environment_setup import LoadTestData,PageElements,EnvironmentSetup,dict_cleanup


@pytest.fixture(scope='module')
def apptio_setup():
    try:
        print("################## Module Set Up ###################")
        __local_env_setup = EnvironmentSetup()
        __local_env_setup.setup()  # create driver for working
        obj_page_elements = PageElements()  # get page elements required to execute test cases in this module into dictionary
        # Load page elements based on the module you want to execute
        obj_page_elements.load_page_elements("Apptio_Pageelements")
        obj_load_data = LoadTestData()  # load the test data required to execute test cases in this module into dictionary
        obj_load_data.load_data("Test_Data", "Apptio_Testdata")
        EnvironmentSetup.go_to_url()
        #time.sleep(3)
    except:
        traceback.print_exc()
    yield apptio_setup
    print("################## Module Tear Down ###################")
    dict_cleanup()
    EnvironmentSetup.quit_driver()
    global obj_load_data
    obj_load_data= None



@pytest.fixture(scope="function")
def function_setup():
    print("####################  Function setup  ####################")
    yield
    print("####################  Function Tear Down  #######################")
