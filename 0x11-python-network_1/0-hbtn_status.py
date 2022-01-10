#!/usr/bin/python3
"""script that fetches https://intranet.hbtn.io/status"""



import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen("https://intranet.hbtn.io/status") as response:
        fetch_html = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(fetch_html)))
        print("\t- content: {}".format(fetch_html))
        print("\t- utf8 content: {}".format(fetch_html.decode('utf8')))
