#!/usr/bin/pythoni3
def uniq_add(my_list=[]):
    unique_list = []
    sum_unique = 0
    for item in my_list:
        if item not in unique_list:
            unique_list.append(item)
            sum_unique += item
    return sum_unique
