#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    count = len(my_list)
    new_list = my_list.copy()
    if idx < 0 or idx > (count - 1):
        return my_list.copy()
    else:
        new_list[idx] = element
    return new_list
