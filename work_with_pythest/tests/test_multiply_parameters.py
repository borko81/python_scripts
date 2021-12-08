import pytest

products = [
    (2, 3, 6),
    (1, 99, 99),
    (0, 99, 0)
]


products2 = [
    (10, 5, 2),
    (10, 1, 10)
]


@pytest.mark.parametrize('a, b, product', products)
def test_multiplication(a, b, product):
    assert a * b == product


@pytest.mark.parametrize('a, b, product', products2)
def test_division(a, b, product):
    assert a / b == product
