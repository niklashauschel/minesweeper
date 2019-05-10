from tkinter import *
from logic import Board
from logging import *
from time import *


class Menubar:
    '''
        It is the definition of the Menubar, which can be inherit by the GUI's later
    '''
    def __init__(self, master):
        self.master = master
        self.creatMenuBar()

    def creatMenuBar(self):
        '''
            Create the standard MenuBar for all of the windows
        '''
        self.menubar = Menu(self.master)
        self.filemenu = Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Help", command=self.helpUser)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=self.exitConfig)
        self.menubar.add_cascade(label="Menu", menu=self.filemenu)
        self.master.config(menu=self.menubar)

    def helpUser(self):
        '''
            Creates a new window, where the rules of the game where the rules are described
        '''
        root2 = Toplevel(self.master)
        myGUI = HelpUserWindow(root2)
        Grid.rowconfigure(root2, 0, weight=1)
        Grid.columnconfigure(root2, 0, weight=1)
        root2.title("Help with Find the Bug")
        root2.update()
        root2.minsize(root2.winfo_width(), root2.winfo_height())
        
    def exitConfig(self):
        self.master.destroy()


class HelpUserWindow(Menubar):
    '''
        In the class the user gets the information about the game
    '''

    def __init__(self, master):
        self.master = master
        self.creatMenuBar()
        debug('Test')

        self.label1 = Label(self.master, text="Find the Bug is a single-player puzzle video game. The objective of the game is to clear a rectangular board containing hidden \"mines\" or bombs without detonating any of them, with help from clues about the number of neighboring mines in each field. The game originates from the 1960s, and has been written for many computing platforms in use today. It has many variations and offshoots.", wraplength=400, justify='left')
        self.label1.grid()
        return super().__init__(master)
  
    def creatMenuBar(self):
        '''
            Overwrites the inherited method, so the windows, has another Menubar  
        '''
        self.menubar = Menu(self.master)
        self.filemenu = Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Exit", command=self.exitConfig)
        self.menubar.add_cascade(label="Menu", menu=self.filemenu)
        self.master.config(menu=self.menubar)


class EndGame(Menubar):
    '''
        Window for the result of the game
    '''

    def __init__(self, master, player, win, time):
        self.master = master
        self.win = win
        self.player = player
        self.time = time
        if self.win is False:
            showText = 'Sorry ' + self.player + ' you have lost the game.'
        else:
            showText = 'Nice ' + self.player + ' you have win the game. Your time was: ' + str(self.time) + ' seconds!'

        print(showText, self.player)
        self.label1 = Label(self.master, text=showText, wraplength=400, justify='left')
        self.label1.grid()
        return super().__init__(master)


class Configuration(Menubar):
    '''
        Configuration Window where the game can be set up. Choice of 3 different degree of difficulty
    '''

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

    def createRadioButtons(self):
        '''
            Create the Radiobuttons and set easy as the dafault value
        '''
        self.radiobutton1 = Radiobutton(self.master, text="Easy", variable=self.v, value=1)
        self.radiobutton2 = Radiobutton(self.master, text="Medium", variable=self.v, value=2)
        self.radiobutton3 = Radiobutton(self.master, text="Hard", variable=self.v, value=3)
        self.v.set(1)

    def destroyMenu(self):
        '''
            Destroy the current window
        '''
        self.master.destroy()

    def createGame(self):
        player = self.textfield.get("1.0", "end")
        player = player.strip()
        degree_of_difficulty = self.v.get()
        root2 = Toplevel(self.master)
        myGUI = Game(root2, player, degree_of_difficulty)
        Grid.rowconfigure(root2, 0, weight=1)
        Grid.columnconfigure(root2, 0, weight=1)
        root2.title("Find the Bug")
        root2.update()
        root2.minsize(root2.winfo_width(), root2.winfo_height())


