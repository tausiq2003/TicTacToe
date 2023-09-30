import tkinter as tk
from project import *

class TicTacToeGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tic-Tac-Toe")
        self.root.geometry("400x400") 
        self.board_frame = tk.Frame(self.root)
        self.board_frame.pack(expand=True, padx=20, pady=20)

        self.board = Board().board
        self.buttons = []

        for i in range(3):
            row_buttons = []
            for j in range(3):
                button = tk.Button(self.board_frame, text="", font=("Arial", 24), width=3, height=1, command=lambda row=i, col=j: self.on_button_click(row, col))
                row_buttons.append(button)
            self.buttons.append(row_buttons)
        
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].grid(row=i, column=j, padx=10, pady=10)

        self.info_frame = tk.Frame(self.root)
        self.info_frame.pack(pady=(0, 20))

        self.player_attempts_label = tk.Label(self.info_frame, text="", font=("Arial", 12))
        self.player_attempts_label.pack()

        self.player1_label = tk.Label(self.info_frame, text="", font=("Arial", 12))
        self.player1_label.pack()

        self.player2_label = tk.Label(self.info_frame, text="", font=("Arial", 12))
        self.player2_label.pack()

        self.status_label = tk.Label(self.info_frame, text="", font=("Arial", 16))
        self.status_label.pack()

        self.rematch_button = tk.Button(self.root, text="Rematch", font=("Arial", 12), state=tk.DISABLED, command=self.rematch)
        self.rematch_button.pack(pady=(10, 20))

        self.new_game()

    def on_button_click(self, row, col):
        if self.board[row][col] == "":
            self.board[row][col] = self.current_player.symbol
            self.buttons[row][col].config(text=self.current_player.symbol, state=tk.DISABLED)

            if isGameOver(self.board, checkWinner):
                winner = getWinner(self.board, checkWinner, self.player1, self.player2)
                if winner:
                    self.status_label.config(text=f"{winner.name} ({winner.symbol}) wins!")
                else:
                    self.status_label.config(text="It's a draw!")

                self.rematch_button.config(state=tk.NORMAL)
            else:
                self.current_player = self.player2 if self.current_player is self.player1 else self.player1
                self.status_label.config(text=f"It's {self.current_player.name}'s turn.")

    def new_game(self):
        self.player1 = Player(choice(["X", "O"]), "Player 1")
        self.player2 = Player("X" if self.player1.symbol == "O" else "O", "Player 2")

        for i in range(3):
            for j in range(3):
                self.board[i][j] = ""
                self.buttons[i][j].config(text="", state=tk.NORMAL)

        self.current_player = self.player1

        self.player1_label.config(text=f"{self.player1.name} is {self.player1.symbol}")
        self.player2_label.config(text=f"{self.player2.name} is {self.player2.symbol}")

        self.status_label.config(text=f"It's {self.current_player.name}'s turn.")

        self.rematch_button.config(state=tk.DISABLED)

    def rematch(self):
        self.new_game()

    def start(self):
        self.root.mainloop()

if __name__ == "__main__":
    gui = TicTacToeGUI()
    gui.start()
