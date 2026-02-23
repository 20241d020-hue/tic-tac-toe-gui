import tkinter as tk

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
            self.current_player = "O" if self.current_player == "X" else "X"

if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToe(root)
    root.mainloop()