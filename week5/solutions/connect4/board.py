def inarow_Neast(ch, r_start, c_start, A, N):
    """Starting from (row, col) of (r_start, c_start)
       within the 2d list-of-lists A (array),
       returns True if there are N ch's in a row
       heading east and returns False otherwise.
    """
    H = len(A)
    W = len(A[0])
    if r_start < 0 or r_start > H - 1:
        return False # out of bounds row
    if c_start < 0 or c_start + (N-1) > W - 1:
        return False # o.o.b. col
    # loop over each location _offset_ i
    for i in range(N):
        if A[r_start][c_start+i] != ch: # a mismatch!
            return False
    return True  # all offsets succeeded, so we return True

def inarow_Nsouth(ch, r_start, c_start, A, N):
    """Starting from (row, col) of (r_start, c_start)
       within the 2d list-of-lists A (array),
       returns True if there are N ch's in a row
       heading south and returns False otherwise.
    """
    H = len(A)
    W = len(A[0])
    if r_start < 0 or r_start + (N-1) > H - 1:
        return False # out of bounds row
    if c_start < 0 or c_start > W - 1:
        return False # o.o.b. col
    # loop over each location _offset_ i
    for i in range(N):
        if A[r_start+i][c_start] != ch: # a mismatch!
            return False
    return True  # all offsets succeeded, so we return True

def inarow_Nnortheast(ch, r_start, c_start, A, N):
    """Starting from (row, col) of (r_start, c_start)
       within the 2d list-of-lists A (array),
       returns True if there are N ch's in a row
       heading northeast and returns False otherwise.
    """
    H = len(A)
    W = len(A[0])
    if r_start - (N-1) < 0 or r_start > H - 1:
        return False # out of bounds row
    if c_start < 0 or c_start + (N-1) > W - 1:
        return False # o.o.b. col
    # loop over each location _offset_ i
    for i in range(N):
        if A[r_start-i][c_start+i] != ch: # a mismatch!
            return False
    return True  # all offsets succeeded, so we return True

def inarow_Nsoutheast(ch, r_start, c_start, A, N):
    """Starting from (row, col) of (r_start, c_start)
       within the 2d list-of-lists A (array),
       returns True if there are N ch's in a row
       heading southeast and returns False otherwise.
    """
    H = len(A)
    W = len(A[0])
    if r_start < 0 or r_start + (N-1) > H - 1:
        return False # out of bounds row
    if c_start < 0 or c_start + (N-1) > W - 1:
        return False # o.o.b. col
    # loop over each location _offset_ i
    for i in range(N):
        if A[r_start+i][c_start+i] != ch: # a mismatch!
            return False
    return True  # all offsets succeeded, so we return True

def clearScreen():
    print("\033[H\033[J") # escape codes instruct the terminal to clear the screen


