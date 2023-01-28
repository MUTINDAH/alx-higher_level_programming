#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return False
# import sys
#
# def safe_print_integer_err(value):
#     try:
#         print("{:d}".format(int(value)))
#         return True
#     except Exception as e:
#         print("Exception: " + str(e), file=sys.stderr)
#         return False
