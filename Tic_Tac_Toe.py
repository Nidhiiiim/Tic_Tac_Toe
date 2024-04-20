import tkinter as tk
from tkinter import messagebox

class TicTacToe(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tic Tac Toe with AI")
        self.player = 'X'  # Human is 'X'
        self.ai = 'O'  # AI is 'O'
        self.current_player = self.player  # Human starts
        self.build_grid()
        self.create_widgets()

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
        if self.buttons[(i, j)]['text'] == '' and self.current_player == self.player:
            self.make_move(i, j, self.player)
            if not self.check_end(self.player):
                self.current_player = self.ai
                self.after(500, self.ai_move)

    def ai_move(self):
        best_score = float('-inf')
        best_move = None
        for (i, j), button in self.buttons.items():
            if button['text'] == '':
                button.config(text=self.ai)
                score = self.minimax(0, False)
                button.config(text='')
                if score > best_score:
                    best_score = score
                    best_move = (i, j)
        if best_move:
            self.make_move(best_move[0], best_move[1], self.ai)
            self.check_end(self.ai)

    def minimax(self, depth, is_maximizing):
        if self.check_winner(self.ai):
            return 1
        if self.check_winner(self.player):
            return -1
        if all(self.buttons[(i, j)]['text'] != '' for i in range(3) for j in range(3)):
            return 0

        if is_maximizing:
            best_score = float('-inf')
            for (i, j), button in self.buttons.items():
                if button['text'] == '':
                    button.config(text=self.ai)
                    score = self.minimax(depth + 1, False)
                    button.config(text='')
                    best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for (i, j), button in self.buttons.items():
                if button['text'] == '':
                    button.config(text=self.player)
                    score = self.minimax(depth + 1, True)
                    button.config(text='')
                    best_score = min(score, best_score)
            return best_score

    def make_move(self, i, j, player):
        self.buttons[(i, j)].config(text=player)
        self.current_player = self.ai if player == self.player else self.player

    def check_end(self, player):
        if self.check_winner(player):
            winner = 'AI (O)' if player == self.ai else 'Player (X)'
            messagebox.showinfo("Game Over", f"{winner} wins!")
            return True
        if all(self.buttons[(i, j)]['text'] != '' for i in range(3) for j in range(3)):
            messagebox.showinfo("Game Over", "It's a draw!")
            return True
        return False

    def check_winner(self, player):
        for i in range(3):
            if all(self.buttons[(i, j)]['text'] == player for j in range(3)) or \
               all(self.buttons[(j, i)]['text'] == player for j in range(3)):
                return True
        if all(self.buttons[(i, i)]['text'] == player for i in range(3)) or \
           all(self.buttons[(i, 2-i)]['text'] == player for i in range(3)):
            return True
        return False

    def reset_game(self):
        for i in range(3):
            for j in range(3):
                self.buttons[(i, j)]['text'] = ''
        self.current_player = self.player  # Human starts

if __name__ == "__main__":
    game = TicTacToe()
    game.mainloop()
