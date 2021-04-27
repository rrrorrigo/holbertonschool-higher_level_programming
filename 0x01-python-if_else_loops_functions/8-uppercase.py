#!/usr/bin/python3
def uppercase(str):
    for con in range(len(str)):
        isup = ord(str[con])
        if isup >= 97 and isup <= 122:
            isup = isup - 32
        asciiToChar = chr(isup)
        print("{}".format(asciiToChar), end="")
    print()
