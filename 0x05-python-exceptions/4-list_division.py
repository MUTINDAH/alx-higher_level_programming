#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            if i >= len(my_list_1) or i >= len(my_list_2):
                raise Exception("out of range")
            if not (isinstance(my_list_1[i], (int, float)) and isinstance(my_list_2[i], (int, float))):
                raise Exception("wrong type")
            result.append(my_list_1[i] / my_list_2[i])
        except ZeroDivisionError:
            print("division by 0")
            result.append(0)
        except Exception as e:
            print(e)
            result.append(0)
    return result
