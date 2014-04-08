from minimal_representation import get_minimal_representation
import unittest


class MinimalRepresentationTests(unittest.TestCase): 
	"""
	We'll this out with a bunch of examples of expected behavior
	"""
	def test_simple_snv(self): 
		pos, ref, alt = 1000, 'A', 'T'
		expected = 1000, 'A', 'T'
		self.assertEqual(get_minimal_representation(pos, ref, alt), expected)


if __name__ == '__main__': 
	unittest.main()