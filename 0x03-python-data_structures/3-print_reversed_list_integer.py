#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    count = len(my_list)
    my_list = [int(item) for item in my_list]
    for i in reversed(range(count)):
        print("{}".format(my_list[i]))
