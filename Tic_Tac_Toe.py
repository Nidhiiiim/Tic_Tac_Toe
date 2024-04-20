import tkinter as tk
from tkinter import messagebox

class TicTacToe(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tic Tac Toe")
        self.game_active = True
        self.player = True  # True for X's turn, False for O's turn
        self.build_grid()
        self.create_widgets()
        self.steps = 1

    def build_grid(self):
        self.buttons = {}
        for i in range(3):
            for j in range(3):
                button = tk.Button(self, text='', font=('normal', 40), width=5, height=2,
                                   command=lambda i=i, j=j: self.on_button_pressed(i, j))
                button.grid(row=i, column=j)
                self.buttons[(i, j)] = button

    def create_widgets(self):
        reset_button = tk.Button(self, text='RESET', command=self.reset_game)
        reset_button.grid(row=3, column=0, columnspan=3, sticky="we")

    def on_button_pressed(self, i, j):
        if self.game_active and self.buttons[(i, j)]['text'] == '':
            self.buttons[(i, j)]['text'] = 'X' if self.player else 'O'
            if self.check_winner():
                self.game_active = False
                winner = 'Player 1 (X)' if self.player else 'Player 2 (O)'
                messagebox.showinfo("Game Over", f"{winner} wins!")
            elif self.check_draw():
                messagebox.showinfo("Game Over", "It's a draw!")
            else:
                self.player = not self.player
                self.steps += 1

    def check_winner(self):
        lines = [
            [(0, 0), (0, 1), (0, 2)],
            [(1, 0), (1, 1), (1, 2)],
            [(2, 0), (2, 1), (2, 2)],
            [(0, 0), (1, 0), (2, 0)],
            [(0, 1), (1, 1), (2, 1)],
            [(0, 2), (1, 2), (2, 2)],
            [(0, 0), (1, 1), (2, 2)],
            [(0, 2), (1, 1), (2, 0)]
        ]
        for line in lines:
            if all(self.buttons[pos]['text'] == ('X' if self.player else 'O') for pos in line):
                return True
        return False

    def check_draw(self):
        return all(self.buttons[pos]['text'] != '' for pos in self.buttons)

    def reset_game(self):
        for pos in self.buttons:
            self.buttons[pos]['text'] = ''
        self.game_active = True
        self.player = True
        self.steps = 1

if __name__ == "__main__":
    game = TicTacToe()
    game.mainloop()
