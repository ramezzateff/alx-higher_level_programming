#!/bin/usr/python3
def print_sorted_dictionary(a_dictionary):
    for key, value in sorted(a_dictionary):
        print("{}: {}".format(key, value))
