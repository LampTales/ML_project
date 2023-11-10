import os

file_path = '../data/TT100K/TT100K.names'
names = open(file_path, 'r').readlines()
names = [name.strip() for name in names]
names_to_num = {}
for i, name in enumerate(names):
    names_to_num[name] = i

# for i, name in enumerate(names):
#     print(i, name)

def get_name_id(name):
    return names_to_num[name]

def get_id_name(id):
    return names[id]