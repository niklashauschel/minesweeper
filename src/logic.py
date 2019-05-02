
import random
import numpy as np


class board():
    """
    
    """
    def __init__(self, rows, colums, bombs):
        """
        input: rows and colums and bombs all numbers
        do: create a list with bombs and notboms fileds and shuffle them randomly
            then formate this list to an 2d array
        out: the 2d array with random bombs
        """
        self.rows = rows
        self.colums = colums
        self.bombs = bombs
        notbombs = self.rows * self.colums - bombs
        if (notbombs <= 0):
            self.board = [10]*self.bombs + notbombs*[0]  # 10 is standing for bombs
            random.shuffle(self.board)
            self.board = np.array(self.board).reshape(rows, colums)
        else:
            console.log("There are to many bombs")

    def getBoard(self):
        """
        simple getter for array complete
        """
        return(self.board)

    def getvaluefromBoard(self, colum, row):
        """
        simple getter for special value on index
        """
        try:
            return(self.board[colum][row])
        except IndexError:
            console.log("This is a mistake in the GUI")

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
            rowsofbomb = cord[1]
            columsofbomb = cord[0]
            for i in [-1, 0, 1]:            # macolumsbe safe one loop
                for j in [-1, 0, 1]:
                    rowsneighbor = rowsofbomb + i
                    columsneighbor = columsofbomb + j
                    if(rowsneighbor >= 0 and
                        rowsneighbor < self.rows and
                        columsneighbor >= 0 and columsneighbor < self.colums and
                            not(i == 0 and j == 0)):
                            if(self.board[rowsneighbor][columsneighbor] != 10):
                                self.board[rowsneighbor][columsneighbor] += 1             

objplacolumsfield = board(1, 2, 0)
objplacolumsfield.createWarnFields()
value = objplacolumsfield.getvaluefromBoard(0, 0)
board = objplacolumsfield.getBoard()
print(value)
print(board)
