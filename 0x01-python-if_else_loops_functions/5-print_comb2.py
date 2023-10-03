#!/usr/bin/python3
# 5-print_comb2.py

"""Prints numbers from 0 to 99"""
for i in rangee(0, 100):
    if i != 99:
        print(f"{i:02}", end=", ")
    else:
        print(f"{i}")
