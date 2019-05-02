from tkinter import *
from logic import Board


class Menubar:
    def __init__(self, master):
        self.master = master
        self.creatMenuBar()

    '''
        Create the standard MenuBar for all of the windows
    '''      
    def creatMenuBar(self):
        self.menubar = Menu(self.master)
        self.filemenu = Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Help", command=self.helpUser)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=self.exitConfig)
        self.menubar.add_cascade(label="Menu", menu=self.filemenu)
        self.master.config(menu=self.menubar)
 
    '''
        Creates a new window, where the rules of the game where the rules are described
    '''
    def helpUser(self):
        root2 = Toplevel(self.master)
        myGUI = HelpUserWindow(root2)
        Grid.rowconfigure(root2, 0, weight=1)
        Grid.columnconfigure(root2, 0, weight=1)
        root2.title("Help with Minesweeper")
        root2.update()
        root2.minsize(root2.winfo_width(), root2.winfo_height())
        root2.mainloop()
        
    def exitConfig(self):
        self.master.destroy()


'''
    In the class the user gets the information about the game
'''
class HelpUserWindow(Menubar):
    def __init__(self, master):
        self.master = master
        self.creatMenuBar()
        self.label1 = Label(self.master, text="Minesweeper is a single-player puzzle video game. The objective of the game is to clear a rectangular board containing hidden \"mines\" or bombs without detonating any of them, with help from clues about the number of neighboring mines in each field. The game originates from the 1960s, and has been written for many computing platforms in use today. It has many variations and offshoots.", wraplength=400, justify='left')
        self.label1.grid()
        return super().__init__(master)

    '''
       Overwrites the inherited method, so the windows, has another Menubar  
    '''     
    def creatMenuBar(self):
        self.menubar = Menu(self.master)
        self.filemenu = Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Exit", command=self.exitConfig)
        self.menubar.add_cascade(label="Menu", menu=self.filemenu)
        self.master.config(menu=self.menubar)


class Configuration(Menubar):
    def __init__(self, master):
        self.master = master
        self.v = IntVar()
       
        self.label1 = Label(self.master, text='Enter your Name')
        self.textfield = Text(self.master, width=15, height=3)
        self.createRadioButtons()

        self.buttonNewWindow = Button(self.master, text="New Game", command=self.createGame)

        self.label1.grid(row=0, column=0, columnspan=2, sticky="N")
        self.textfield.grid(row=1, column=0, rowspan=1, columnspan=2, sticky="NESW")
        self.radiobutton1.grid(row=2, column=0, columnspan=2, sticky="N")
        self.radiobutton2.grid(row=3, column=0, columnspan=2, sticky="N")
        self.radiobutton3.grid(row=4, column=0, columnspan=2, sticky="N")

        self.buttonNewWindow.grid(row=6, column=1, sticky="E")
        return super().__init__(master)

    '''
        Create the Radiobuttons and set easy as the dafault value
    '''
    def createRadioButtons(self):
        self.radiobutton1 = Radiobutton(self.master, text="Easy", variable=self.v, value=1)
        self.radiobutton2 = Radiobutton(self.master, text="Medium", variable=self.v, value=2)
        self.radiobutton3 = Radiobutton(self.master, text="Hard", variable=self.v, value=3)
        self.v.set(1)

    def destroyMenu(self):
        self.master.destroy()

    def createGame(self):
        player = self.textfield.get("1.0", "end")
        degree_of_difficulty = self.v.get()
        root2 = Toplevel(self.master)
        myGUI = Game(root2, player, degree_of_difficulty)
        Grid.rowconfigure(root2, 0, weight=1)
        Grid.columnconfigure(root2, 0, weight=1)
        root2.title("Minesweeper Game")
        root2.update()
        root2.minsize(root2.winfo_width(), root2.winfo_height())
        root2.mainloop()


def endGame():
    print('TODO Endgame')




    

