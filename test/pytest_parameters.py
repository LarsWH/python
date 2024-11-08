import pytest


@pytest.mark.parametrize("num1,num2,expected_output",
                         [
                             (2, 2, 4),
                             (3, 6, 9),
                             (4, 5, 10)
                         ]
                         )

def test_addition(num1, num2, expected_output):
    assert num1 + num2 == expected_output

