#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
        result = []
        for x in range(list_length):
                try:
                        result.append(my_list_1[x] / my_list_2[x])
                except ZeroDivisionError:
                        print("division by 0")
                        result.append(0)
                except TypeError:
                        print("wrong type")
                        result.append(0)
                except IndexError:
                        print("out of range")
                        result.append(0)
                finally:
                        pass
        return result
