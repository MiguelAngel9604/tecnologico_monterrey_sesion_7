import pytest


def myfunc():
    raise ValueError("Exception 123 raised")


def test_match_v1():
    """The dot . matches any character, and the asterisk * means zero or more of them.
    So this pattern will match a string that contains "123" anywhere in it."""
    with pytest.raises(ValueError, match=r".* 123 .*"):
        myfunc()


def test_match_v2():
    with pytest.raises(ValueError, match="123"):
        myfunc()


def zero_division():
    return 1 / 0


def test_zero_division_v1():
    with pytest.raises(ZeroDivisionError):
        zero_division()


def test_zero_division_v2():
    with pytest.raises(ZeroDivisionError):
        1 / 0


# si necesita tener acceso a la información de excepción real, puede usar:
def test_recursion_depth():
    with pytest.raises(RuntimeError) as excinfo:

        def f():
            f()

        f()

        # print(excinfo.value)
        # print(excinfo.type)
        # print(excinfo.traceback)
    # assert "maximum recursion" in str(excinfo.value)
    assert "<class 'RecursionError'>" in str(excinfo.type)


@pytest.mark.xfail(raises=ZeroDivisionError)
def test_xfail():
    # myfunc()
    zero_division()


"""
Using pytest.raises() is likely to be better for cases where you are testing exceptions 
your own code is deliberately raising, whereas using @pytest.mark.xfail with a check 
function is probably better for something like documenting unfixed bugs 
(where the test describes what “should” happen) or bugs in dependencies.

https://docs.pytest.org/en/7.1.x/how-to/assert.html
"""
