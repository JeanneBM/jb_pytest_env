import pytest
from src.triangle_field import get_triangle_field

def triangle_field_test(capsys):
    # try
    base = 10
    height = 8

    # when
    get_triangle_field(base, height)
    out, err = capsys.readouterr()

    # then
    assert out == '40.0\n'
