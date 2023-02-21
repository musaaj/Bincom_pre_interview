#!/usr/bin/python3
"""search for a number in a list"""


def search(number, number_list, start_pos=0):
    """return index of a number in a list of numbers

    Args:
        number: int
        number_list: list<int>
        start_pos: positive int

    Return:
        int on success else None
    """
    if start_pos >= len(number_list):
        return
    if number_list[start_pos] == number:
        return (start_pos)
    return search(number, number_list, start_pos = start_pos + 1)
