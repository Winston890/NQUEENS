#Credits to Prof Luca for show board and read board
import numpy as np

QUEEN = 1
EMPTY = 0
FORBIDDEN = 2
WALL = 3

def show_board(board):
    rows, cols = board.shape
    for r in range(rows):
        s = ""
        for c in range(cols):
            if board[r, c] == QUEEN:
                s += "Q"
            elif board[r, c] == FORBIDDEN:
                s += "*"
            elif board[r, c] == WALL:
                s += "#"
            elif board[r, c] == EMPTY:
                s += "."
            else:
                s += "?"
        print(s)

def read_board(string_list):
    rows = len(string_list)
    cols = len(string_list[0])
    board = np.zeros((rows, cols))
    for r, row in enumerate(string_list):
        assert len(row) == cols
        for c, s in enumerate(row):
            if s == "Q":
                board[r, c] = QUEEN
            elif s == "#":
                board[r, c] = WALL
            elif s == "*":
                board[r, c] = FORBIDDEN
    return board

class HolyQueens(object):
    
    def __init__(self, board):
        self.board = board
        self.num_rows, self.num_cols = self.board.shape
        # Current number of queens in the board. 
        self.num_queens = np.sum(self.board == QUEEN)

    def show(self):
        show_board(self.board)

    def propagate(self):
        """Propagates the information on the board, marking with 2 the 
        positions where a queen cannot be."""
        queen_pos = []
        queen_directions = [(1,1), (-1,1), (1,-1), (-1,-1), (0,-1), (0,1), (1,0), (-1,0)]
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                if self.board[row][col] == 1:
                    queen_pos.append((row, col))
        for i in queen_pos:
            for j in queen_directions:
                temp = i                           
                while (0 <= temp[0] + j[0] < self.num_rows) and (0 <= temp[1] + j[1] < self.num_cols) and (self.board[temp[0] + j[0]][temp[1] + j[1]] in [0,2]):
                    self.board[temp[0] + j[0]][temp[1] + j[1]] = 2
                    temp = (temp[0] + j[0]), (temp[1] + j[1])
    
    def search(self, total_num_queens):
        """Searches for a solution, starting from the given board, 
        which contains exactly num_queens.  It returns the board, 
        if such a solution is found, or None, if none could be found
        after exhaustive search."""
        self.propagate()
        original_queens = self.num_queens
        original_board = np.copy(self.board)
        possible_queens = []
        empty = list(np.argwhere(self.board == 0))
        if len(empty) < (total_num_queens - self.num_queens):
            return None
        elif (total_num_queens - self.num_queens) == 0:
            return self.board
        while len(empty) > 0:
            pos = empty.pop()
            self.board[pos[0]][pos[1]] = 1
            self.num_queens += 1
            solution = self.search(total_num_queens)
            if solution is None:
                self.board = np.copy(original_board)
                self.num_queens = original_queens
            if solution is not None:
                return self.board
