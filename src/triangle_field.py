def get_triangle_field(base: int, height: int) -> float:
    print(0.5 * base * height)


def test_triangle_area(capsys):
    # try
    base = 10
    height = 8

    # when
    get_triangle_field(base, height)
    out, err = capsys.readouterr()

    # then
    assert out == '40.0\n'
