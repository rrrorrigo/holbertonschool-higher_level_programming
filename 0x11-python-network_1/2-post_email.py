#!/usr/bin/python3
"""Python script that takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter"""
from urllib import request
from urllib import parse
from sys import argv


if __name__ == '__main__':
        url = argv[1]
        email = argv[2]
        value = {'email': email}
        data = parse.urlencode(value)
        data = data.encode('ascii')
        req = request.Request(url, data)
        with request.urlopen(req) as response:
                r = response.read()
                print(r.decode('utf8'))
