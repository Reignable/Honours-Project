def debug_print(class_name, function_name, data):
    header = '\033[95m'
    endc = '\033[0m'
    bold = '\033[1m'
    tabs1 = '\t\t' if len(class_name) < 17 else '\t'
    tabs2 = '\t\t' if len(function_name) < 17 else '\t'
    print (class_name + tabs1
           + function_name + tabs2
           + str(data))
