#!/usr/bin/python3
def magic_string():
    magic_string.n = getattr(magic_string, 'n', 0) + 1
    return "\n".join(", ".join(["BestSchool"] * i) for i in range(1, magic_string.n + 1)) + "$"
