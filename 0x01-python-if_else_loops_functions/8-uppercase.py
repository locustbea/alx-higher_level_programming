#!/usr/bin/python3
# 8-uppercase.py

"""Prints a string in uppercase"""
def uppercase(str):
    for i in str:
        c = ord(i)
        if (97 <= c <= 122):
            c -= 32
            print(f"{c:c}", end="")
    print("")
