#!/usr/bin/python3
""" sends a request to the URL and displays the value of the X-Request-Id"""

import requests
from sys import argv

if __name__ == "__main__":

    req = requests.get(argv[1])
    if req.status_code >= 400:
        print("Error code: {}" .format(req.status_code))
    else:
        print(req.text)
