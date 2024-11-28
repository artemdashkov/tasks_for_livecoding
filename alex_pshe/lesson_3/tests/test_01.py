from alex_pshe.lesson_3.class_and_methods import CheckNumber
import pytest

@pytest.mark.parametrize("number", [15, 5, 3])
def test_001(number):
    object_1 = CheckNumber()
    assert object_1.divided_on_fife_and_three(number), f"{number} don't divided on 5 or 3"
