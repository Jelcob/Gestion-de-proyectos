import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.board = [""] * 9
        self.current_player = "X"

        # Crear botones
        self.buttons = []
        for i in range(9):
            row = i // 3
            col = i % 3
            button = tk.Button(self.window, text="", font=("Helvetica", 24), width=4, height=2,
                               command=lambda i=i: self.on_button_click(i))
            button.grid(row=row, column=col)
            self.buttons.append(button)

    def on_button_click(self, index):
        if self.board[index] == "" and not self.check_winner():
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)
            if self.check_winner():
                messagebox.showinfo("Tic Tac Toe", f"Player {self.current_player} wins!")
                self.reset_game()
            elif "" not in self.board:
                messagebox.showinfo("Tic Tac Toe", "It's a tie!")
                self.reset_game()
            else:
                self.switch_player()
                self.make_ai_move()

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def make_ai_move(self):
        if not self.check_winner() and "" in self.board:
            best_score = float("-inf")
            best_move = None

            for i in range(9):
                if self.board[i] == "":
                    self.board[i] = "O"
                    score = self.minimax(self.board, 0, False)
                    self.board[i] = ""

                    if score > best_score:
                        best_score = score
                        best_move = i

            if best_move is not None:
                self.board[best_move] = "O" 
                self.buttons[best_move].config(text="O")
                if self.check_winner():
                    messagebox.showinfo("Tic Tac Toe", "Player O wins!")
                    self.reset_game()
                elif "" not in self.board:
                    messagebox.showinfo("Tic Tac Toe", "It's a tie!")
                    self.reset_game()
                else:
                    self.switch_player()

    def minimax(self, board, depth, is_maximizing):
        scores = {"X": -1, "O": 1, "Tie": 0}

        winner = self.check_winner()
        if winner:
            return scores[winner]

        if is_maximizing:
            best_score = float("-inf")
            for i in range(9):
                if board[i] == "":
                    board[i] = "O"
                    score = self.minimax(board, depth + 1, False)
                    board[i] = ""
                    best_score = max(score, best_score)
            return best_score
        else:
            best_score = float("inf")
            for i in range(9):
                if board[i] == "":
                    board[i] = "X"
                    score = self.minimax(board, depth + 1, True)
                    board[i] = ""
                    best_score = min(score, best_score)
            return best_score

    def check_winner(self):
        # Verificar filas, columnas y diagonales
        for i in range(3):
            if self.board[i] == self.board[i + 3] == self.board[i + 6] != "":
                return self.board[i]

            if self.board[i * 3] == self.board[i * 3 + 1] == self.board[i * 3 + 2] != "":
                return self.board[i * 3]

        if self.board[0] == self.board[4] == self.board[8] != "":
            return self.board[0]

        if self.board[2] == self.board[4] == self.board[6] != "":
            return self.board[2]

        return None

    def reset_game(self):
        for i in range(9):
            self.board[i] = ""
            self.buttons[i].config(text="")
        self.current_player = "X"

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = TicTacToe()
    game.run()
