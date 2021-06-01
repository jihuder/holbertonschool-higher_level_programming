#!/usr/bin/python3
"""script that adds all arguments to a Python list,
  and then save them to a file
"""


import json
import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

try:
    list_js = load_from_json_file('add_item.json')
except:
    list_js = []
finally:
    for argc in sys.argv[1:]:
        list_js.append(argc)
        save_to_json_file(list_js, 'add_item.json')
