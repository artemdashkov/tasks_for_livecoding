import pytest

@pytest.mark.parametrize("new_data", ['ar', 'br'])
def test_01(new_data, new_obj):
    print(f"\t ==============> {new_data}")


@pytest.fixture()
def new_obj():
    print(f"start func")
    yield print(f"yield")
    print(f"end func")
