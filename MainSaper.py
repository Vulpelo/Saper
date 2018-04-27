import random
import MyError

# controller
class Saper:
    def __init__(self):
        self._writtenCode = ""
        self._clearedPlaces = 0
        self._gameEnded = False
        self._firstGameLunch = False
        self._mines = 0
        self._markedMines = 0
        self._correctMarkedMines = 0
        self._map_width = 0
        self._map_height = 0
        self._mine_map = []

    def setModel(self, view):
        self._view = view

    def keyPressed(self, char):
        self._writtenCode = char + self._writtenCode[0:5]
        self.gameCodes()

    def gameCodes(self):
        if "xyzzy" in self._writtenCode[::-1]:
            self._writtenCode = ""
            self.showMines(what="onlyColor")

    def getAndSetEnteredData(self):
        self._map_width, self._map_height, self._mines = self._view.menu.getEntryData()
        self._map_width = int(self._map_width)
        self._map_height = int(self._map_height)
        self._mines = int(self._mines)
        if not 2 <= self._map_width <= 15 or not 2 <= self._map_height <= 15 or \
                not 0 <= self._mines <= self._map_width * self._map_height:
            raise MyError.WrongDataException("")
        self._view.map.new(self._map_height, self._map_width, self._mines)
        self.drawGameMap()
        self._view.menu.newGameStart()
        self._clearedPlaces = 0
        self._firstGameLunch = True

    def newGame(self):
        self._markedMines = 0
        self._correctMarkedMines = 0
        self._gameEnded = False
        try:
            self.getAndSetEnteredData()
        except ValueError:
            self._view.menu.errorDisplay("Niepoprawne dane")
        except MyError.WrongDataException:
            self._view.menu.errorDisplay("Złe wymiary lub zła ilość min")

    def restartGame(self):
        if self._firstGameLunch:
            self._markedMines = 0
            self._correctMarkedMines = 0
            self._gameEnded = False
            for i in range(self._map_height):
                for j in range(self._map_width):
                    self._mine_map[i][j] = self._mine_map[i][j][0] + "n"
            self._view.map.new(self._map_height, self._map_width, self._mines)

    def drawGameMap(self):
        rd = random.sample(range(0, self._map_width * self._map_height), self._mines)
        self._mine_map = [["Mn" if j * self._map_width + i in rd else "0n" for i in range(self._map_width)]
                          for j in range(self._map_height)]
        self._mine_map = [["Mn" if self._mine_map[j][i][0] == "M" else str(self.countNearMines(i, j)) + "n" for i in
                           range(self._map_width)] for j in range(self._map_height)]

    def countNearMines(self, x, y) -> int:
        count = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i + y < 0 or j + x < 0:
                    continue
                try:
                    if self._mine_map[i + y][j + x][0] == "M":
                        count += 1
                except IndexError:
                    continue
        return count

    def leftClick(self, x, y):
        if self._mine_map[y][x][0] == "M":
            self._gameEnded = True
            self.showMines()
            self._view.map.lost(x, y)
        else:
            if self._mine_map[y][x][0] == "0":
                self._clearedPlaces += self.uncoverEmptyMapArea(x, y)
            else:
                self._clearedPlaces += 1
                self._view.map.uncoverPlace(x, y, int(self._mine_map[y][x][0]))
            self._mine_map[y][x] = self._mine_map[y][x][0] + "o"
            self.didWin()

    def rightClick(self, pos_x, pos_y):
        if not self._gameEnded and self._mine_map[pos_y][pos_x][1] != "o":
            if self._mine_map[pos_y][pos_x][1] == "f":
                self._markedMines -= 1
                self._mine_map[pos_y][pos_x] = self._mine_map[pos_y][pos_x][0] + "q"
                if self._mine_map[pos_y][pos_x][0] == "M":
                    self._correctMarkedMines -= 1
                self._view.map.setButtonSign(pos_x, pos_y, "questionmark")
            elif self._mine_map[pos_y][pos_x][1] == "q":
                self._mine_map[pos_y][pos_x] = self._mine_map[pos_y][pos_x][0] + "n"
                self._view.map.setButtonSign(pos_x, pos_y, "empty")
            else:
                self._mine_map[pos_y][pos_x] = self._mine_map[pos_y][pos_x][0] + "f"
                self._markedMines += 1
                if self._mine_map[pos_y][pos_x][0] == "M":
                    self._correctMarkedMines += 1
                self._view.map.setButtonSign(pos_x, pos_y, "flag")
            self.didWin()

    def showMines(self, what=""):
        for j in range(self._map_height):
            for i in range(self._map_width):
                if self._mine_map[j][i][0] == "M":
                    self._view.map.showMinePlace(i, j, what)

    def uncoverEmptyMapArea(self, x, y):
        uncovered = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                try:
                    if y + i < 0 or x + j < 0 or self._mine_map[y + i][x + j][1] == "f":
                        continue
                    elif self._mine_map[y + i][x + j][1] in "nq":
                        uncovered += 1
                        self._mine_map[y + i][x + j] = self._mine_map[y + i][x + j][0] + "o"
                        self._view.map.uncoverPlace(x + j, y + i, int(self._mine_map[y + i][x + j][0]))
                        if self._mine_map[y + i][x + j][0] == "0":
                            uncovered += self.uncoverEmptyMapArea(x + j, y + i)
                except IndexError:
                    continue
        return uncovered

    def didWin(self):
        if self._mines == self._correctMarkedMines == self._markedMines or \
                self._clearedPlaces == self._map_width * self._map_height - self._mines:
            self._gameEnded = True
            self._view.map.win()
