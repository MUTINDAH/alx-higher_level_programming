#!/usr/bin/python3
for i in range(97, 123):
    a = chr(i).format(i).replace("e", "") and chr(i).format(i).replace("q", "")
    print(a.format(i), end="")
