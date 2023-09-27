import tkinter as tk
from tkinter import messagebox
import random

class TicTacToeApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic-Tac-Toe")

        self.current_player = "X"
        self.board = [[" " for _ in range(3)] for _ in range(3)]

        self.x_wins = 0
        self.o_wins = 0

        self.score_label = tk.Label(self.window, text="Score: X - 0 | O - 0", foreground="red")
        self.score_label.grid(row=3, column=0, columnspan=2)

        self.mode_label = tk.Label(self.window, text="Select Mode:")
        self.mode_label.grid(row=4, column=0, columnspan=2)

        self.bot_button = tk.Button(self.window, text="Play with Bot", command=self.play_with_bot)
        self.bot_button.grid(row=4, column=2)

        self.player2_button = tk.Button(self.window, text="Player vs. Player", command=self.play_with_player2)
        self.player2_button.grid(row=4, column=3)

        self.buttons = [[None for _ in range(3)] for _ in range(3)]

        self.bot_mode = False
        self.bot_player = "O"

    def play_with_bot(self):
        self.bot_mode = True
        self.bot_player = "O"
        self.mode_label.config(text="Mode: Player vs. Bot")
        self.start_game()

    def play_with_player2(self):
        self.bot_mode = False
        self.mode_label.config(text="Mode: Player vs. Player")
        self.start_game()

    def start_game(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(
                    self.window,
                    text=" ",
                    font=("normal", 24),
                    width=6,
                    height=2,
                    command=lambda row=i, col=j: self.make_move(row, col),
                )
                self.buttons[i][j].grid(row=i, column=j)

    def make_move(self, row, col):
        if self.board[row][col] == " ":
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            if self.check_win(row, col):
                self.update_score()
                self.display_winner_message(f"Player {self.current_player} wins! Play again?")
            elif self.check_draw():
                self.display_draw_message("It's a draw! Play again?")
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                if self.bot_mode and self.current_player == self.bot_player:
                    self.bot_move()

    def bot_move(self):
        empty_cells = [(i, j) for i in range(3) for j in range(3) if self.board[i][j] == " "]
        if empty_cells:
            row, col = random.choice(empty_cells)
            self.make_move(row, col)

    def check_win(self, row, col):
        player = self.board[row][col]
        return (
            all(self.board[row][j] == player for j in range(3)) or
            all(self.board[i][col] == player for i in range(3)) or
            all(self.board[i][i] == player for i in range(3)) or
            all(self.board[i][2 - i] == player for i in range(3))
        )

    def check_draw(self):
        return all(self.board[i][j] != " " for i in range(3) for j in range(3))

    def update_score(self):
        if self.current_player == "X":
            self.x_wins += 1
        else:
            self.o_wins += 1
        self.score_label.config(text=f"Score: X - {self.x_wins} | O - {self.o_wins}")

    def restart_game(self):
        for i in range(3):
            for j in range(3):
                self.board[i][j] = " "
                self.buttons[i][j].config(text=" ")
        self.current_player = "X"
        self.mode_label.config(text="Select Mode:")
        self.bot_mode = False

    def display_winner_message(self, message):
        result = messagebox.askyesno("Game Over", message)
        if result:
            self.restart_game()
        else:
            self.window.quit()

    def display_draw_message(self, message):
        result = messagebox.askyesno("Game Over", message)
        if result:
            self.restart_game()
        else:
            self.window.quit()

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = TicTacToeApp()
    app.run()
