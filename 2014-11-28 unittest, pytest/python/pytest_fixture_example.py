import pytest

@pytest.fixture
def context_data():
	class Human:
		def __init__(self):
			self.name = "Pasha"
		def getName(self):
			return self.name

	return Human()

def test_something(context_data):
	assert context_data.getName() == 'Pasha'
