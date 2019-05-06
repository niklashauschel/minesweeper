import logic as logic
import unittest
from unittest.mock import patch



class Testlogic(unittest.TestCase):
    def testgetValueFromBoard(self):
    
        testboard = [[2, 0], 
                         [0, 0]]
        
        test = logic.Board(0, 0, 0, testboard)
        self.assertEqual(2, test.getValueFromBoard(0, 0))
        

 




unittest.main()
