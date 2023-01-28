#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    printed_elements = 0
    for i in range(x):
        try:
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end=' ')
                printed_elements += 1
        except(ValueError, TypeError):
            continue
    print()
    return printed_elements
