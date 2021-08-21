#!/usr/bin/python3
"""Python script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id"""
import requests
from sys import argv


if __name__ == '__main__':
        repository = argv[1]
        owner = argv[2]
        r = requests.get("https://api.github.com/repos/{}/{}/commits"
                         .format(repository, owner))
        try:
                data = r.json()
                for i, req in enumerate(data):
                        if i < 10:
                                sha = req.get('sha')
                                author = req.get('commit')\
                                            .get('author').get('name')
                                print("{}: {}".format(sha, author))
                        else:
                                break
        except:
                pass
