import logic as logic
import unittest
import numpy as np
from unittest.mock import patch
import logging
LOG_FILENAME = 'Debugfile_tests.log'
logging.basicConfig(filename=LOG_FILENAME, level=logging.DEBUG)





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
        
        test.createWarnFields()
        HowTheBoardLooksLike = np.array([[10, 1],
                                [1, 1]], dtype=int)
                                
        self.assertTrue(np.array_equal(test.getBoard(), HowTheBoardLooksLike))
    
    




    def test_GetAllOtherOpenFields(self):
        ''' 
        use these special testcase because off, it destroy the programm by the first implementation from GetAllOtherFields
        '''
           
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
        test2 = logic.Board(10, 10, 1, None)
        test2.createWarnFields()  # because sometimes they give None pack 
        for i in [0, 10]:
            for j in [0, 10]:
                listOfOpentest2 = test2.getAllOtherOpenFields(i, j, [])
                self.assertIsNotNone(listOfOpentest2)

    def test_getOpenFiledsNumber



        # copied from https://stackoverflow.com/questions/8866652/
        # determine-if-2-lists-have-the-same-elements-regardless-of-order
        
if __name__ == '__main__':
    unittest.main()



