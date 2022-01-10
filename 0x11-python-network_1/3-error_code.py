#!/usr/bin/python3
"""
script that takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8).
"""

if __name__ == "__main__":
    import urllib.error as err
    import urllib.request as request
    from sys import argv
    r = request.Request(argv[1])
    try:
        with request.urlopen(r) as rq:
            print(rq.read().decode('utf-8'))
    except err.HTTPError as e:
        print("Error code: {}".format(e.code))
