import logic as logic
import unittest
import numpy as np
from unittest.mock import patch



class Testlogic(unittest.TestCase):
    def test_GetValueFromBoard(self):
    
        testboard = [[2, 0], 
                         [0, 0]]
        
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
       testboard=[[ 0,  0,  1,  1,  1],
 [ 0,  0,  1, 10,  1],
 [ 0,  1,  2,  3,  2],
 [ 0,  1, 10,  2, 10],
 [ 0,  1,  1,  2,  1]]
       
   #    self.assertEqual(0, 5)
if __name__ == '__main__':
    unittest.main()



