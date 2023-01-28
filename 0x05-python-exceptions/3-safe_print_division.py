#!/usr/bin/python3

def safe_print_division(a, b):
    quotient = (a / b)
    try:
        return quotient
    except ZeroDivisionError:
        quotient = None
    finally:
        print("Inside result: {:d}".format(quotient))
    return quotient
