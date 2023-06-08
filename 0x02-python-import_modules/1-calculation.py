#!/usr/bin/python3
from calculator_1 import add, div, subs, mult
a = 10
b = 5
if __name__ == "__main__":
    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))
    print("{} - {} = {}".format(a, b, subs(a, b)))
    print("{} * {} = {}".format(a, b, mult(a, b)))
