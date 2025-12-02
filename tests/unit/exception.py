import pytest

with pytest.raises(RuntimeError) as excinfo:

    def f():
        f()

    f()
# print(excinfo.value)
print(excinfo.type)
# print(excinfo.traceback)
