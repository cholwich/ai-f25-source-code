# A Tic-Tac-Toe game using Minimax and TkInter
import tkinter as tk
from minimax import TicTacToeGameState, minimax

class TicTacToe(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tic-Tac-Toe")
        self.resizable(False, False)

        self.current_state = TicTacToeGameState(board=None, player="min")

        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        top = tk.Frame(self, padx=10, pady=10)
        top.pack()
        self.status = tk.Label(top, text="Your turn (O)", font=('Helvetica', 14))
        self.status.grid(row=0, column=0, sticky='w')
        tk.Button(top, text="Restart", command=self.restart, width=10).grid(row=0, column=1, padx=(12, 0))

        board_frame = tk.Frame(self, padx=10, pady=10)
        board_frame.pack()
        for r in range(3):
            for c in range(3):
                b = tk.Button(
                    board_frame, text="", width=4, height=2,
                    font=("Helvetica", 28, "bold"),
                    command=lambda r=r, c=c: self.play(r, c)
                )
                b.grid(row=r, column=c, padx=4, pady=4)
                self.buttons[r][c] = b

    def play(self, row, col):
        if (row, col) not in self.current_state.actions or \
            self.current_state.is_terminal or \
            self.current_state.player == 'max':
            return
        self.current_state = self.current_state.result((row, col))
        self.buttons[row][col].config(text="O", state=tk.DISABLED)
        if self.current_state.is_terminal:
            if self.current_state.utility == -1:
                self.status.config(text="You win!")
            elif self.current_state.utility == 0:
                self.status.config(text="It's a draw.")
        else:
            self.status.config(text="AI's turn (X)")
            self.ai_move()

    def ai_move(self):
        _, best_action = minimax(self.current_state)
        self.status.config(text=f"AI chooses ({best_action[0]}, {best_action[1]})")
        self.current_state = self.current_state.result(best_action)
        self.buttons[best_action[0]][best_action[1]].config(text="X", state=tk.DISABLED)
        if self.current_state.is_terminal:
            if self.current_state.utility == 1:
                self.status.config(text="AI wins!")
            elif self.current_state.utility == 0:
                self.status.config(text="It's a draw.")
        else:
            self.status.config(text="Your turn (O)")
            if len(self.current_state.actions) == 1:
                self.play(*self.current_state.actions[0])

    def restart(self):
        self.current_state = TicTacToeGameState(board=None, player="min")
        self.status.config(text="Your turn (O)")
        for r in range(3):
            for c in range(3):
                self.buttons[r][c].config(text="", state=tk.NORMAL)

if __name__ == "__main__":
    app = TicTacToe()
    app.mainloop()
