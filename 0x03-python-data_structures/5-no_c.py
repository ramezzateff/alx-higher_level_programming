#!/usr/bin/python3
def no_c(my_string):
    count = len(my_string)
    charRemove = "c"
    charRemove2 = "C"
    new_string = ""
    for i in range(count):
        if my_string[i] != charRemove and my_string[i] != charRemove2:
            new_string += my_string[i]
    return new_string
