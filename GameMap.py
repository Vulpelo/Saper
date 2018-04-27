from tkinter import *
from Button import MButton
import time

# view2
class GameMap:
    def __init__(self, win, controller, positionx=3, positiony=1):
        self._controller = controller
        self._posx = positionx
        self._posy = positiony
        self._window = win
        self._button_map = []
        self._markedMines = 0

        self._timeStarted = False
        self._timeGoing = False
        self._time = time.time()
        self._flag_image = PhotoImage(file='images/t_flag20px.png')
        self._mine_image = PhotoImage(file='images/t_mine20px.png')

        self._textMarkedMines = StringVar()
        self._textNumberOfMines = StringVar()
        self._textTimer = StringVar()
        self._textTimer.set("0")

        self._labelWinLost = Label(self._window, text="white")
        self._labelEmpty = Label(self._window, image='', width="2")
        self._labelMarkedMines = Label(self._window, textvariable=self._textMarkedMines)
        self._labelMarkedIcon = Label(self._window, image=self._flag_image)
        self._labelMines = Label(self._window, textvariable=self._textNumberOfMines)
        self._labelMinesIcon = Label(self._window, image=self._mine_image)
        self._labelTimer = Label(self._window, textvariable=self._textTimer)

    def new(self, height, width, mines):
        self._markedMines = 0
        self._textNumberOfMines.set(str(mines))

        self._textMarkedMines.set(": 0")

        self._labelWinLost.config(text="", bg="white")
        self._labelWinLost.grid(column=self._posx, row=self._posy, columnspan=width, sticky="news")
        self._labelTimer.grid(column=self._posx + width+1, row=self._posy, columnspan=2)

        self._labelEmpty.grid(column=width + self._posx + 1, row=self._posy + 1, rowspan=2)

        self._labelMinesIcon.grid(column=width + self._posx + 2, row=self._posy + 1)
        self._labelMines.grid(column=width + self._posx + 3, row=self._posy + 1)

        self._labelMarkedIcon.grid(column=width + self._posx + 2, row=self._posy + 2)
        self._labelMarkedMines.grid(column=width + self._posx + 3, row=self._posy + 2)
        self.drawButtons(width, height)
        self._timeStarted = True
        self._timeGoing = False

    def lost(self, x, y):
        self._labelWinLost.config(text="YOU LOST", bg="red")
        [[xx.disable() for xx in yy] for yy in self._button_map]
        self._button_map[y][x].mark(marked="minered")
        self._timeGoing = False

    def win(self):
        self._labelWinLost.config(text="YOU WIN", bg="green")
        [[x.disable() for x in y] for y in self._button_map]
        self._timeGoing = False

    def setButtonSign(self, pos_x, pos_y, what):
        if what == "questionmark":
            self._markedMines -= 1
            self._button_map[pos_y][pos_x].active()
            self._button_map[pos_y][pos_x].mark("questionmark")
        elif what == "empty":
            self._button_map[pos_y][pos_x].mark("empty")
        elif what == "flag":
            self._markedMines += 1
            self._button_map[pos_y][pos_x].disable()
            self._button_map[pos_y][pos_x].mark("flag")
        self._textMarkedMines.set(": " + str(self._markedMines))

    def showMinePlace(self, x, y, what=""):
        self._button_map[y][x].mark(marked="highlight")
        if what != "onlyColor":
            self._button_map[y][x].mark(marked="mine")

    def uncoverPlace(self, x, y, number):
        self._button_map[y][x].uncover(number)

    def drawButtons(self, width, height):
        [[y.destroy() for y in x] for x in self._button_map]
        self._button_map = [[MButton(self._window, i, j, self._controller.leftClick, self._controller.rightClick,
                                     i + self._posx, j + self._posy + 1)
                             for i in range(width)] for j in range(height)]

    def timer(self):
        if self._timeGoing:
            self._textTimer.set( str("%3.1f"%(time.time() - self._time)) )
        elif self._timeStarted:
            self._time = time.time()
            self._textTimer.set(str(0))
            self._timeGoing = True
            self._timeStarted = False
        self._window.after(100, self.timer)
