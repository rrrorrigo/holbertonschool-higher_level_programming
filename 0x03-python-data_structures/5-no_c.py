#!/usr/bin/env python3
def no_c(my_string):
        if my_string:
                new_string = ''
                for i in my_string:
                        if i not in 'Cc':
                                new_string += i
                return new_string
