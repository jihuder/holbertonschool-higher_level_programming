#!/usr/bin/python3
"""
script that takes in a letter and sends a POST
request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""

if __name__ == "__main__":
    import requests
    from sys import argv

    if len(argv) == 2:
        q = argv[1]
    else:
        q = ""
    res = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})

    try:
        req = res.json()
        id = req.get('id')
        name = req.get('name')
        if len(req) == 0 or not id or not name:
            print("No result")
        else:
            print("[{}] {}".format(req.get('id'), req.get('name')))
    except Exception:
        print("Not a valid JSON")
