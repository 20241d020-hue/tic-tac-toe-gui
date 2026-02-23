import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.root.configure(bg="#1e1e2e")
        self.board = [""] * 9
        self.current_player = "X"
        self.buttons = []
        self._build_header()
        self._build_board()

    def _build_header(self):
        self.status_label = tk.Label(
            self.root, text="Turno: Jugador X",
            font=("Helvetica", 14, "bold"),
            bg="#1e1e2e", fg="#cdd6f4"
        )
        self.status_label.pack(pady=10)

    def _build_board(self):
        frame = tk.Frame(self.root, bg="#1e1e2e")
        frame.pack(padx=20, pady=10)
        for i in range(9):
            btn = tk.Button(
                frame, text="", width=5, height=2,
                font=("Helvetica", 24, "bold"),
                bg="#313244", fg="#cdd6f4",
                activebackground="#45475a",
                relief="flat", bd=2,
                command=lambda i=i: self.make_move(i)
            )
            btn.grid(row=i // 3, column=i % 3, padx=4, pady=4)
            self.buttons.append(btn)

    def make_move(self, index):
        if self.board[index] == "":
            color = "#89b4fa" if self.current_player == "X" else "#f38ba8"
            self.board[index] = self.current_player

            self.buttons[index].config(text=self.current_player, fg=color)

            winner = self.check_winner()
            if winner:
                messagebox.showinfo("¡Fin del juego!", f"¡Jugador {winner} gana!")

                self.status_label.config(text=f"¡{winner} ganó!")
                self.disable_board()
            elif "" not in self.board:
                messagebox.showinfo("¡Fin del juego!", "¡Empate!")
                self.status_label.config(text="¡Empate!")
                self.disable_board()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                self.status_label.config(text=f"Turno: Jugador {self.current_player}")

    def check_winner(self):
        win_combos = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]

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