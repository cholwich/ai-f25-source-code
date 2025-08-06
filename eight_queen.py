from typing import List, Tuple, Any
from state import State

class EightQueenState(State):
    def __init__(self, queens: List[int]) -> None:
        self.queens = queens            # list of queens on the board

    def is_goal(self) -> bool:
        return len(self.queens) == 8    # check if there are 8 queens on the board
    
    def __repr__(self) -> str:
        board = [['.' for _ in range(8)] for _ in range(8)]     # create an 8x8 board filled with '.'
        for col, row in enumerate(self.queens):
            board[row-1][col] = 'Q'     # place the queens on the board, we neeed to subtract 1 from the row index to match the 0-based index of the list
        return '\n'.join([' '.join(row) for row in board])
    
    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, EightQueenState):
            return False
        return self.queens == other.queens
    
    def __hash__(self) -> int:
        return hash(tuple(self.queens))
    
    def attack(self, row1: int, col1: int, row2: int, col2: int) -> bool:
        return row1 == row2 or col1 == col2 or abs(row1 - row2) == abs(col1 - col2) # check if two queens attack each other
    
    def placable(self, new_row: int, new_col: int) -> bool: # check if a queen can be placed at the given new_row and new_col
        for col in range(len(self.queens)):                 # for each existing queen
            row = self.queens[col]                          # get the row of the existing queen in the column
            if self.attack(new_row, new_col, row, col):     # check if the new queen attacks any existing queen
                return False
        return True
    
    def successors(self) -> List[Tuple["EightQueenState", int]]:
        successors = []
        new_col = len(self.queens)      # the column where the new queen will be placed
        for new_row in range(1, 9):     # for each row in the column
            if self.placable(new_row, new_col):
                new_queens = self.queens[:]     # create a copy of the current queens
                new_queens.append(new_row)      # place the new queen in the new column
                successors.append((EightQueenState(new_queens), 1))
        return successors