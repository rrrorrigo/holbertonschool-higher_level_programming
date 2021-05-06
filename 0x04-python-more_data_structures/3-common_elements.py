#!/usr/bin/python3
def common_elements(set_1, set_2):
        set_r = []
        for string in set_1:
                if string in set_2:
                        set_r.append(string)
        return set_r
