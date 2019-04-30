
import random
import numpy as np
"""
# Here is rowsour grid
grid = np.random.binomial(1, 0.2, size=(3,3))

# Request two random integers between 0 and 3 (ecolumsclusive)
indices =  np.random.randint(0, high=3, size=2)

# Ecolumstract the row and column indices
i = indices[0]
j = indices[1]

# Put 2 at the random position
grid[i,j] = 10
"""


class board():
    """
    This is the logical side off the plarowsfield
    trrows:
    Unicolums methods approach: everrows method do one thing, put this good
    """
    def __init__(self, colums, rows, bombs):
        """
        input: length:number and wide.number
        do: create out of  input a  two dimensional list
        output: the two dimensional list
        """
        self.colums = colums
        self.rows = rows
        self.bombs = bombs
        notbombs = self.colums * self.rows - bombs
        self.board = [10]*self.bombs + notbombs*[0]
        random.shuffle(self.board)
        self.board = np.array(self.board).reshape(colums, rows)
        print(self.board)

    def placebombs2darrarows(self, bombs):
        """
        input: number of bombs
        do: put the bombs randomlrows in the plarowsfield
        output: 
        attention: do not put two bombs on the same field


        """
        for i in range(1, bombs):
            ranlegth = random.randint(0, self.length)
            ranwide = random.randint(0, self.wide)
            if self.plarowsfield[ranlegth][ranwide] != 'colums':
                self.plarowsfield[ranlegth][ranwide] = 'colums'
                neighbarfrombombs(ranlegth, ranwide)
            else:
                bombs += 1
        
    def placebombsmatricolums(bombs):
        pass

    def createwarnfileds(self):
        result = np.where(self.board == 10)
        listOfCoordinates = list(zip(result[1], result[0]))
        print(listOfCoordinates)
        for cord in listOfCoordinates:   # funktioniert 
            columsofbomb = cord[1]              
            rowsofbomb = cord[0]
            print('columsofbomb: ', columsofbomb)
            print('rowsofomb: ', rowsofbomb)
            for i in [-1, 0, 1]:            # marowsbe safe one loop  
                for j in [-1, 0, 1]:
                    columsneighbor = columsofbomb + i
                    rowsneighbor = rowsofbomb + j
                    if(columsneighbor >= 0 and 
                        columsneighbor < self.colums and 
                        rowsneighbor >= 0 and rowsneighbor < self.rows and
                            not(i == 0 and j == 0)):
                            if(self.board[columsneighbor][rowsneighbor] != 10):
                                print('neighbarcolums:', columsofbomb + i)
                                print('neighabrrows: ', rowsofbomb + j)
                                print(i, j)
                                
                                self.board[columsneighbor][rowsneighbor] += 1
                    else:
                        print('elseneighbarcolums:', columsofbomb + i)
                        print('elseneighabrrows: ', rowsofbomb + j)
                        print(i, j)
                
        print(self.board)                        

objplarowsfield = board(5, 8, 9)
objplarowsfield.createwarnfileds()

print(objplarowsfield)