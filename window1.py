from Menu import Menu
from GameMap import GameMap
import tkinter as tk

class Window1:
    def __init__(self, controller):
        self._window = tk.Tk()
        self._ctrler = controller
        # ustawianie parametrów okna
        self._window.title("Saper")
        self._window.iconbitmap("icon.ico")
        x = (self._window.winfo_screenwidth() / 4)
        y = (self._window.winfo_screenheight() / 4)
        self._window.geometry('+%d+%d' % (x, y))

        self._window.bind("<Key>", lambda event: controller.keyPressed(event.char))  # wykrywanie wciskanych przycisków

        # view1
        self.menu = Menu(self._window, controller)
        # view2
        self.map = GameMap(self._window, controller)

        self.map.timer()

    def setController(self, controller):
        self._ctrler = controller

    def windowLoop(self):
        self._window.mainloop()
