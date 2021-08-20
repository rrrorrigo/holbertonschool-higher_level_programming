#!/usr/bin/python3
"""  Python script that takes in a URL, sends a request to the URL
and displays the value of the X-Request-Id variable foundin the
header of the response"""
from urllib import request
from urllib import error
from sys import argv


if __name__ == '__main__':
        try:
                with request.urlopen(argv[1]) as response:
                        r = response.read()
                        print(r.decode('utf8'))
        except error.HTTPError as e:
                print("Error code: {}".format(e.code))
