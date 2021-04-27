#!/usr/bin/python3
for d in range(10):
    for u in range(10):
        if d < u:
            print("{}{}".format(d, u), end='\n' if d is 8 and u is 9 else ", ")
