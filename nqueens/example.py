from nqueens import HolyQueens
from nqueens import show_board
from nqueens import read_board

# Example of 6 non-interfering queens
bs = [
    "......", 
    "...##.",
    "...##.",
    "......",
    "......"
    ]
hq = HolyQueens(read_board(bs))
show_board(hq.search(6))