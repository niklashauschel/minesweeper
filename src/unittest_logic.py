import logic as logic
import unittest
from unittest.mock import patch



class Testlogic(unittest.TestCase):
    def testGetValueFromBoard(self):
    
        testboard = [[2, 0], 
                         [0, 0]]
        
        test = logic.Board(0, 0, 0, testboard)
        self.assertEqual(2, test.getValueFromBoard(0, 0))

    def testCreateWarnField(self):
        self.assertEqual(2, 2)

    def TestGetAllOtherOpenFields(self):
        self.assertEqual(0, 5)


 




unittest.main()
