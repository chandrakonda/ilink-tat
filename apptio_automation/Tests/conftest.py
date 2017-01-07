import pytest,sys,os,traceback,pdb,json
from time import localtime, strftime
# from Framework.Environment_setup import LoadTestData,PageElements,EnvironmentSetup , dict_cleanup


# run_time_dic_data = {}

########################################################################################
#Fixture to modify command line arguments for updating result path
#########################################################################################
# --html=c:\workingdirectory\att\sample3.html
#pdb.set_trace()
def pytest_cmdline_preparse(args):
    get_current_time = None
    if 'time' in sys.modules:
        import time
        now = time.localtime(time.time())
        __local_automation_path = os.path.abspath(os.path.join(os.path.dirname("__file__")))
        __local_var_folder = time.strftime("%Y%m%d", now)
        __local_var_current_date_time = time.strftime("%Y%m%d%H%M%S", now)
        __folder_path = os.path.join(__local_automation_path,"Results",__local_var_folder)

    if not os.path.exists(__folder_path):
        os.makedirs(__folder_path)
    val = args
    __val = "--html={}\\{}.html".format(__folder_path,__local_var_current_date_time)
    val[0] = __val
    args = val
    #pdb.set_trace()


#########################################################################################
# Load Json Data
#########################################################################################

@pytest.fixture(scope='session',autouse=False)
def json_data(request,jsonfileversion):
    #jsonData = {}
    #pdb.set_trace()
    __local_automation_path = os.path.abspath(os.path.join(os.path.dirname("__file__")))
    if jsonfileversion == '1':
        __json_file_name = "atum-tree_v1.0.json"
    elif jsonfileversion == '2':
        __json_file_name = "atum-tree_v2.0.json"
    else:                # if user is not passing any value for the file, then we will take default as version 2
        __json_file_name = "atum-tree_v2.0.json"

    file_name = os.path.join(__local_automation_path, "Jsonfiles",__json_file_name)
    with open(file_name) as data_file:
        yield json.load(data_file)


def pytest_addoption(parser):
    parser.addoption("--jsonfileversion")

@pytest.fixture(scope="session")
def jsonfileversion(request):
    return request.config.getoption("--jsonfileversion")



# #########################################################################################

# #TODO: http://doc.pytest.org/en/latest/writing_plugins.html#pytest.Parser.addoption
# TODO: http://stackoverflow.com/questions/34466027/in-py-test-what-is-the-use-of-conftest-py-files


# ########################################################################################
# #These fixtures are used for report
# #########################################################################################
# @pytest.fixture(autouse=True)
# def _environment(request):
#     request.config._environment.append(('Testing Environment', 'Qa'))
#     request.config._environment.append(('Test cases', 'smoke Testcases'))
#     request.config._environment.append(('Release', '579'))


# def pytest_report_header(config):
#     return "Application Name : Autoforms"

# #########################################################################################
# # Used to capture run time data
# #########################################################################################
# @pytest.fixture(scope='session')
# def run_time_dic_data(request):
#     run_time_dic_data = {}
