#!/usr/bin/python3

import sys


def safe_function(fct, *args):
    try:
        return fct(*args)
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None

# #!/usr/bin/python3
#
# import sys
#
#
# def safe_function(fct, *args):
#     try:
#         result = fct(*args)
#         return (result)
#     except:
#         print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
#         return (None)
