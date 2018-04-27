from tkinter import *

# view1
class Menu:
    def __init__(self, win, control):
        self._window = win

        self._title_image = PhotoImage(file='images/t_title200x80px.png')
        self._labelTitle = Label(self._window, image=self._title_image)
        self._labelTitle.grid(row=0, columnspan=100, sticky="news")
        self._labelWidth = Label(self._window, text="Szerokość")
        self._labelWidth.grid(row=1, sticky="e")
        self._entryWidth = Entry(self._window)
        self._entryWidth.grid(row=1, column=1)
        self._labelHeight = Label(self._window, text="Wysokość")
        self._labelHeight.grid(row=2, sticky="e")
        self._entryHeight = Entry(self._window)
        self._entryHeight.grid(row=2, column=1)
        self._labelMines = Label(self._window, text="Ilość min")
        self._labelMines.grid(row=3, sticky="e")
        self._entryMines = Entry(self._window)
        self._entryMines.grid(row=3, column=1)
        self._buttonStart = Button(self._window, text="Nowa Gra")
        self._buttonStart.grid(columnspan=2)
        self._buttonRestart = Button(self._window, text="Restart", stat=DISABLED)
        self._buttonRestart.grid(columnspan=2)
        self._buttonStart.bind("<Button-1>", lambda event: control.newGame())
        self._buttonStart.bind("<Return>", lambda event: control.newGame())
        self._buttonRestart.bind("<Button-1>", lambda event: control.restartGame())
        self._buttonRestart.bind("<Return>", lambda event: control.restartGame())
        self._labelError = Label(self._window, text="", fg="red")

    def newGameStart(self):
        self._labelError.grid_forget()
        self._buttonRestart.config(stat=ACTIVE)

    def errorDisplay(self, comment):
        self._labelError.config(text=comment)
        self._labelError.grid(row=6, columnspan=2)

    def getEntryData(self):
        return self._entryWidth.get(), self._entryHeight.get(), self._entryMines.get()
