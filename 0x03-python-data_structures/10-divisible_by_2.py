#!/usr/bin/python3
def divisible_by_2(my_list=[]):
        if my_list:
                newList = my_list.copy()
                for i in range(len(my_list)):
                        if my_list[i] % 2:
                                newList[i] = False
                        else:
                                newList[i] = True
                return newList
