#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as calc
    import sys

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    op = sys.argv[2]
    a = int(sys.argv[1])
    b = int(sys.argv[3])

    if op == "+":
        print("{} {} {} = {}".format(a, op, b, calc.add(a, b)))
    elif op == "-":
        print("{} {} {} = {}".format(a, op, b, calc.sub(a, b)))
    elif op == "*":
        print("{} {} {} = {}".format(a, op, b, calc.mul(a, b)))
    elif op == "/":
        print("{} {} {} = {}".format(a, op, b, calc.div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
