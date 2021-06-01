#!/usr/bin/python3
"""script that adds all arguments to a Python list,
   and then save them to a file
"""
from sys import argv


save_from_json = __import__('5-save_to_json_file').save_to_json_file
load_from_json = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
    content = load_from_json_file(filename)
except:
    content = []

save_from_json(content + argv[1:], filename)
