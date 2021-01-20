#!/usr/bin/python3

from os import path
import json
from sys import argv

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

"""script that adds all arguments to a list, and then save them to a file"""

list_json = []

file_name = "add_item.json"

if path.exists(file_name):
    obj = load_from_json_file(file_name)
    for element in obj:
        list_json.append(element)
for i in range(1, len(argv)):
    list_json.append(argv[i])
save_to_json_file(list_json, file_name)