def getRealButtonPosition(event):
    print(event.widget.grid_info())
    gridDict = event.widget.grid_info()
    clickedRow = gridDict['row']
    clickedColumn = gridDict['column']
    clickedRow = clickedRow - 1
    #print(clickedRow, clickedColumn)
    return clickedRow, clickedColumn


class Game(Menubar):
    def __init__(self, master, player, degree_of_difficulty):
        self.degree_of_difficulty = degree_of_difficulty
        self.master = master
        self.player = player
        self.setGameFieldSize()
        self.createBoard()
        self.setUpFrame()
        self.createFirstLine()

        self.photo = PhotoImage(file="test.png")    
        
        for r in range(1, self.row):
            for c in range(self.column):

                name = str(c) + " " + str(r)
                self.btn = Button(self.frame, image=self.photo, text=name)
                self.btn.grid(column=c, row=r, sticky=N+S+E+W)
                self.btn.bind("<Button-1>", self.handleButtonClickLeft)
                self.btn.bind("<Button-3>", self.handleButtonClickRight)

                Grid.columnconfigure(self.frame, c, weight=1)
                Grid.rowconfigure(self.frame, r, weight=1)
        return super().__init__(master)


    '''
        Handle the right click on a button
    '''
    def handleButtonClickRight(self, event):
        if event.widget['bg'] == 'blue':
            event.widget.config(bg='white')
        else:
            event.widget.config(bg='blue')

    '''
        Handle the left click on a button
    '''
    def handleButtonClickLeft(self, event):
        r, c = getRealButtonPosition(event)
        print(r, c)
        valueCell = self.board1.getvaluefromBoard(c, r)
        print(valueCell)
        if valueCell == 10:
            print('You clicked on a mine')
            endGame()
        else:
            print("You didn't clicked on a mine")
        event.widget.config(bg='red', image='', text=valueCell)
        event.widget.unbind('<Button-1>')
        event.widget.unbind('<Button-3>')
    
    '''
        Check the input degree_of_difficulty and get the playground size
    '''
    def setGameFieldSize(self):
        # TODO Give here the module the game field size
        if self.degree_of_difficulty == 1:
            self.column = 5
            self.row = 5
            self.mines = 3
        elif self.degree_of_difficulty == 2:
            self.column = 9
            self.row = 7
            self.mines = 5
        else:
            self.column = 18
            self.row = 10
            self.mines = 10

    def createBoard(self):
        self.board1 = Board(self.column, self.row, self.mines)
        self.board1.createWarnFields()
        print(self.board1.getBoard())

    ''' 
        First setup the Frame and configure the grid
        # Source: https://stackoverflow.com/questions/7591294/how-to-create-a-self-resizing-grid-of-buttons-in-tkinter
    '''
    def setUpFrame(self):
        self.frame = Frame(self.master)
        self.frame.grid(row=0, column=0, sticky=N+S+E+W)
        self.grid = Frame(self.frame)
        self.grid.grid(sticky=N+S+E+W, column=0, row=0)
        Grid.rowconfigure(self.frame, 0, weight=1)
        Grid.columnconfigure(self.frame, 0, weight=1)
    
    ''' 
        Create first line of the game field and configure the line of labels based on playing field width
    '''
    def createFirstLine(self):
        
        # create
        minesNumber = str(self.mines) + " Mines"
        self.time = Label(self.master, text=minesNumber)
        self.label1 = Label(self.frame, text="Welcome to Minesweeper")
        self.name = Label(self.frame, text=self.player)

        # configure
        self.time.grid(row=0, column=0, sticky="NW", columnspan=self.row)
        self.label1.grid(row=0, column=0, sticky="N", columnspan=self.row)
        self.name.grid(row=0, column=0, sticky="NE", columnspan=self.row)

    def destroyMenu(self):
        self.master.destroy()

    
def main():
    root = Tk()
    config = Configuration(root)
    root.title("Minesweeper Configuration")
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.update()
    root.minsize(root.winfo_width(), root.winfo_height())
    root.mainloop()


if __name__ == "__main__":
    main()