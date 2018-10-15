# Saper

Game saper written in Python 3 using built-in library Tkinter.

### Code features:
- Used simpler version of architectural pattern MVC (Model-View-Controller). Controller and Model are in the same class.

### Game features:
- You can enter your own dimensions of the board from 2x2 up to 15x15 and also number of mines from 0 to M*N (M-width of board; N-hight of board)
- New game button to start game with a new placement of mines.
- Restart button to start game with the same placement of mines as in last played game.
- Marking squares as flag ('there is a mine') or question mark('there might be a mine'). Squares marked with flag cannot be uncovered.
- Game can be won by marking all places with mines with flag and nothing else.
- You can type 'xyzzy' on keyboard to darken places where mines are.
- Game has stopwatch to measure your time.
