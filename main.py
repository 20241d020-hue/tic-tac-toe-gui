import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.board = [""] * 9
        self.current_player = "X"
        self.buttons = []
        self._build_board()

    def _build_board(self):
        frame = tk.Frame(self.root)
        frame.pack()
        for i in range(9):
            btn = tk.Button(frame, text="", width=6, height=3,
                            command=lambda i=i: self.make_move(i))
            btn.grid(row=i // 3, column=i % 3)
            self.buttons.append(btn)

    def make_move(self, index):
        if self.board[index] == "":
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)

            winner = self.check_winner()
            if winner:
                messagebox.showinfo("¡Fin del juego!", f"¡Jugador {winner} gana!")
                self.disable_board()
            elif "" not in self.board:
                messagebox.showinfo("¡Fin del juego!", "¡Empate!")
                self.disable_board()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        # Combinaciones ganadoras: filas, columnas y diagonales
        win_combos = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # filas
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columnas
            [0, 4, 8], [2, 4, 6]               # diagonales
        ]
        for combo in win_combos:
            a, b, c = combo
            if self.board[a] == self.board[b] == self.board[c] != "":
                return self.board[a]
        return None

    def disable_board(self):
        for btn in self.buttons:
            btn.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToe(root)
    root.mainloop()