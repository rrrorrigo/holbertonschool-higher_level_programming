#!/usr/bin/python3
"""Python script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id"""
import requests
from sys import argv


if __name__ == '__main__':
        usr = argv[1]
        pwd = argv[2]
        try:
                r = requests.get('https://api.github.com/user', auth=(usr, pwd))
                data = r.json()
                print(data['id'])
        except:
                pass
