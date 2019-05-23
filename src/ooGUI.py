# !/usr/bin/python
"""
    @ user : Niklas Hauschel
    @ e-mail: niklas.hauschel@web.de
    @ date : 22.06.2019
"""

from logging import *
import time as t
from datetime import *
from tkinter import *

from logic import Board

# Source for column row in tkinter https://diyodemag.com/education/secret_code_tkinter
# TODO --> erster Klick keine mine!

filename = 'ooGUI'


class Menubar:
    '''
        It is the definition of the Menubar, which can be inherit by the GUI's later
    '''
    def __init__(self, master):
        '''
            in: master frame
            do: Creates the menu for all of the windows
            out: -
        '''
        self.logNameClass = 'Menubar'
        logNameMethod = '__init__'
        log = getLogger(filename + '.' + self.logNameClass + '.' + logNameMethod)
        log.debug('Setup the Menubar class!')
        self.master = master
        self.creatMenuBar()

    def creatMenuBar(self):
        '''
            in: -
            do: Create the standard MenuBar for all of the windows
            out: -
            TODO: property
        '''
        logNameMethod = 'creatMenuBar'
        log = getLogger(filename + '.' + self.logNameClass + '.' + logNameMethod)
        log.debug('Creates a menu bar template')
        self.menubar = Menu(self.master)
        self.filemenu = Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Help", command=self.helpUser)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=self.exitWindow)
        self.menubar.add_cascade(label="Menu", menu=self.filemenu)
        self.master.config(menu=self.menubar)

    def helpUser(self):
        '''
            in: -
            do: Creates a new window, which descibes the rules of the game
            out: -
            TODO: property
        '''
        logNameMethod = 'helpUser'
        log = getLogger(filename + '.' + self.logNameClass + '.' + logNameMethod)
        log.debug('Creates a new window if the user needs help. Setup HelpUserWindow!')
        root2 = Toplevel(self.master)
        myGUI = HelpUserWindow(root2)
        Grid.rowconfigure(root2, 0, weight=1)
        Grid.columnconfigure(root2, 0, weight=1)
        root2.title("Help with Find the Bug")
        root2.update()
        root2.minsize(root2.winfo_width(), root2.winfo_height())

    def exitWindow(self):
        '''
            in: -
            do: Close the window
            out: -
            TODO: property
        '''
        logNameMethod = 'exitWindow'
        log = getLogger(filename + '.' + self.logNameClass + '.' + logNameMethod)
        log.debug('Destory the window')
        self.master.destroy()


class HelpUserWindow(Menubar):
    '''
        In the class the user gets the information about the game
    '''

    def __init__(self, master):
        '''
            in: master frame
            do: Create the window for the information about the game
            out: -
            TODO: property
        '''
        self.logNameClass = 'HelpUserWindow'
        logNameMethod = '__init__'
        log = getLogger(filename + '.' + self.logNameClass + '.' + logNameMethod)
        log.debug('Setup the {} Window'.format(self.setLoggerClass))
        self.master = master
        self.creatMenuBar()
        self.label1 = Label(self.master,
                            text="Find the Bug is a single-player puzzle video game. The objective " +
                            "of the game is to clear a rectangular board containing hidden \"mines\" " +
                            "or bombs without detonating any of them, with help from clues " +
                            "about the number of neighboring mines in each field. The game " +
                            "originates from the 1960s, and has been written for many " +
                            "computing platforms in use today. It has many variations and offshoots.",
                            wraplength=400, justify='left')
        self.label1.grid()
        return super().__init__(master)

    def creatMenuBar(self):
        '''
            in: -
            do: Overwrites the inherited method, so the windows, has another Menubar
            out: -
            TODO: property
        '''
        logNameMethod = 'creatMenuBar'
        log = getLogger(filename + '.' + self.logNameClass + '.' + logNameMethod)
        log.debug('Overwrite inherited method, which changes the Menubar in the current window')
        self.menubar = Menu(self.master)
        self.filemenu = Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Exit", command=self.exitWindow)
        self.menubar.add_cascade(label="Menu", menu=self.filemenu)
        self.master.config(menu=self.menubar)


