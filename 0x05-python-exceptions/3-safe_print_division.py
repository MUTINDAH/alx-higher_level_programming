#!/usr/bin/python3

def safe_print_division(a, b):
    result = a / b
    try:
        result
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
