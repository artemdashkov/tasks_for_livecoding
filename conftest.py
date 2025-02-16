import pytest

@pytest.fixture()
def func_1():
    print("\nstart to fixture: 'func_1'")
    yield
    print("\nend to fixture: 'func_1'")