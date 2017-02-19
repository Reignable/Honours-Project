def debug_print(class_name, function_name, data):
    header = '\033[95m'
    endc = '\033[0m'
    bold = '\033[1m'
    print (header
           + class_name + '\t'
           + endc
           + bold
           + function_name + '\t'
           + endc
           + str(data))
