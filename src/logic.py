
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
    def __init__(self, colums, rows, bombs, board):   # sometimes only board is use an rest the other
        """
        input: rows and colums and bombs all numbers
        do: create a list with bombs and notboms fileds and shuffle them randomly
            then formate this list to an 2d array
        out: the 2d array with random bombs
        """
        if board is None:
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
        else:
            self.board = board

    def getBoard(self):
        """
        simple getter for board
        """
        return self.board        

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
            for(rowsNeighbor, columsNeighbor) in self.getNeighbours(columsOfBomb, rowsOfBomb):
                if(rowsNeighbor >= 0 and
                    rowsNeighbor < self.rows and
                        columsNeighbor >= 0 and columsNeighbor < self.colums):
                            if(self.board[rowsNeighbor][columsNeighbor] != 10):
                                self.board[rowsNeighbor][columsNeighbor] += 1

    def getNeighbours(self, colum, row):

        '''
        Free from minesweeper.py
        why a extra method?
        Because you need the Neighbours for a field  in morec then one Mthod
        input: the colum and row from one field
        do: calculate the neighbars
        output: the neighbarsfrom one field
        '''
        NEIGHBARS = ((-1, -1), (-1,  0), (-1,  1),
                     (0, -1),            (0,  1),
                     (1, -1), (1,  0),   (1,  1))
        return ((row + neighbarsRow, colum + neighbarsColum) for (neighbarsRow, neighbarsColum) in NEIGHBARS)

    def getAllOtherOpenFields(self, colum, row, _openfields):  # This funktion need really on test case, this not a easy testcase
        '''
        input: an field with no bombs in the neighbarhood and 
        openfields list which is a list off allready calculatec that they have to be open in before rekursiv method call
        has to be null to beginning 
        do: search all fields around which have no bombs around and also the first field which have bombs around
        output: all fields which should open in minesweeper, if you press a button on the filed
        '''
        openfields = _openfields  # Wenn wir eine leere Liste erste rekursion
        openfields.append((colum, row))
        for(columsNeighbor, rowsNeighbor) in self.getNeighbours(colum, row):
                if(rowsNeighbor >= 0 and
                    rowsNeighbor < self.rows and
                        columsNeighbor >= 0 and columsNeighbor < self.colums and
                        not((columsNeighbor, rowsNeighbor) in openfields)):
                        openfields.append((columsNeighbor, rowsNeighbor))
                        if(self.board[rowsNeighbor][columsNeighbor] == 0):
                                self.getAllOtherOpenFields(columsNeighbor, rowsNeighbor, openfields)
                        else:
                            if(self.board[rowsNeighbor][columsNeighbor] == 10):
                                return print("something gone terrible wrong")
                elif (rowsNeighbor == row + 1 and
                        columsNeighbor == colum + 1 and
                        (columsNeighbor, rowsNeighbor) in openfields):
                        return openfields











# the following methods are only for testing casses

objplacolumsfield = Board(9, 7, 4, None)
objplacolumsfield.createWarnFields()
value = objplacolumsfield.getValueFromBoard(1, 0)
board = objplacolumsfield.getBoard()
print(board)
nochange = objplacolumsfield.getAllOtherOpenFields(2, 2, [])
print(value)
print(nochange)
