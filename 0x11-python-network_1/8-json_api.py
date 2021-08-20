#!/usr/bin/python3
"""Python script that takes in a URL, sends a request
to the URL and displays the body of the response"""
import requests
from sys import argv


if __name__ == '__main__':
        url = "http://0.0.0.0:5000/search_user"
        value = {'q': ""}
        if len(argv) > 1:
                value['q'] = argv[1]
        r = requests.post(url, data=value)
        try:
                data = r.json()
                if data == {}:
                        print("No result")
                else:
                        print("[{}] {}".format(data['id'], data['name']))
        except:
                print("Not a valid JSON")
