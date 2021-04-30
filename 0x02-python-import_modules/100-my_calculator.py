#!/usr/bin/python3
if __name__ == "__main__":
        from sys import argv
        l = len(argv)
        if l != 4:
                print("Usage: ./100-my_calculator.py <a> <operator> <b>")
                exit(1)
        from calculator_1 import add, sub, mul, div
        operator = ["+", "-", "*", "/"]
        a = int(argv[1])
        b = int(argv[3])
        f = [add, sub, mul, div]
        for i, check in enumerate(operator):
                if check == argv[2]:
                        print("{} {} {} = {}".format(a, check, b, f[i](a, b)))
                        break
        else:
                print("Unknown operator. Available operators: +, -, * and /")
                exit(1)
