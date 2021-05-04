#!/usr/bin/python3
def multiple_returns(sentence):
        r = (0, None)
        if sentence:
                r = (len(sentence), sentence[0])
        return r
