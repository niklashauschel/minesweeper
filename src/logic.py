
import random
import numpy as np

import logging
LOG_FILENAME = 'Debugfile_logic.log'
logging.basicConfig(filename=LOG_FILENAME, level=logging.DEBUG)


class Board():
    """
    creating and working an the board 
    tkinter need the totall different  position of colum and row
    """
    """
    TODO talk if creatwarnfileds have to call in init
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
    
    def getClickedFieldsAmount(self):
        result = np.where(self.board == 11)
        listOfCoordinates = list(zip(result[1], result[0]))
        return len(listOfCoordinates)

    def createWarnFields(self):
        """
        input: the board with only bombs and filed with no bombs
        do: write on the filed with no bombs how much bombs are int the near
        output: the filed with everyfiled the number of bombs in the near
        """
        result = np.where(self.board == 10)
        listOfCoordinates = list(zip(result[1], result[0]))
        for cord in listOfCoordinates:   # funktioniert
            rowsOfBomb = cord[1]
            columsOfBomb = cord[0]
            for(rowsNeighbor, columsNeighbor) in self.getNeighbours(columsOfBomb, rowsOfBomb):
                if(rowsNeighbor >= 0 and
                    rowsNeighbor < self.rows and
                        columsNeighbor >= 0 and columsNeighbor < self.colums):
                            if(self.board[rowsNeighbor][columsNeighbor] != 10):
                                self.board[rowsNeighbor][columsNeighbor] += 1

    def setValueFromBoard(self, colum, row):
        self.board[row][colum] = 11

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
        
        
        '''
        input: an field with no bombs in the neighborhood and 
        openfields list which is a list off allready calculatec that they have to be open in before rekursiv method call
        has to be null to beginning 
        do: search all fields around which have no bombs around and also the first field which have bombs around
        output: all fields which should open in minesweeper, if you press a button on the filed
        '''
        logging.debug('rekursiv call witth colum:{} row:{}'.format(colum, row))
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
                        elif(rowsNeighbor == row + 1 and
                             columsNeighbor == colum + 1 and self.board[rowsNeighbor][columsNeighbor]):
                                return openfields
                            
                elif (rowsNeighbor == row + 1 and
                        columsNeighbor == colum + 1):
                        return openfields

        def isBoardSovable(self):
            """
            TODO Check if one filed has more then 7 neighbours with bombs check off mirror axis
            are they more not solvable in notsolvable fields folder
            """
            pass
