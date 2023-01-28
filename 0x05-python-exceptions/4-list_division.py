#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(0, list_length):
        try:
            div = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            div = 0
        except ZeroDivisionError:
            print("division by 0")
            div = 0
        except IndexError:
            print("out of range")
            div = 0
        finally:
            new_list.append(div)
    return new_list
# def list_division(my_list_1, my_list_2, list_length):
#     result = []
#     for i in range(list_length):
#         try:
#             if i >= len(my_list_1) or i >= len(my_list_2):
#                 raise Exception("out of range")
#             if not (isinstance(my_list_1[i], (int, float)) and isinstance(my_list_2[i], (int, float))):
#                 raise Exception("wrong type")
#             result.append(my_list_1[i] / my_list_2[i])
#         except ZeroDivisionError:
#             print("division by 0")
#             result.append(0)
#         except Exception as e:
#             print(e)
#             result.append(0)
#     return result
