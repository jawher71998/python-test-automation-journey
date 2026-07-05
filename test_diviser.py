import pytest


def diviser(a, b):
    if b == 0:
        raise ValueError("Impossible de diviser par zéro")
    return a / b


def test_diviser_normal():
    assert diviser(10, 2) == 5


def test_diviser_resultat_decimal():
    assert diviser(7, 2) == 3.5


def test_diviser_par_zero():
    with pytest.raises(ValueError):
        diviser(5, 0)