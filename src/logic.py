#Is onnly playing ground
import random
import numpy as np
"""
# Here is your grid
grid = np.random.binomial(1, 0.2, size=(3,3))

# Request two random integers between 0 and 3 (exclusive)
indices =  np.random.randint(0, high=3, size=2)

# Extract the row and column indices
i = indices[0]
j = indices[1]

# Put 2 at the random position
grid[i,j] = 10
"""
class playfield():
    """
    This is the logical side off the playfield
    try:
    Unix methods approach: every method do one thing, put this good

    """
    def __init__(self, length, wide, bombs):
        """
        input: length:number and wide.number
        do: create out of  input a  two dimensional list
        output: the two dimensional list
        """
        notbombs=wide*length - bombs
        self.board = [10]*bombs + notbombs*[0]
        #random.shuffle(board)
        self.board = np.array(board).reshape(length,wide)
       
        

    def placebombs2darray(self, bombs):
        """
        input: number of bombs
        do: put the bombs randomly in the playfield
        output: 
        attention: do not put two bombs on the same field


        """
        for i in range(1,bombs):
            ranlegth=random.randint(0,self.length)
            ranwide=random.randint(0,self.wide)
            if self.playfield[ranlegth][ranwide] != 'x':
                self.playfield[ranlegth][ranwide] = 'x'
                neighbarfrombombs(ranlegth,ranwide)
            else:
                bombs+=1
        
    def placebombsmatrix(bombs):


                





        pass
    def createwarnfileds(self, length, wide):
        result = 

       

    
        
        pass

playfield(5,8,3)
#createwarnfileds()

