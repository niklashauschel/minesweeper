from tkinter import *

# zwei Buttons: Einer um die Anwendung zu verlassen (QUIT) und der andere mit dem Text "Hello" startet die Methode write_slogan, die dann entsprechenden Text ausgibt

class Configuration:
    def __init__(self, master):
        self.master = master
        self.v = IntVar()

        # self.frame = Frame(master)

        # self.frame.grid()

        self.label1 = Label(self.master, text='Enter your Name')
        self.textfield = Text(self.master, width=15, height=3)
        self.radiobutton1 = Radiobutton(self.master, text="One", variable=self.v, value=1)
        self.radiobutton2 = Radiobutton(self.master, text="Two", variable=self.v, value=2)
        self.radiobutton3 = Radiobutton(self.master, text="Three", variable=self.v, value=3)

        self.button = Button(self.master, text="QUIT", fg ='red', bg = 'black', command=self.destroyMenu)
        self.buttonNewWindow = Button(self.master, text="New", fg ='red', bg = 'black', command=self.goto)


        self.label1.grid(row=0, column=0, columnspan=2, sticky="N")
        self.textfield.grid(row=1, column=0, rowspan=1, columnspan=2, sticky="NESW")
        self.radiobutton1.grid(row=2, column=0, columnspan=2, sticky="N")
        self.radiobutton2.grid(row=3, column=0, columnspan=2, sticky="N")
        self.radiobutton3.grid(row=4, column=0, columnspan=2, sticky="N")

        self.button.grid(row=5, column=0, sticky="W")
        self.buttonNewWindow.grid(row=5, column=1, sticky="E")

    def destroyMenu(self):
        self.master.destroy()

    def goto(self):
        player = self.textfield.get("1.0", "end")
        degree_of_difficulty = 1
        root2 = Toplevel(self.master)
        myGUI = Game(root2, player, degree_of_difficulty)
        root2.title("Minesweeper Game")
        root2.grid_rowconfigure(0, weight=1)
        root2.grid_columnconfigure(0, weight=1)
        root2.update()
        root2.minsize(root2.winfo_width(), root2.winfo_height())
        root2.geometry('400x400')

def endGame():
    print('TODO Endgame')

def handleButtonClickRight(event):
    if event.widget['text'] == 'x':
        print('You clicked on a mine')
        endGame()
    else:
        print("You didn't clicked on a mine")
    print("hi rigth", event.widget['text'])
    event.widget.config(bg='red', image='')
    event.widget.unbind('<Button-1>')
    event.widget.unbind('<Button-3>')

    

def handleButtonClickLeft(event):
    if event.widget['bg'] == 'blue':
        event.widget.config(bg='white')
    else:
        event.widget.config(bg='blue')
    print("hi left", event.widget['text'])



class Game:
     
    def __init__(self, master, player, degree_of_difficulty):
        self.master = master
        self.player = player
        self.frame = Frame(master)

        rangex = 0
        rangey = 0
        if degree_of_difficulty == 1:
            rangex = 10
            rangey = 10

        Grid.rowconfigure(self.master, 0, weight=1)
        Grid.columnconfigure(self.master, 0, weight=1)
        self.frame.grid(row=0, column=0, sticky=N+S+E+W)
        self.grid = Frame(self.frame)
        self.grid.grid(sticky=N+S+E+W, column=0, row=0)
        Grid.rowconfigure(self.frame, 0, weight=1)
        Grid.columnconfigure(self.frame, 0, weight=1)

        self.time = Label(self.master, text="91 Sekunden")
        self.label1 = Label(self.frame, text="Welcome to Minesweeper")
        self.name = Label(self.frame, text=self.player)
        self.time.grid(row=0, column=0, sticky="NW", columnspan=10)
        self.label1.grid(row=0, column=0, sticky="N", columnspan=10)
        self.name.grid(row=0, column=00, sticky="NE", columnspan=10)

        self.photo = PhotoImage(file="imagen.png")
        #self.photo2 = self.photo.subsample(10, 10)
        
        # source: https://stackoverflow.com/questions/7591294/how-to-create-a-self-resizing-grid-of-buttons-in-tkinter
        

        for x in range(rangex):
            for y in range(1, rangey):
                name = str(x) + " " + str(y)
                if(x==0 and y==1):
                    #btn = Button(self.frame, text='x', width="1",height="1")
                    btn = Button(self.frame, text='x', image=self.photo)
                else:
                    #btn = Button(self.frame, text=name, width="1",height="1")
                     btn = Button(self.frame, text=name, image=self.photo)

                btn.grid(column=x, row=y, sticky=N+S+E+W)
                btn.bind("<Button-1>", handleButtonClickRight)
                btn.bind("<Button-3>", handleButtonClickLeft)
                Grid.columnconfigure(self.frame, x, weight=1)
                Grid.rowconfigure(self.frame, y, weight=1)
   

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