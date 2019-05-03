
import random
import numpy as np
"""
import logging
LOG_FILENAME = 'example.log'
logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG)

logging.debug('This message should go to the log file')
"""


class Board():
    """
      creating and working an the board 
    """
    def __init__(self, colums, rows, bombs):
        """
        input: rows and colums and bombs all numbers
        do: create a list with bombs and notboms fileds and shuffle them randomly
            then formate this list to an 2d array
        out: the 2d array with random bombs
        """
        self.rows = rows
        self.colums = colums
        self.bombs = bombs
        notBombs = self.rows * self.colums - bombs
        if (notBombs > 0):
            self.board = [10]*self.bombs + notBombs*[0]  # 10 is standing for bombs
            random.shuffle(self.board)
            self.board = np.array(self.board).reshape(rows, colums)
        else:
            print("There are to many bombs")

    def getBoard(self):
        """
        simple getter for array complete
        """
        return(self.board)

    def getValueFromBoard(self, colum, row):
        """
        simple getter for special value on index
        """
        try:
            return(self.board[row][colum])
        except IndexError:
            print("This is a mistake in the GUI")

    def createWarnFields(self):
        """
        input: the board with only bombs and filed with no bombs
        do: write on the filed with no bombs how much bombs are int the near
        output: the filed with everyfiled the number of bombs in the near
        """
        result = np.where(self.board == 10)
        listOfCoordinates = list(zip(result[1], result[0]))
        print(listOfCoordinates)
        for cord in listOfCoordinates:   # funktioniert
            rowsOfBomb = cord[1]
            columsOfBomb = cord[0]
            for i in [-1, 0, 1]:            # macolumsbe safe one loop
                for j in [-1, 0, 1]:
                    rowsNeighbor = rowsOfBomb + i
                    columsNeighbor = columsOfBomb + j
                    if(rowsNeighbor >= 0 and
                        rowsNeighbor < self.rows and
                        columsNeighbor >= 0 and columsNeighbor < self.colums and
                            not(i == 0 and j == 0)):
                            if(self.board[rowsNeighbor][columsNeighbor] != 10):
                                self.board[rowsNeighbor][columsNeighbor] += 1             
'''
the following methods are only for testing casses
'''
objplacolumsfield = Board(9, 7, 3)
objplacolumsfield.createWarnFields()
value = objplacolumsfield.getValueFromBoard(1, 0)
board = objplacolumsfield.getBoard()
print(value)
print(board)
