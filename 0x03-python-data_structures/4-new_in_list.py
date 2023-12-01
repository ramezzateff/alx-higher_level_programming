#!/bin/bash
def new_in_list(my_list, idx, element):
    count = len(my_list)
    if idx < 0 or idx >= count:
        return my_list
    else:
        new_list = my_list.copy()
        new_list[idx] = element
    return new_list
