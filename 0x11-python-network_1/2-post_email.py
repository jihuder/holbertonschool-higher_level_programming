#!/usr/bin/python3
"""script that takes in a URL and an email, sends a POST"""


if __name__ == "__main__":
    import urllib.parse
    import urllib.request
    from sys import argv
    val = {'email': argv[2]}
    data = urllib.parse.urlencode(val).encode('ascii')
    rq = urllib.request.Request(argv[1], data)
    with urllib.request.urlopen(rq) as response:
        content = response.read().decode('utf-8')
    print(content)
