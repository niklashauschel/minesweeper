
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
      tkinter need the totall different  position of colum and row
    """
    def __init__(self, colums, rows, bombs, board):   # sometimes only board is use an rest the other
        """
        input: rows and colums and bombs all numbers
        do: create a list with bombs and notboms fileds and shuffle them randomly
            then formate this list to an 2d array
        out: the 2d array with random bombs
        """
        
        self.rows = rows
        self.colums = colums
        self.bombs = bombs
        if board is None:
            notBombs = self.rows * self.colums - bombs
            if (notBombs > 0):
                self.board = [10]*self.bombs + notBombs*[0]  # 10 is standing for bombs
                random.shuffle(self.board)
                self.board = np.array(self.board, dtype=int).reshape(rows, colums)
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
            print('IndexError')

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
        NEIGHBOURS = ((-1, -1), (-1,  0), (-1,  1),
                     (0, -1),            (0,  1),
                     (1, -1), (1,  0),   (1,  1))
        return ((row + neighborRow, colum + neighborColum) for (neighborRow, neighborColum) in NEIGHBOURS)


    def getAllOtherOpenFields(self, colum, row, _openfields):  # This funktion need really on test case, this not a easy testcase
        #  Eckzelle mit Zahl
        #  keine 0 um eine 0 herum 
        '''
        input: an field with no bombs in the neighborhood and 
        openfields list which is a list off allready calculatec that they have to be open in before rekursiv method call
        has to be null to beginning 
        do: search all fields around which have no bombs around and also the first field which have bombs around
        output: all fields which should open in minesweeper, if you press a button on the filed
        '''
        openfields = _openfields
        if not openfields:
            openfields.append((colum, row))
        for(rowsNeighbor, columsNeighbor) in self.getNeighbours(colum, row):
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
                        columsNeighbor == colum + 1):
                        return openfields    










# the following methods are only for testing casse
'''
testboard =[[1, 1, 1, 0, 0],
            [1, 10, 1, 1, 1],
            [1, 2, 2, 2, 10],
            [0, 1, 10, 2, 1],
            [0, 1, 1, 1, 0]]
objplacolumsfield = Board(5, 5, 3, testboard)
# objplacolumsfield.createWarnFields()
#value = objplacolumsfield.getValueFromBoard(1, 0)
board = objplacolumsfield.getBoard()
print(board)
nochange = objplacolumsfield.getAllOtherOpenFields(4, 4, [])
# print(value)
print(nochange)
nochange = objplacolumsfield.getAllOtherOpenFields(4, 0, [])
# print(value)
print(nochange)
nochange = objplacolumsfield.getAllOtherOpenFields(0, 4, [])
# print(value)
print(nochange)
'''
testboard =[[1, 1, 0, 1, 1],
            [10, 2, 1, 1, 10],
            [2, 10, 1, 1, 1],
            [1, 2, 2, 1, 0],
            [0, 1, 10, 1, 0]]
objplacolumsfield = Board(5, 5, 3, testboard)
# objplacolumsfield.createWarnFields()
#value = objplacolumsfield.getValueFromBoard(1, 0)
board = objplacolumsfield.getBoard()
print(board)
nochange = objplacolumsfield.getAllOtherOpenFields(3, 0, [])
# print(value)
print(nochange)
# nochange = objplacolumsfield.getAllOtherOpenFields(0, 4, [])
# print(value)
# print(nochange)
# nochange = objplacolumsfield.getAllOtherOpenFields(4, 4, [])
# print(value)
# print(nochange)
