import pytest
from utils import fact

def test_fact0():
	assert fact(0) == 1

def test_fact1():
	assert fact(1) == 1

def test_fact():
	n = 5
	assert fact(5) == 120

def test_fact_stupid():
	with pytest.raises(TypeError):
		n = fact([])

def test_fact_negative():
	with pytest.raises(ValueError):
		n = fact(-1)