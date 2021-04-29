#!/usr/bin/python3
if __name__ == "__main__":
        from sys import argv
        import calculator_1
        l = len(argv)
        op = ["+", "-", "*", "/"]
        a = int(argv[1])
        b = int(argv[3])
        add = calculator_1.add(a, b)
        sub = calculator_1.sub(a, b)
        mul = calculator_1.mul(a, b)
        div = calculator_1.div(a, b)
        if l != 4:
                print("Usage: {:s} <a> <operator> <b>".format(argv[0]))
                exit(1)
        for i in range(0, l):
                if operator[i] == argv[2]:
                        check = i
                        break
                check = -1
        if check == -1:
                print("Unknown operator. Available operators: +, -, * and /")
                exit(1)
        elif op[check] == "+":
                print("{:d} + {:d} = {:d}".format(a, b, add))
        elif op[check] == "-":
                print("{:d} - {:d} = {:d}".format(a, b, sub))
        elif op[check] == "*":
                print("{:d} * {:d} = {:d}".format(a, b, mul))
        elif op[check] == "/":
                print("{:d} / {:d} = {:d}".format(a, b, div))
