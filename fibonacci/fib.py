#!/usr/bin/python3
"""fibnacci module""" 


def fib():
    """generate the first 50 fibnacci series"""
    sequence = []
    for i in range(50):
        if i == 0 or i == 1:
            sequence.append(i)
        else:
            sequence.append(sequence[i - 1 ]
                    + sequence[i - 2])
    return sequence

