#!/usr/bin/python3
def multiple_returns(sentence):
    """if sentence is empty or none,return none"""

    if not sentence:
        return (0, "None")
    else:
        return (len(sentence), sentence[0])