class EndGame(Menubar):
    '''
        Window for the result of the game
    '''

    def __init__(self, master, player, win, time):
        '''
            in: master frame, player name, win True or False, time
            do: create the window at the end of the game
            out: -
            TODO: property
        '''
        self.logNameClass = 'EndGame'
        logNameMethod = '__init__'
        log = getLogger(filename + '.' + self.logNameClass + '.' + logNameMethod)
        log.debug('Setup the window {} '.format(self.logNameClass))
        self.master = master
        self.win = win
        self.player = player
        self.time = time
        if self.win is False:
            showText = 'Sorry ' + self.player + ' you have lost the game.'
            log.debug('The player {} have lost the game'.format(self.player))
        else:
            showText = 'Nice ' + self.player + ' you have won the game. Your time was: ' + str(self.time) + ' seconds!'
            log.debug('The The player {} have won the game in {} seconds'.format(self.player, str(self.time)))
        self.label1 = Label(self.master, text=showText, wraplength=400, justify='left')
        self.label1.grid()
        return super().__init__(master)


class Configuration(Menubar):
    '''
        Configuration Window where the game can be set up. Choice of 3 different degree of difficulty
    '''

    def __init__(self, master):
        '''
            in: master frame
            do: create the configruation window
            out: -
            TODO: property
        '''
        self.logNameClass = 'Configuration'
        logNameMethod = '__init__'
        log = getLogger(filename + '.' + self.logNameClass + '.' + logNameMethod)
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
            in: -
            do: Create the Radiobuttons and set easy as the dafault value
            out: -
            TODO: property
        '''
        self.radiobutton1 = Radiobutton(self.master, text="Easy", variable=self.v, value=1)
        self.radiobutton2 = Radiobutton(self.master, text="Medium", variable=self.v, value=2)
        self.radiobutton3 = Radiobutton(self.master, text="Hard", variable=self.v, value=3)
        self.v.set(1)

    def createGame(self):
        '''
            in: -
            do: configure the game window
            out: -
            TODO: property
        '''
        player = self.textfield.get("1.0", "end")
        player = player.strip()
        if player == '':
            player = 'Layer 8 error'
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
        '''
            in: master frame, player name, degree_of_difficulty
            do: create the game window
            out: -
            TODO: property
        '''
        self.logNameClass = 'Game'
        logNameMethod = '__init__'
        log = getLogger(filename + '.' + self.logNameClass + '.' + logNameMethod)
        log.debug('Setup the Game window!')
        self.degree_of_difficulty = degree_of_difficulty
        self.master = master
        self.player = player
        self.setGameFieldSize()
        self.createBoard()
        self.setUpFrame()
        self.createFirstLine()

        self.setUpImages()
        self.ButtonNameDict = {}

        # loop which creates the window
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
                log.debug("Button with column {} and row {} will be created " +
                          "with the click event. In the background it has the row {}"
                          .format(c, realR, r))

        self.startTime = t.time()
        log.debug('The time for the game has been started')
        log.debug('Next step is that the class inherits everything from the inheriting class.')
        return super().__init__(master)

    def handleButtonClickRight(self, event):
        '''
            in: click event
            do: Handle the right click on a button. Search Bug image for the first click on a button.
            The next change it back to the white image.
            out: -
            TODO: property
        '''
        logNameMethod = 'handleButtonClickRight'
        log = getLogger(filename + '.' + self.logNameClass + '.' + logNameMethod)
        if event.widget['bg'] == '#FF0000':
            event.widget.config(image=self.white, bg='#FFFFFF')
            log.debug('Clicked Button is red, so the background color change to white')
        else:
            event.widget.config(image=self.search_bug, bg='#FF0000')
            log.debug('Clicked Button is white, so the background color change to red')

    def handleButtonClickLeft(self, event):
        '''
            in: click event
            do: Handle the left click on a button
            out: -
            TODO: property
        '''
        logNameMethod = 'handleButtonClickLeft'
        log = getLogger(filename + '.' + self.logNameClass + '.' + logNameMethod)
        c, r = self.getRealButtonPosition(event)
        valueCell = self.board1.getValueFromBoard(c, r)
        log.debug('Button were clicked in column {} and row {} and have the value {}'.format(c, r, valueCell))
        if event.widget['bg'] == '#FF0000':
            event.widget.config(bg='#FFFFFF')
            log.debug('Clicked Button is red and so the background color change to white')
        if valueCell == 10:
            event.widget.config(image=self.bug)
            log.debug('Clicked Button is a bug, so the image change to the bug. Next step is that the game is lost')
            self.endGame(False, None)
        elif valueCell == 8:
            log.debug('Clicked Button is a 8, so the image change to 8')
            event.widget.config(image=self.eight)
        elif valueCell == 7:
            log.debug('Clicked Button is a 7, so the image change to 7')
            event.widget.config(image=self.seven)
        elif valueCell == 6:
            log.debug('Clicked Button is a 6, so the image change to 6')
            event.widget.config(image=self.six)
        elif valueCell == 5:
            log.debug('Clicked Button is a 5, so the image change to 5')
            event.widget.config(image=self.five)
        elif valueCell == 4:
            log.debug('Clicked Button is a 4, so the image change to 4')
            event.widget.config(image=self.four)
        elif valueCell == 3:
            log.debug('Clicked Button is a 3, so the image change to 3')
            event.widget.config(image=self.three)
        elif valueCell == 2:
            log.debug('Clicked Button is a 2, so the image change to 2')
            event.widget.config(image=self.two)
        elif valueCell == 1:
            log.debug('Clicked Button is a 1, so the image change to 1')
            event.widget.config(image=self.one)
        elif valueCell == 0:
            log.debug('Clicked Button is a 0, so the image change to 0.' +
                      'Next step is that other cells around the button will automatically clicked')
            self.openOtherCells(event, c, r)
            event.widget.config(image=self.zero)
        self.board1.setValueFromBoard(c, r)
        log.debug('The Button gets a new number 11 in the logic in column {} and row {}. ' +
                  'The Button will be unbind from the click event'.format(c, r))
        event.widget.unbind('<Button-1>')
        event.widget.unbind('<Button-3>')
        log.debug('Current Gamefield after a click on a field\n{}'.format(self.board1.getBoard()))
        self.checkVictory()

    def checkVictory(self):
        '''
            in: click event
            do: Check if the game is over. At the beginning there are unclicked buttons(the product of column and row).
                For every new click the game check if there are only the same number of unclicked buttons as the
                number of mines.
            out: -
            TODO: property
        '''
        logNameMethod = 'checkVictory'
        log = getLogger(filename + '.' + self.logNameClass + '.' + logNameMethod)
        clickedCells = self.board1.getClickedFieldsAmount()
        log.debug('Number of clicked Cells so far {}'.format(clickedCells))
        if clickedCells == self.clicksUntilVictory:
            self.endTime = t.time()
            self.time = self.endTime - self.startTime
            self.time = round(self.time)
            log.debug('You have won the Game and takes {} seconds'.format(self.time))

            self.endGame(True, self.time)

    def endGame(self, win, time):
        '''
            in: win True or False, time
            do: The player clicked on a mine. Open all Buttons of the field
            out: -
            TODO: property
        '''
        logNameMethod = 'endGame'
        log = getLogger(filename + '.' + self.logNameClass + '.' + logNameMethod)
        log.debug('The game is over')
        for cellname in self.ButtonNameDict.keys():
            name1 = cellname.split(',')
            c = name1[0]
            r = name1[1]
            valueCell = self.board1.getValueFromBoard(int(c), int(r))
            log.debug('Cellname {}, column {}, Row {}, ValueCell {}. Next step is that each button will change ' +
                      'the image if the valuecell is not 11'.format(cellname, c, r, valueCell))
            if valueCell != 11:
                self.changeImageOfCell(valueCell, cellname)
        self.configureEndGame(win, time)

    def configureEndGame(self, win, time):
        '''
            in: win True or False, time
            do: configure the endgame window
            out: -
            TODO: property
        '''
        logNameMethod = 'configureEndGame'
        log = getLogger(filename + '.' + self.logNameClass + '.' + logNameMethod)
        log.debug('Create Endgame Window')
        root2 = Toplevel(self.master)
        myGUI = EndGame(root2, self.player, win, time)
        Grid.rowconfigure(root2, 0, weight=1)
        Grid.columnconfigure(root2, 0, weight=1)
        root2.title("End Game")
        root2.update()
        root2.minsize(root2.winfo_width(), root2.winfo_height())

    def openOtherCells(self, event, c, r):
        '''
            in: column (c), row (r)
            do: Open all cell around the clicked zero. Open a method from the logic and get a list.
                The List are the cells which should be programmly clicked
            out: -
            TODO: property
        '''
        logNameMethod = 'openOtherCells'
        log = getLogger(filename + '.' + self.logNameClass + '.' + logNameMethod)
        log.debug('A cell with the value 0 were clicked. Next step is to get the cells around the button')
        openFieldList = self.board1.getAllOtherOpenFields(c, r, [])
        for cell in openFieldList:
            c = cell[0]
            r = cell[1]
            valueCell = self.board1.getValueFromBoard(c, r)
            cellname = str(c) + ',' + str(r)
            self.board1.setValueFromBoard(c, r)
            valueCell2 = self.board1.getValueFromBoard(c, r)
            self.changeImageOfCell(valueCell, cellname)
            log.debug('Cellname {}, column {}, Row {}, ValueCell {}, new valuecell {}'
                      .format(cellname, c, r, valueCell, valueCell2))

    def changeImageOfCell(self, valueCell, cellname):
        '''
            in: valueCell, cellname
            do: Change the image of a cell with the Buttonname and unbind the click event
            out: -
            TODO: property
        '''
        logNameMethod = 'changeImageOfCell'
        log = getLogger(filename + '.' + self.logNameClass + '.' + logNameMethod)
        if valueCell == 10:
            log.debug('Clicked Button is a 10, so the image change to Bug')
            self.ButtonNameDict[cellname].config(image=self.bug)
        elif valueCell == 8:
            self.ButtonNameDict[cellname].config(image=self.eight)
            log.debug('Clicked Button is a 8, so the image change to 8')
        elif valueCell == 7:
            log.debug('Clicked Button is a 7, so the image change to 7')
            self.ButtonNameDict[cellname].config(image=self.seven)
        elif valueCell == 6:
            log.debug('Clicked Button is a 6, so the image change to 6')
            self.ButtonNameDict[cellname].config(image=self.six)
        elif valueCell == 5:
            log.debug('Clicked Button is a 5, so the image change to 5')
            self.ButtonNameDict[cellname].config(image=self.five)
        elif valueCell == 4:
            log.debug('Clicked Button is a 4, so the image change to 4')
            self.ButtonNameDict[cellname].config(image=self.four)
        elif valueCell == 3:
            log.debug('Clicked Button is a 3, so the image change to 3')
            self.ButtonNameDict[cellname].config(image=self.three)
        elif valueCell == 2:
            log.debug('Clicked Button is a 2, so the image change to 2')
            self.ButtonNameDict[cellname].config(image=self.two)
        elif valueCell == 1:
            log.debug('Clicked Button is a 1, so the image change to 1')
            self.ButtonNameDict[cellname].config(image=self.one)
        elif valueCell == 0:
            log.debug('Clicked Button is a 0, so the image change to 0')
            self.ButtonNameDict[cellname].config(image=self.zero)
        log.debug('Unbind clickevents for Clicked Button')
        self.ButtonNameDict[cellname].unbind('<Button-1>')
        self.ButtonNameDict[cellname].unbind('<Button-3>')

    def setUpImages(self):
        '''
            in: -
            do: The method set up all images for the game
            out: -
            TODO: property
        '''
        logNameMethod = 'setUpImages'
        log = getLogger(filename + '.' + self.logNameClass + '.' + logNameMethod)
        log.debug('Setup once all images for the game')
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
            in: click event
            do: Calculate the real position of the Button, because on row is used for the Game information
            out: position column, row
            TODO: property
        '''
        logNameMethod = 'getRealButtonPosition'
        log = getLogger(filename + '.' + self.logNameClass + '.' + logNameMethod)
        gridDict = event.widget.grid_info()
        clickedRow = gridDict['row']
        clickedColumn = gridDict['column']
        clickedRowNew = clickedRow - 1
        log.debug('Because of the first line, one must be subtracted in each one of the lines. ' +
                  'row {} column {}, real row {} '.format(clickedRow, clickedColumn, clickedRowNew))
        return clickedColumn, clickedRowNew

    def setGameFieldSize(self):
        '''
            in: -
            do: Check the input degree_of_difficulty and get the playground size
            out: -
            TODO: proptery
        '''
        logNameMethod = 'setGameFieldSize'
        log = getLogger(filename + '.' + self.logNameClass + '.' + logNameMethod)
        if self.degree_of_difficulty == 1:
            self.column = 5
            self.row = 5
            self.mines = 4
            log.debug('The player picked the easy degree. So the Game has {} columns, {} rows and {} mines'
                      .format(self.column, self.row, self.mines))
        elif self.degree_of_difficulty == 2:
            self.column = 9
            self.row = 7
            self.mines = 10
            log.debug('The player picked the medium degree. So the Game has {} columns, {} rows and {} mines'
                      .format(self.column, self.row, self.mines))
        else:
            self.column = 18
            self.row = 10
            self.mines = 30
            log.debug('The player picked the hard degree. So the Game has {} columns, {} rows and {} mines'
                      .format(self.column, self.row, self.mines))
        self.clicksUntilVictory = (self.column * self.row) - self.mines
        print('Clicks until victory', self.clicksUntilVictory)

    def createBoard(self):
        '''
            in: -
            do: Create Board with module logic, need the column, row and the nuber of mines for the game
            out: -
            TODO: property
        '''
        logNameMethod = 'createBoard'
        log = getLogger(filename + '.' + self.logNameClass + '.' + logNameMethod)
        log.debug('Give the following information to the logic modul. ' +
                  'So the Game has {} columns, {} rows and {} mines'.format(self.column, self.row, self.mines))
        self.board1 = Board(self.column, self.row, self.mines, None)
        self.board1.isBoardSolvable()

        log.debug('\n{}'.format(self.board1.getBoard()))

    def setUpFrame(self):
        '''
            in: -
            do: First setup the Frame and configure the grid
            out: -
            TODO: property
            Source: https://stackoverflow.com/questions/7591294/how-to-create-a-self-resizing-grid-of-buttons-in-tkinter
        '''
        logNameMethod = 'setUpFrame'
        log = getLogger(filename + '.' + self.logNameClass + '.' + logNameMethod)
        log.debug('Setup the postion of the buttons')
        self.frame = Frame(self.master)
        self.frame.grid(row=0, column=0, sticky=N+S+E+W)
        self.grid = Frame(self.frame)
        self.grid.grid(sticky=N+S+E+W, column=0, row=0)
        Grid.rowconfigure(self.frame, 0, weight=1)
        Grid.columnconfigure(self.frame, 0, weight=1)

    def createFirstLine(self):
        '''
            in: -
            do: Create first line of the game field and configure the line of labels based on playing field width
            out: -
            TODO: property
        '''
        logNameMethod = 'createFirstLine'
        log = getLogger(filename + '.' + self.logNameClass + '.' + logNameMethod)

        # create
        log.debug('Creates the first line of the game with number of bugs, Welcome and player name')
        minesNumber = str(self.mines) + " Bugs"
        self.time = Label(self.master, text=minesNumber)
        self.label1 = Label(self.frame, text="Welcome to Find the Bug")
        self.name = Label(self.frame, text=self.player)

        # configure
        log.debug('Configure the first line')
        self.time.grid(row=0, column=0, sticky="NW", columnspan=self.column)
        self.label1.grid(row=0, column=0, sticky="N", columnspan=self.column)
        self.name.grid(row=0, column=0, sticky="NE", columnspan=self.column)


def main():
    '''
        in: -
        do: main
        out: -
    '''

    LOG_FILENAME = 'Debugfile.log'
    basicConfig(filename=LOG_FILENAME, level=DEBUG)
    debug('Start the game on:' + str(datetime.today()))
    debug('Setup the configuration Window')
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
