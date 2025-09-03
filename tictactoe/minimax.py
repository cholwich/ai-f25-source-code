from functools import cached_property

# Abstract base class for a game state
class GameState:
    def __init__(self):
        self.player = "max"
        pass

    def result(self, action):
        return None
    
    @property
    def is_terminal(self):
        return False
    
    @cached_property
    def utility(self):
        return 0

    @cached_property
    def actions(self):
        return []
    
    def __repr__(self):
        return "GameState"
    
    def __hash__(self):
        return hash(repr(self))
    
class TicTacToeGameState(GameState):
    def __init__(self, board=None, player="max"):
        self.player = player
        if board is None:
            self.board = [[' ' for _ in range(3)] for _ in range(3)]
        else:
            self.board = board

    def result(self, action):
        new_board = [row[:] for row in self.board]
        x, y = action
        new_board[x][y] = 'X' if self.player == "max" else 'O'
        new_player = "min" if self.player == "max" else "max"
        return TicTacToeGameState(new_board, new_player)

    @cached_property
    def utility(self):
        # check rows
        for row in self.board:
            if row.count('X') == 3:
                return 1
            if row.count('O') == 3:
                return -1
        # check columns
        for col in range(3):
            if all(self.board[row][col] == 'X' for row in range(3)):
                return 1
            if all(self.board[row][col] == 'O' for row in range(3)):
                return -1
        # check diagonals
        if all(self.board[i][i] == 'X' for i in range(3)):
            return 1
        if all(self.board[i][i] == 'O' for i in range(3)):
            return -1
        if all(self.board[i][2-i] == 'X' for i in range(3)):
            return 1
        if all(self.board[i][2-i] == 'O' for i in range(3)):
            return -1
        # check if all cells are filled, i.e. draw
        if all(cell != ' ' for row in self.board for cell in row):
            return 0
        return -999

    @property
    def is_terminal(self):
        return self.utility in [-1, 0, 1]
    
    @cached_property
    def actions(self):
        # return all empty cell positions
        res = []
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    res.append((i, j))
        return res

    def __repr__(self):
        border = '+---+---+---+'
        return '\n'.join([border] + 
                         ['| ' + ' | '.join(row) + ' |' + 
                          '\n' + border 
                          for row in self.board])

    def __hash__(self):
        return hash(''.join([cell for row in self.board for cell in row]) + 
                    self.player)

def minimax(state):
    if state.is_terminal:
        # return the utility 
        return state.utility, None
    if state.player == "max":
        v = float('-inf')
        best_action = None
        for action in state.actions:
            child = state.result(action)
            child_value, _ = minimax(child)
            if child_value > v:
                v = child_value
                best_action = action
        return v, best_action
    else:
        v = float('inf')
        best_action = None
        for action in state.actions:
            child = state.result(action)
            child_value, _ = minimax(child)
            if child_value < v:
                v = child_value
                best_action = action
        return v, best_action