import unittest
# This is a simple test case for string methods in Python
# It checks the functionality of upper, isupper, and split methods
class TestStringMethods(unittest.TestCase):
    # Test case for the upper method
    # It checks if the string 'foo' is converted to 'FOO'
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')
    # Test case for the isupper method
    # It checks if 'FOO' is uppercase and 'Foo' is not
    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())
    # Test case for the split method
    # It checks if the string 'hello world' is split into a list of words
    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        with self.assertRaises(TypeError):
            s.split(2)
    # Test case for the isdigit method
    # It checks if the string '123' is a digit
    def test_isdigit(self):
        self.assertTrue('123'.isdigit())

if __name__ == '__main__':
    unittest.main()