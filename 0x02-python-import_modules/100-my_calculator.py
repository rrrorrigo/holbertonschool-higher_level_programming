#!/usr/bin/python3
if __name__ == "__main__":
        from sys import argv
        l = len(argv)
        if l != 4:
                print("Usage: {:s} <a> <operator> <b>".format(argv[0]))
                exit(1)
        from calculator_1 import add, sub, mul, div
        operator = ["+","-","*","/"]
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
