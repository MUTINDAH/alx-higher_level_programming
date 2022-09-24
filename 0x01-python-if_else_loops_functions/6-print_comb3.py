#!/usr/bin/python3
for first_num in range(0, 10):
    for second_num in range(0, 10):
        if first_num < second_num:
            print("{}{}".format(first_num, second_num), end="")
            if first_num < 8:
                print(", ", end="")
print("\n", end="")