class Board:
    """A data type representing a Connect-4 board
       with an arbitrary number of rows and columns.
    """

    def __init__(self, width, height):
        """Construct objects of type Board, with the given width and height."""
        self.width = width
        self.height = height
        self.data = [[' ']*width for row in range(height)]

        # We do not need to return anything from a constructor!

    def __repr__(self):
        """This method returns a string representation
           for an object of type Board.
        """
        s = ''                          # the string to return
        for row in range(0, self.height):
            s += '|'
            for col in range(0, self.width):
                s += self.data[row][col] + '|'
            s += '\n'

        s += (2*self.width + 1) * '-'   # bottom of the board

        # and the numbers underneath here

        return s       # the board is complete, return it

    def addMove(self, col, ox):
        """ Modifies this board by placing the given character/piece
            in the given column
        """
        for row in reversed(self.data):
            if row[col] == ' ':
                break
        row[col] = ox

    def clear(self):
        """ Resets all spaces of this board to empty
        """
        for row in reversed(self.data):
            self.data = [[' ']*self.width for row in range(self.height)]

    def setBoard(self, moveString):
        """Accepts a string of columns and places
           alternating checkers in those columns,
           starting with 'X'.

           For example, call b.setBoard('012345')
           to see 'X's and 'O's alternate on the
           bottom row, or b.setBoard('000000') to
           see them alternate in the left column.

           moveString must be a string of one-digit integers.
        """
        nextChecker = 'X'   # start by playing 'X'
        for colChar in moveString:
            col = int(colChar)
            if 0 <= col <= self.width:
                self.addMove(col, nextChecker)
            if nextChecker == 'X':
                nextChecker = 'O'
            else:
                nextChecker = 'X'

    def allowsMove(self, c):
        """Checks if a piece may be added to the given column"""
        return c >= 0 and c < self.width and self.data[0][c] == ' '

    def isFull(self):
        """Checks if there are any empty spaces remaining on the board"""
        for c in range(self.width):
            if self.allowsMove(c):
                return False
        return True

    def delMove(self, col):
        """ Modifies this board by removing the top character/piece
            in the given column
        """
        for row in reversed(self.data):
            if row[col] == ' ':
                break
        for row in self.data:
            if row[col] != ' ':
                break
        row[col] = ' '

    def winsFor(self, ox):
      """Checks if this board is a win for the given character/piece
         ie. checks if there are four in a row of that piece anywhere
         on the board
      """
      for row in range(self.height):
        for col in range(self.width):
          if inarow_Neast(ox, row, col, self.data, 4) or \
                  inarow_Nsouth(ox, row, col, self.data, 4) or \
                  inarow_Nnortheast(ox, row, col, self.data, 4) or \
                  inarow_Nsoutheast(ox, row, col, self.data, 4):
              return True

    def playerTurn(self, ox):
        col = int(input(f"Player '{ox}' what column would you like to play in?"))
        while not self.allowsMove(col):
            clearScreen()
            print(f"Can't play in column {col}. Try again")
            print(self)
            col = int(input(f"Player '{ox}' what column would you like to play in?"))
        self.addMove(col, ox)
        clearScreen()
        print(self)
        return self.winsFor(ox)


    def hostGame(self):
      print("Welcome to Connect4!")
      print(self)
      while True:
          if self.playerTurn('X'):
              print("Player 'X' Wins!")
              break;
          if self.isFull():
              print("The board is full; it's a tie!")
              break;
          if self.playerTurn('O'):
              print("Player 'O' Wins!")
              break;
          if self.isFull():
              print("The board is full; it's a tie!")
              break;



def test():
    #test addMove
    b = Board(7, 6)
    b.addMove(0, 'X')
    b.addMove(0, 'O')
    b.addMove(0, 'X')
    b.addMove(3, 'O')
    b.addMove(4, 'O')
    b.addMove(5, 'O')
    b.addMove(6, 'O')
    print(b)

    #test clear and setBoard
    b.clear()
    print(b)
    b.setBoard('12345')
    print(b)
    b.clear()
    b.setBoard('1122334455')
    print(b)

    #test allowsMove
    b = Board(2, 2)
    b.setBoard('11')
    print(b)
    assert not b.allowsMove(-1)
    assert b.allowsMove(0)
    assert not b.allowsMove(1)
    assert not b.allowsMove(2)

    #test isFull
    b = Board(2, 2)
    assert not b.isFull()
    b.setBoard('0011')
    assert b.isFull()

    #test delMove
    b = Board(2, 2)
    b.setBoard('0011')
    b.delMove(1)
    b.delMove(1)
    b.delMove(1)
    b.delMove(0)
    print(b)

    #test winsFor
    b = Board(7, 6)
    b.setBoard('00102030')
    print(b)
    assert b.winsFor('X')
    assert b.winsFor('O')
    b.clear()
    b.setBoard('23344545515')
    print(b)
    assert b.winsFor('X') #diagonal
    assert not b.winsFor('O')

b = Board(6, 7)
b.hostGame()

