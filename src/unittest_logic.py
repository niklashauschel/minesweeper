import logic as logic
import unittest

class TestStringMethods(unittest.TestCase):
    def test(self): 
        result = logic.testForTest() 
        expected = 5
        self.assertEqual(expected, result)
unittest.main()