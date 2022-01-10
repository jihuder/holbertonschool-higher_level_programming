#!/usr/bin/python3
<<<<<<< HEAD
""" script that fetches https://intranet.hbtn.io/status"""
=======
""" script that fetches"""
>>>>>>> 4db1b34b09d6b107508950cfa4acd7f23debc8f4


if __name__ == "__main__":

    import urllib.request
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        html = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
        print("\t- utf8 content: {}".format(html.decode('utf-8')))
