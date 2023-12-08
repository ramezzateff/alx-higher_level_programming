#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    total_product = sum(x * y for x, y in my_list)
    total_weights = sum(y for _, y in my_list)
    return total_product / total_weights
