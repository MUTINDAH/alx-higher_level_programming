#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    int_elements = 0
    for i in range(x):
        if isinstance(my_list[i], int):
            try:
                print("{}".format(my_list[i]), end="")
                int_elements += 1
            except IndexError:
                break
    print("")
    return int_elements
