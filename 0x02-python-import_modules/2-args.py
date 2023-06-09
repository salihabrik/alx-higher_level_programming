#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    args = len(argv) - 1
    if args == 0:
        print("{} arguments.". format(args))
    elif args == 1:
        print("{} argument:".format(args))
        print("1: {}".format(argv[1]))
    else:
        print("{} arguments:".format(args))
        i = 1
        for arg in argv[1:]:
            print("{}: {}".format(i, arg))
            i += 1
