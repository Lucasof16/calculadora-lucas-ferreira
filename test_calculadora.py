import pytest
from calculadora import soma, subtrai

def test_soma_positivos():
    assert soma(5, 5) == 10

def test_soma_negativos():
    assert soma(-1, -1) == -2

def test_subtracao_positivos():
    assert subtrai(10, 5) == 5

def test_subtracao_negativos():
    assert subtrai(-5, -5) == 0

def test_soma_zero():
    assert soma(0, 0) == 0
