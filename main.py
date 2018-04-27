from window1 import Window1
from MainSaper import Saper

if __name__ == '__main__':
    gameC = Saper()
    gameV = Window1(gameC)
    gameC.setModel(gameV)
    gameV.windowLoop()
