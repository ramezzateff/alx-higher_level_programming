#!/usr/bin/python3
def max_integer(my_list=[]):
    count = len(my_list)
    max_num = my_list[0]
    if count == 0:
        return "None"
    else:
        for i in range(count):
            if my_list[i] > max_num:
                max_num = my_list[i]
    return max_num
