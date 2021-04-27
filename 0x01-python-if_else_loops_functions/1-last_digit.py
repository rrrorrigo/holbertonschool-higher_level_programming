#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ld = number % 10 if number > 0 else abs(number) % 10
print("Last digit of {} is ".format(number), end='')
if ld > 5:
    print("{} and is greater than 5".format(ld))
elif ld < 6 and ld > 0:
    if number < 0:
        print("-{} and is less than 6 and not 0".format(ld))
    else:
        print("{} and is less than 6 and not 0".format(ld))
else:
    print("is 0")