class Game(Menubar):
    '''
        Game Window with the Buttons
    '''

    def __init__(self, master, player, degree_of_difficulty):
        self.degree_of_difficulty = degree_of_difficulty
        self.master = master
        self.player = player
        self.setGameFieldSize()
        self.createBoard()
        self.setUpFrame()
        self.createFirstLine()

        self.setUpImages()
        self.ButtonNameDict = {}
        for c in range(self.column):
            for r in range(1, self.row+1):
                self.btn = Button(self.frame, image=self.white, bg='#FFFFFF')
                self.btn.grid(column=c, row=r, sticky=N+S+E+W)
                self.btn.bind("<Button-1>", self.handleButtonClickLeft)
                self.btn.bind("<Button-3>", self.handleButtonClickRight)
                Grid.columnconfigure(self.frame, c, weight=1)
                Grid.rowconfigure(self.frame, r, weight=1)
                realR = r - 1
                self.name = str(c) + "," + str(realR)
                self.ButtonNameDict[self.name] = self.btn
        self.startTime = time()
        return super().__init__(master)

    def handleButtonClickRight(self, event):
        '''
            Handle the right click on a button. Search Bug image for the first click on a button.
            The next change it back to the white image.
            in: click event
            out: -
        '''
        if event.widget['bg'] == '#FF0000':
            event.widget.config(image=self.white, bg='#FFFFFF')
        else:
            event.widget.config(image=self.search_bug, bg='#FF0000')
 
    def handleButtonClickLeft(self, event):
        '''
            Handle the left click on a button
            in: click event
            out: -
        '''
        c, r = self.getRealButtonPosition(event)
        print(c, r)
        valueCell = self.board1.getValueFromBoard(c, r)

        logger1 = getLogger('myapp.area1')
        logger2 = getLogger('myapp.area2')

        logger1.debug('Test111')
        debug('Test1')





        print(valueCell)
        if event.widget['bg'] == '#FF0000':
            event.widget.config(bg='#FFFFFF')
        if valueCell == 10:
            print('You clicked on a mine')
            event.widget.config(image=self.bug)
            self.endGame(False, None)
        elif valueCell == 8:
            print("You didn't clicked on a mine")
            event.widget.config(image=self.eight)
        elif valueCell == 7:
            print("You didn't clicked on a mine")
            event.widget.config(image=self.seven)
        elif valueCell == 6:
            print("You didn't clicked on a mine")
            event.widget.config(image=self.six)
        elif valueCell == 5:
            print("You didn't clicked on a mine")
            event.widget.config(image=self.five)
        elif valueCell == 4:
            print("You didn't clicked on a mine")
            event.widget.config(image=self.four)
        elif valueCell == 3:
            print("You didn't clicked on a mine")
            event.widget.config(image=self.three)
        elif valueCell == 2:
            print("You didn't clicked on a mine")
            event.widget.config(image=self.two)
        elif valueCell == 1:
            print("You didn't clicked on a mine")
            event.widget.config(image=self.one)
        elif valueCell == 0:
            print("You didn't clicked on a mine")
            self.openOtherCells(event, c, r)
            event.widget.config(image=self.zero)
        self.board1.setValueFromBoard(c, r)
        print(c, r, 'new Vallue while clicked', self.board1.getValueFromBoard(c, r))
        event.widget.unbind('<Button-1>')
        event.widget.unbind('<Button-3>')
        print(self.board1.getBoard())
        self.checkVictory()

    def checkVictory(self):
        '''
            TODO explain th method
        '''
        clickedCells = self.board1.getClickedFieldsAmount()
        print(clickedCells)
        if clickedCells == self.clicksUntilVictory:
            print('You have won the Game')
            self.endTime = time()
            self.time = self.endTime - self.startTime
            self.time = round(self.time)
            self.endGame(True, self.time)

    def endGame(self, win, time):
        '''
            The player clicked on a mine
            do: Open all Buttons of the field
            in: -
            out: -
        '''
        print('Endgame')
        for cellname in self.ButtonNameDict.keys():
            name1 = cellname.split(',')
            c = name1[0]
            r = name1[1]
            # print(cellname, c, r)
            valueCell = self.board1.getValueFromBoard(int(c), int(r))
            self.changeImageOfCell(valueCell, cellname)
        self.configureEndGame(win, time)
    
    def configureEndGame(self, win, time):
        root2 = Toplevel(self.master)
        myGUI = EndGame(root2, self.player, win, time)
        Grid.rowconfigure(root2, 0, weight=1)
        Grid.columnconfigure(root2, 0, weight=1)
        root2.title("End Game")
        root2.update()
        root2.minsize(root2.winfo_width(), root2.winfo_height())

    def openOtherCells(self, event, c, r):
        '''
            Open all cell around the clicked zero
            do: Open a method from the logic and get a list. The List are the cells which should be programmly clicked
            in: column (c), row (r)
            out: -
        '''
        openFieldList = self.board1.getAllOtherOpenFields(c, r, [])
        for cell in openFieldList:
            c = cell[0]
            r = cell[1]
            valueCell = self.board1.getValueFromBoard(c, r)
            cellname = str(c) + ',' + str(r)
            self.changeImageOfCell(valueCell, cellname)
            self.board1.setValueFromBoard(c, r)
            print(c, r, 'new Vallue while clicked', self.board1.getValueFromBoard(c, r))
       
    def changeImageOfCell(self, valueCell, cellname):
        '''
            do: Change the image of a cell with the Buttonname and unbind the click event
            in: valueCell, cellname
            out: -
        '''
        if valueCell == 10:
            self.ButtonNameDict[cellname].config(image=self.bug)
        elif valueCell == 8:
            self.ButtonNameDict[cellname].config(image=self.eight)
        elif valueCell == 7:
            self.ButtonNameDict[cellname].config(image=self.seven)
        elif valueCell == 6:
            self.ButtonNameDict[cellname].config(image=self.six)
        elif valueCell == 5:
            self.ButtonNameDict[cellname].config(image=self.five)
        elif valueCell == 4:
            self.ButtonNameDict[cellname].config(image=self.four)
        elif valueCell == 3:
            self.ButtonNameDict[cellname].config(image=self.three)
        elif valueCell == 2:
            self.ButtonNameDict[cellname].config(image=self.two)
        elif valueCell == 1:
            self.ButtonNameDict[cellname].config(image=self.one)
        elif valueCell == 0:
            self.ButtonNameDict[cellname].config(image=self.zero)
        self.ButtonNameDict[cellname].unbind('<Button-1>')
        self.ButtonNameDict[cellname].unbind('<Button-3>')

    def setUpImages(self):
        '''
            The method set up all images for the game
            in: -
            out: -
        '''
        self.white = PhotoImage(file="assets/white.png")
        self.bug = PhotoImage(file="assets/bug.png")
        self.search_bug = PhotoImage(file="assets/search_bug.png")
        self.zero = PhotoImage(file="assets/zero.png")
        self.one = PhotoImage(file="assets/one.png")
        self.two = PhotoImage(file="assets/two.png")
        self.three = PhotoImage(file="assets/three.png")
        self.four = PhotoImage(file="assets/four.png")
        self.five = PhotoImage(file="assets/five.png")
        self.six = PhotoImage(file="assets/six.png")
        self.seven = PhotoImage(file="assets/seven.png")
        self.eight = PhotoImage(file="assets/eight.png")

    def getRealButtonPosition(self, event):
        '''
            Calculate the real position of the Button, because on row is used for the Game information
            in: click event
            out: position column, row
        '''
        gridDict = event.widget.grid_info()
        clickedRow = gridDict['row']
        clickedColumn = gridDict['column']
        clickedRow = clickedRow - 1
        return clickedColumn, clickedRow

    def setGameFieldSize(self):
        '''
            Check the input degree_of_difficulty and get the playground size
        '''
        if self.degree_of_difficulty == 1:
            self.column = 5
            self.row = 5
            self.mines = 4
        elif self.degree_of_difficulty == 2:
            self.column = 9
            self.row = 7
            self.mines = 10
        else:
            self.column = 18
            self.row = 10
            self.mines = 30
        self.clicksUntilVictory = (self.column * self.row) - self.mines
        print('Clicks until victory', self.clicksUntilVictory)

    def createBoard(self):
        '''
            Create Board with module logic, need the column, row and the nuber of mines for the game
        '''
        self.board1 = Board(self.column, self.row, self.mines, None)
        self.board1.createWarnFields()
        print(self.board1.getBoard())

    def setUpFrame(self):
        ''' 
            First setup the Frame and configure the grid
            Source: https://stackoverflow.com/questions/7591294/how-to-create-a-self-resizing-grid-of-buttons-in-tkinter
        '''
        self.frame = Frame(self.master)
        self.frame.grid(row=0, column=0, sticky=N+S+E+W)
        self.grid = Frame(self.frame)
        self.grid.grid(sticky=N+S+E+W, column=0, row=0)
        Grid.rowconfigure(self.frame, 0, weight=1)
        Grid.columnconfigure(self.frame, 0, weight=1)

    def createFirstLine(self):
        ''' 
            Create first line of the game field and configure the line of labels based on playing field width
        '''
        # create
        minesNumber = str(self.mines) + " Mines"
        self.time = Label(self.master, text=minesNumber)
        self.label1 = Label(self.frame, text="Welcome to Find the Bug")
        self.name = Label(self.frame, text=self.player)

        # configure
        self.time.grid(row=0, column=0, sticky="NW", columnspan=self.column)
        self.label1.grid(row=0, column=0, sticky="N", columnspan=self.column)
        self.name.grid(row=0, column=0, sticky="NE", columnspan=self.column)

    def destroyMenu(self):
        '''
            Destroy the current window
        '''
        self.master.destroy()


def main():
    '''
        TODO Docstring
    '''

    LOG_FILENAME = 'Debugfile.log'
    basicConfig(filename=LOG_FILENAME, level=DEBUG)


    root = Tk()
    config = Configuration(root)
    root.title("Find the Bug Configuration")
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.update()
    root.minsize(root.winfo_width(), root.winfo_height())
    root.mainloop()


if __name__ == "__main__":
    main()
