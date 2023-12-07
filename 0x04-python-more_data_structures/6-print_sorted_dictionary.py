#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    a_dictionary = sorted(a_dictionary.items(), key=lambda x: x[0])
    for key, value in a_dictionary:
        print("{}: {}".format(key, value))
