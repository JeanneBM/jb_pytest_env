'''

how to test print():
capsys - special variable appears during the program
out, err = capsys.readouterr() - returns tuple -> an output or an error

'''

def triangle_field_test(capsys):
    # try
    base = 10
    height = 8

    # when
    get_triangle_field(base, height)
    out, err = capsys.readouterr()

    # then
    assert out == '40.0\n'
