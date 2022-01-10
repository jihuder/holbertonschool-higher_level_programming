#!/usr/bin/python3
"""
script that takes your GitHub credentials
(username and password) and uses the GitHub
API to display your id
"""

if __name__ == '__main__':
    import requests
    from requests.auth import HTTPBasicAuth
    from sys import argv

    url = 'https://api.github.com/user'

    r = requests.get(url, auth=HTTPBasicAuth(argv[1], argv[2]))
    print(r.json().get('id'))
