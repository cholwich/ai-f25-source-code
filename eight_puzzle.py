from typing import List, Tuple, Any
from state import State

class EightPuzzleState(State):
    def __init__(self, board: List, blank_tile: Tuple[int, int]) -> None:
        self.board = board  # initial state of the board
        self.blank_tile = blank_tile
        self.goal_state = [[1,2,3],[4,5,6],[7,8,0]]

    def is_goal(self) -> bool:
        return self.board == self.goal_state    # check if the current state is the goal state
    
    def __repr__(self) -> str:
        return '\n'.join([' '.join(map(str, row)) for row in self.board]) # string representation of the board
    
    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, EightPuzzleState):   # check if the other object is an instance of EightPuzzleState
            return False
        return self.board == other.board        # check if the board is equal to the other board
    
    def __hash__(self) -> int:
        return hash(tuple(tuple(row) for row in self.board))  # convert the board to a tuple of tuples for hashing
    
    def is_valid(self, row: int, col: int) -> bool:
        return 0 <= row < 3 and 0 <= col < 3    # check if the row and column are within the bounds of the board
    
    def successors(self) -> List[Tuple["EightPuzzleState", int]]:
        successors = []
        row, col = self.blank_tile                          # get the position of the blank tile
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]     # possible moves: up, down, left, right
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc           # calculate the new position of the blank tile
            if self.is_valid(new_row, new_col):             # check if the new position is valid
                new_board = [r[:] for r in self.board]      # create a copy of the board
                new_board[row][col], new_board[new_row][new_col] = new_board[new_row][new_col], new_board[row][col] # swap the blank tile with the adjacent tile
                new_board[new_row][new_col] = 0             # set the new blank tile position to 0
                successors.append((EightPuzzleState(new_board, (new_row, new_col)), 1))
        return successors