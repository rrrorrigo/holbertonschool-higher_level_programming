#!/usr/bin/python3
if __name__ == "__main__":
        from sys import argv
        l = len(argv)
        if l == 1:
                print("0 arguments.")
        elif l == 2:
                print("1 argument:\n" + "1: {:s}".format(argv[1]))
        else:
                pos = 1
                print("{:d} arguments:".format(l - 1))
                for i in range(1, l):
                        print("{:d}: {:s}".format(pos, argv[i]))
                        pos += 1
