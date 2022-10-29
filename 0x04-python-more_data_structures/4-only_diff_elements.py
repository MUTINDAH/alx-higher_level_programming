#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    duplicates = []
    for element in set_1:
        if element not in set_2:
            duplicates.append(element)
    for element in set_2:
        if element not in set_1:
            duplicates.append(element)
    return duplicates
