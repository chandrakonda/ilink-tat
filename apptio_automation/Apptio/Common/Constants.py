

class Constant_Values:

    #json_attributes_to_check = ["description","examples","uom_list","target_users","service_offering_levers","service_level_kpis"]

    app_to_json_mapping = {

        "Description":"description",
        "Children":"children",
        "Examples":"examples",
        "Unit of Measure List":"uom_list",
        "Service Level KPIs":"service_level_kpis",
        "Target Users":"target_users",
        "Service Offering Levers":"service_offering_levers"
    }

    children_validation_col_list = ["Key_value", "Imagepresent", "Cloudimagepresent", "Childlist", "Childrenmatching","FinalStatus"]
    detail_validation_col_list = ['Top Level', 'Current Testing Node', 'Matching Keys', 'Non Matching Keys', 'Status']
