#!/usr/bin/python3
def fizzbuzz():
        for aux in range(1, 101):
                if aux % 3 == 0 and aux % 5 == 0:
                        print("FizzBuzz", end=' ')
                elif (aux % 3) == 0:
                        print("Fizz", end=' ')
                elif (aux % 5) == 0:
                        print("Buzz", end=' ')
                else:
                        print("{}".format(aux), end=' ')
