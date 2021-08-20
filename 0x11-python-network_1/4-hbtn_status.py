#!/usr/bin/python3
""" Python Script that fetches https://intranet.hbtn.io/status"""
from urllib import request


if __name__ == '__main__':
        with request.urlopen("https://intranet.hbtn.io/status") as response:
                body = response.read()
                body = body.decode('utf8')
                print("Body response:")
                print("\t- type: {}".format(type(body)))
                print("\t- content: {}".format(body))
