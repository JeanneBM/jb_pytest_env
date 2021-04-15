import pytest

def sort_by(names, first_letter=False, last_letter=False, length=False):
    if first_letter:
        names.sort()

    if last_letter:
        names.sort(key=lambda name: name[::-1])

    if length:
        names.sort(key=len)

    return names
