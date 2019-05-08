import logic as logic
import unittest
import numpy as np
from unittest.mock import patch
import collections as coll



class Testlogic(unittest.TestCase):
    def test_GetValueFromBoard(self):
    
        testboard = np.array([[2, 0], 
                         [0, 0]], dtype=int)
        
        test = logic.Board(2, 2, 0, testboard)
        self.assertEqual(2, test.getValueFromBoard(0, 0))

    def test_CreateWarnField(self):
        
        testboard = np.array([[10, 0],
                         [0, 0]], dtype=int)
        test = logic.Board(2, 2, 1, testboard)
        # print(testboard)
        test.createWarnFields()
        HowTheBoardLooksLike = np.array([[10, 1],
                                [1, 1]], dtype=int)
        # print(HowTheBoardLooksLike)                        
        self.assertTrue(np.array_equal(test.getBoard(), HowTheBoardLooksLike))




    def test_GetAllOtherOpenFields(self):
        testboard = np.array(
            [[1, 1, 0, 1, 1],
             [10, 2, 1, 1, 10],
             [2, 10, 1, 1, 1],
             [1, 2, 2, 1, 0],
             [0, 1, 10, 1, 0]], dtype=int)
        test = logic.Board(5, 5, 3, testboard)
        listOfOpen = test.getAllOtherOpenFields(2, 0, [])
        fieldsHaveToBeOpen = [(1, 0), (2, 0), (3, 0), (1, 1), (2, 1), (3, 1)]
        self.assertTrue(not sum([not i in listOfOpen  for i in fieldsHaveToBeOpen])) 

        # copied from https://stackoverflow.com/questions/8866652/
        # determine-if-2-lists-have-the-same-elements-regardless-of-order
        
if __name__ == '__main__':
    unittest.main()



