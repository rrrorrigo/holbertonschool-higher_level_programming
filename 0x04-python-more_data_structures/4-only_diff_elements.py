#!/usr/bin/python3
def common_elements(set_1, set_2):
        set_r = []
        for string in set_1:
                if string not in set_2:
                        set_r.append(string)
        for string2 in set_2:
                if string2 not in set_1:
                        set_r.append(string2)
        return set_r
