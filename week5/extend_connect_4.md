# Extending Connect4

Connect 4 is just one of many games that are won by creating a row of the player's pieces. In
this exercise we will extend our code to play a few more games. In the process, we will see how
to use and inherit from simpler classes to extend their capabilities.

Note: You'll need a completed `Board` class from the Connect Four exercise. I will provide one in
class that you can use if you did not have time to finish yesterday.

## Varying how many pieces in a row we look for

One of the simplest extensions we can make to our game is to make the umber of pieces in a row
required to win configurable.

- Add an add an attribute `needed_to_win` to `Board` by modifying the `__init__` method.
- Modify the `winsFor` method to check for a run of `needed_to_win` pieces.

## Varying how stones are placed

Maybe want to support games like tic-tac-toe where player can play on any open space rather than
only being able to play in the next open space in a column. Notice how there is some behavior that
we'll want to share (eg. clearing the board, checking for n-in-a-row) and some behavior we'll want
to be different (adding and removing pieces). This is a reasonable place to use inheritance.

1. Rename the your current `Board` class `Connect4Board` and create a new empty class called
`Board`. Have `Connect4Board` inherit from `Board`. Your code should looks something like:

```
class Board(object):
    pass


class Connect4Board(Board):
    ...
```

2. Now we can move any method that will be shared between tic-tac-toe boards and connect4 boards
to the `Board` class. (Hint: this is basically everything except `addMove`, `delMove` and methods
that call `addMove` or `delMove`.

3. Now create a `TicTacToeBoard` and implement `addMove`, `delMove`, and `hostGame`. eg.
```
class TicTacToeBoard(Board):
    def addMove(self, row, col, ox):
        """ Modifies this board by placing the given character/piece
            in the space at the given row and column.
        """
        pass

    def delMove(self, row, col):
        """ Modifies this board by removing the character/piece
            in the given row and column
        """
        pass

    def hostGame(self):
        pass
```

## Placing other shapes

Some related games (pente) support more that two players where each player gets their own tokens.
It turns out most of our `TicTacToeBoard` class is generic enough to support this; eg. `addMove`
just accepts a string to place in a cell. We'll just need to change `hostGame` to support more

Lets move the functions
for playing the game out of TicTacToe board to a separate TicTacToe class/program. Now "TicTacToeBoard"
can be something more general. Use this more general thing to make a pente game player.

## Capture rules/other win conditions

Pente actually has a rule that lets a player "caputure" their opponent's pieces. We can create a new
Pente Board with a special addMove and winsFor to add this feature.

## More?

There are many more games that introduce slight variations; how would you reorganize your code to add
support for [quarto](https://en.wikipedia.org/wiki/Quarto_(board_game))?
What about [connect6](https://en.wikipedia.org/wiki/Connect6)?

