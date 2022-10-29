#!/usr/bin/pythoni3
def uniq_add(my_list=[]):
    unique_list = []
    sum_unique_list = []
    for items in my_list:
        if item not in unique_list:
            unique_list.append(item)
            sum_unique_list += item
    return sum_unique_list
