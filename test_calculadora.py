import pytest
from calculadora import soma, subtrai, multiplica, divide

def test_soma():
    assert soma(5, 5) == 10

def test_subtrai():
    assert subtrai(10, 5) == 5

def test_multiplica():
    assert multiplica(3, 4) == 12

def test_divide_comum():
    assert divide(10, 2) == 5

def test_divide_por_zero():
    assert divide(10, 0) == "Erro: Divisão por zero"
