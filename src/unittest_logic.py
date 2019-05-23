# !/usr/bin/python
"""
    @ author : Till Fetzer
    @ e-mail : till.fetzer@googlemail.com
    @ date : 17.05.2019
"""
import unittest  # standart liberies
import numpy as np
from unittest.mock import patch
import logging

import logic as logic  # local source

LOG_FILENAME = 'Debugfile_tests.log'
logging.basicConfig(filename=LOG_FILENAME, level=logging.DEBUG)


class Testlogic(unittest.TestCase):
    """
    in: -
    do: test the definit testcases
    out: in terminal if testcase run correctly or not
    """

    def test_GetValueFromBoard(self):
        """
        in: value from GetValueFromBoard, self calulate value
        do: combare if the Method GetValueFromBoard
        with a  the value from that is on the board itself
        out: if test run good or with an error
        """
        testboard = np.array([[2, 0],
                             [0, 0]], dtype=int)
        test = logic.Board(2, 2, 0, testboard)
        self.assertEqual(2, test.getValueFromBoard(0, 0))

    def test_CreateWarnField(self):
        """
        in:  self calculate board how have to look like the board after createwarnfileds,
            the board after the method CreateWarnfileds
        do:  Prepare for test and combare the inputs
        out:  if test run good or with an error
        """
        testboard = np.array([[10, 0],
                              [0, 0]], dtype=int)
        test = logic.Board(2, 2, 1, testboard)
        test.createWarnFields()
        HowTheBoardLooksLike = np.array([[10, 1],
                                         [1, 1]], dtype=int)
        self.assertTrue(np.array_equal(test.getBoard(), HowTheBoardLooksLike))

    def test_GetAllOtherOpenFields(self):
        '''
        use these special testcase because off, it destroy the programm
            by the first implementation from GetAllOtherFields
        in: the fields in on array off tubles that should, be open from GetAllOtherOpenFileds,
             the fields in on array off tubles that  open from GetAllOtherOpenFileds,
        do:  prepare the test and compare the inputs
        out:  if test run good or with an error
        '''
        testboard = np.array([[1, 1, 0, 1, 1],
                              [10, 2, 1, 1, 10],
                              [2, 10, 1, 1, 1],
                              [1, 2, 2, 1, 0],
                              [0, 1, 10, 1, 0]], dtype=int)
        test = logic.Board(5, 5, 3, testboard)
        listOfOpen = test.getAllOtherOpenFields(2, 0, [])
        fieldsHaveToBeOpen = [(1, 0), (2, 0), (3, 0), (1, 1), (2, 1), (3, 1)]
        self.assertTrue(not sum([i not in listOfOpen for i in fieldsHaveToBeOpen]))
        # copied from https://stackoverflow.com/questions/8866652/
        # determine-if-2-lists-have-the-same-elements-regardless-of-order

    def test_GetAllOtherOpenFieldsNotReturnNone(self):
        """
        in: the output off all fileds with method GetAllOtherOpenFields
        do: Check off if None back, this is because off this is the case if
        the GetAllOpenFields do not come to an return
        out:  if test run good or with an error
        """

        test2 = logic.Board(10, 10, 1, None)
        test2.createWarnFields()  # because sometimes they give None pack
        for i in [0, 10]:
            for j in [0, 10]:
                listOfOpentest2 = test2.getAllOtherOpenFields(i, j, [])
                self.assertIsNotNone(listOfOpentest2)

    def test_getOpenFiledsAmount(self):
        """
        in: the output of getOpenFieldsAmount with the given field
        do: Check if the output and the self calculated value are the same
        out: if test run good or with an error
        """
        testboard = np.array([[1, 11, 0, 1, 1],
                              [10, 2, 1, 1, 10],
                              [2, 11, 1, 11, 1],
                              [1, 2, 2, 1, 0],
                              [0, 1, 11, 1, 0]], dtype=int)
        getOpenFiledsAmountTestBoard = logic.Board(5, 5, 3, testboard)
        self.assertEqual(getOpenFiledsAmountTestBoard.getClickedFieldsAmount(), 4)

if __name__ == '__main__':
    unittest.main()
