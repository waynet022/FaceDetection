
def read_names(file):
    name_list = []
    with open(file) as names:
        list = names.read().splitlines()
        for name in list:
            name_list.append(name)
    return name_list