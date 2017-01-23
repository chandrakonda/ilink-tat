import csv, time ,os , logging
from apptio_automation.Framework.Environment_setup import EnvironmentSetup

import apptio_automation.Framework.Extensions.Custom_logger as  cl
log = cl.customLogger(logging.DEBUG)
pass_list,fail_list = [],[]

details_results_list = []


framework_path = getattr(EnvironmentSetup,"var_parent_folder_path")

current_run_folder_name = getattr(EnvironmentSetup,"var_dynamic_name") #time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))

def collect_details_results(modified ,same ,current_category_value,parent_category):
    #__val = 1
    __result_dict = {}
    __result_dict["Top Level"] = parent_category
    __result_dict["Current Testing Node"] = current_category_value
    if bool(modified):
        __result_dict["Matching Keys"] =  ""
        __result_dict["Non Matching Keys"] = list(modified)
        __result_dict["Status"] = "Fail"

    elif bool(same):
        __result_dict["Matching Keys"] = list(same)
        __result_dict["Non Matching Keys"] = ""
        __result_dict["Status"] = "Pass"
        #pass_list.append(pass_dict)
    else:
        __result_dict["Matching Keys"] = "Data not available"
        __result_dict["Non Matching Keys"] = ""
        __result_dict["Status"] = "Pass"
        #pass_list.append(pass_dict)
    details_results_list.append(__result_dict)



def write_category_details_in_log(file_name,data):
    __folder_path = os.path.join(framework_path, "Results", time.strftime("%Y%m%d", time.localtime(time.time())),current_run_folder_name)
    if not os.path.exists(__folder_path):
        os.makedirs(__folder_path)
    __file = "{}\\{}.txt".format(__folder_path, file_name)
    with open(__file, "a") as myfile:
        myfile.write("\n###########\n" + str(data))



def write_category_details_to_csv(file_name,fieldnames,result_list):
    __folder_path = os.path.join(framework_path, "Results", time.strftime("%Y%m%d", time.localtime(time.time())),current_run_folder_name)
    if not os.path.exists(__folder_path):
        os.makedirs(__folder_path)
    __file = "{}\\{}.csv".format(__folder_path,file_name)
    with open(__file, 'wb') as csvfile:
        header_names = fieldnames
        writer = csv.DictWriter(csvfile, fieldnames=header_names)
        writer.writerow(dict((fn, fn) for fn in header_names))
        for row in result_list:
            writer.writerow(row)

# def write_category_details_to_csv(file_name):
#     env = EnvironmentSetup()
#     framework_path = env.get_parent_folder_path()
#     result_file_name = file_name+time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
#     __folder_path = os.path.join(framework_path, "Results", time.strftime("%Y%m%d", time.localtime(time.time())))
#     if not os.path.exists(__folder_path):
#         os.makedirs(__folder_path)
#     __file = "{}\\{}.csv".format(__folder_path,result_file_name)
#     with open(__file, 'wb') as csvfile:
#         fieldnames = ['Top Level', 'Current Testing Node', 'Matching Keys', 'Non Matching Keys','Status']
#         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#         writer.writerow(dict((fn, fn) for fn in fieldnames))
#         for row in pass_list:
#             writer.writerow(row)
#         for row1 in fail_list:
#             writer.writerow(row1)

#
# def write_child_results(dict):
#     child_list.append(dict)
