
import random
import numpy as np
from logging import *


filename = 'logic'

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
        in: rows and colums and bombs all numbers
        do: create a list with bombs and notboms fileds and shuffle them randomly
            then formate this list to an 2d array
        out: the 2d array with random bombs
        """
        self.logNameClass = 'Board'
        logNameMethod = '__init__'
        log = getLogger(filename + '.' + self.logNameClass + '.' + logNameMethod)
        self.rows = rows
        self.colums = colums
        self.bombs = bombs
        if board is None:
            notBombs = self.rows * self.colums - bombs
            if (notBombs > 0):
                self.board = [10]*self.bombs + notBombs*[0]  # 10 is standing for bombs
                random.shuffle(self.board)
                self.board = np.array(self.board, dtype=int).reshape(rows, colums)
                log.debug("Board is created sucessful")
            else:
                log.error("There are to many bombs")
        else:
            self.board = board
        log.debug("Board is set from outside")

    def getBoard(self):
        """
        getter for board
        """
        logNameMethod = 'getBoard'
        log = getLogger(self.logNameClass + '.' + logNameMethod)
        log.debug('getBoard call and Board looks like: \n {}'.format(self.board))
        return self.board        

    def getValueFromBoard(self, colum, row):
        """
        simple getter for special value on index
        """
        logNameMethod = 'getValueFromBoard'
        log = getLogger(filename + '.' + self.logNameClass + '.' + logNameMethod)
        try:
            log.debug('value of return is {}'.format(self.board[row][colum]))
            return(self.board[row][colum])
        except IndexError:
            log.error('IndexError')
    
    def getClickedFieldsAmount(self):
        logNameMethod = 'getClieckedFieldsAmound'
        log = getLogger(filename + '.' + self.logNameClass + '.' + logNameMethod)
        result = np.where(self.board == 11)
        listOfCoordinates = list(zip(result[1], result[0]))
        log.debug('value of return is {}'.format(len(listOfCoordinates)))
        return len(listOfCoordinates)

    def createWarnFields(self):
        """
        input: the board with only bombs and filed with no bombs
        do: write on the filed with no bombs how much bombs are int the near
        output: the filed with everyfiled the number of bombs in the near
        """
        logNameMethod = 'createWarnFields'
        log = getLogger(filename + '.' + self.logNameClass + '.' + logNameMethod)
        result = np.where(self.board == 10)
        listOfCoordinates = list(zip(result[1], result[0]))
        for cord in listOfCoordinates: 
            rowsOfBomb = cord[1]
            columsOfBomb = cord[0]
            for(rowsNeighbor, columsNeighbor) in self.getNeighbours(columsOfBomb, rowsOfBomb):
                if(rowsNeighbor >= 0 and
                   rowsNeighbor < self.rows and
                   columsNeighbor >= 0 and columsNeighbor < self.colums):
                                self.board[rowsNeighbor][columsNeighbor] += 1
        log.debug('Board after creating Warnfileds looks like: \n {}'.format(self.board))


    def setValueFromBoard(self, colum, row):
        logNameMethod = 'setValueFromBoard'
        log = getLogger(self.logNameClass + '.' + logNameMethod)
        self.board[row][colum] = 11
        log.debug('value is setted as 11 that mean clicked')
    

    def getNeighbours(self, colum, row):
        '''
        Free from minesweeper.py
        why a extra method?
        Because you need the Neighbours for a field  in morec then one Mthod
        in: the colum and row from one field
        do: calculate the neighbars
        out: the neighbarsfrom one field
        '''
        
        NEIGHBOURS = ((-1, -1), (-1,  0), (-1,  1),
                     (0, -1),            (0,  1),
                     (1, -1), (1,  0),   (1,  1))
        return ((row + neighborRow, colum + neighborColum) for (neighborRow, neighborColum) in NEIGHBOURS)

    def getAllOtherOpenFields(self, colum, row, _openfields):  # This funktion need really on test case, this not a easy testcase
        '''
        in: an field with no bombs in the neighborhood and 
        openfields list which is a list off allready calculatec that they have to be open in before rekursiv method call
        has to be null to beginning 
        do: search all fields around which have no bombs around and also the first field which have bombs around
        out: all fields which should open in minesweeper, if you press a button on the filed
        '''
        logNameMethod = 'getAllOtherOpenFields'
        log = getLogger(self.logNameClass + '.' + logNameMethod)
        log.debug('rekursiv call witth colum:{} row:{}'.format(colum, row))
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

    def checkAllNeighboursWhereBombs(self):
        logNameMethod = 'checkAllNeighboursWhereBombs'
        log = getLogger(self.logNameClass + '.' + logNameMethod)
        self.createWarnFields()
        test = np.where(self.board == 19)
        if(len(test[0]) != 0 and len(test[1]) != 0):
            log.debug('All Neighbours are bombs')
            return True
        else:
            morethan10 = np.where(self.board > 10)
            listOfCoordinates = list(zip(morethan10[0], morethan10[1]))
            for cord in listOfCoordinates: 
                rowsof10 = cord[0]
                columsof10 = cord[1]
                self.board[rowsof10][columsof10] = 10
            log.debug('not all Neighbours are bombs')
            return False

    def isBoardSolvable(self):
        """
        TODO Check if one filed has more then 7 neighbours with bombs check off mirror axis
        are they more not solvable in notsolvable fields folder
        """
        logNameMethod = 'isBoardSolvable'
        log = getLogger(self.logNameClass + '.' + logNameMethod)
        result = np.where(self.board == 8)
        if((len(result[0]) != 0 and len(result[1]) != 0) or self.checkAllNeighboursWhereBombs()):  # or self.mirrorAxis()
            log.debug('it is not solvable, create new board')
            self.__init__(self.colums, self.rows, self.bombs, None)
        else:
            # TODO logging it is solvable
            log.debug('Allright it is solvable')
            pass

    def mirrorAxis(self):
        logNameMethod = 'mirrorAxis'
        log = getLogger(self.logNameClass + '.' + logNameMethod)
        halfcolum = int(np.ceil(self.colums/2)) - 1
        halfrow = int(np.ceil(self.rows/2)) - 1
        
        for i in range(self.rows-1):
            for j in range(halfcolum):
                print(i)
                if(self.board[i][halfcolum - j - 1] == self.board[i][halfcolum + j] and
                   i == halfcolum):
                    return True
                else:
                    i = self.rows
        for i in range(self.colums):
            for j in range(halfrow):
                if(self.board[halfrow - j - 1][i] == self.board[halfrow + j][i] and
                   i == halfrow):
                    return True
                else:
                    i = self.colums
        return False



        log.debug('No MirrorAxis in Board')
        return False
                
                    

            
