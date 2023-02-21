#!/usr/bin/python3
"""generates random integer"""
import random


def generate_int():
    """return random integer from 0 to 16"""
    binary = ''
    for i in range(4):
        binary += str(random.randint(0, 1))
    return int(binary, base=2)
