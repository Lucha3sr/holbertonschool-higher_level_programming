#!/usr/bin/python3
""" sends a request to the URL and displays the value of the X-Request-Id"""

import urllib.request
from sys import argv

if __name__ == "__main__":

    req = urllib.request.Request(argv[1])
    try:
        with urllib.request.urlopen(req) as response:
            html = response.read()
            print(html.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}" .format(e.code))
