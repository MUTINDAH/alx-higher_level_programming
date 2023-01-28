#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    total_elements = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            total_elements += 1
        except IndexError:
            break
    print("")
    return total_elements

# def safe_print_list(my_list=[], x=0):
#     """The function will attempt to print x elements from the list,
#     with each element separated by a space"""
#     print_elements = 0
#     try:
#         """if there are not enough elements in the list to print x elements,
#          the function will print as many
#          elements as it can without raising an error."""
#         for i in range(x):
#             print(my_list[i], end=' ')
#             print_elements += 1
#     except:
#         pass
#     print()
#     """The function then returns the number of elements that were
#     actually printed."""
#     return print_elements
