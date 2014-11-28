import unittest
import utils

class SumTest(unittest.TestCase):

	def test_ab0(self):
		self.assertEquals(utils.sum(0,0), 0)

	def test_ab(self):
		a = 5
		b = 2
		self.assertEquals(utils.sum(a,b), a + b)

if __name__ == '__main__':
	unittest.main()