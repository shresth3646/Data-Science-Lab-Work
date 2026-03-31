import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.root.geometry("400x500")
        self.root.configure(bg="#2B2B2B")
        self.root.resizable(False, False)
        
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        
        # UI Colors
        self.color_x = "#FF5E5E" # Coral Red for X
        self.color_o = "#5BC0BE" # Cyan for O
        self.bg_color = "#3C3F41"
        self.hover_color = "#4C5052"
        
        self.create_ui()

    def create_ui(self):
        # Title Label
        title = tk.Label(self.root, text="TIC-TAC-TOE", font=("Helvetica", 24, "bold"), 
                         bg="#2B2B2B", fg="#FFFFFF", pady=15)
        title.pack()

        # Status Label
        self.status_label = tk.Label(self.root, text=f"Player {self.current_player}'s Turn", 
                                     font=("Helvetica", 14), bg="#2B2B2B", fg=self.color_x)
        self.status_label.pack()

        # Frame for the grid
        self.grid_frame = tk.Frame(self.root, bg="#2B2B2B", pady=20)
        self.grid_frame.pack()

        # 3x3 Buttons
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        for row in range(3):
            for col in range(3):
                btn = tk.Button(self.grid_frame, text="", font=("Helvetica", 28, "bold"),
                                width=4, height=1, bg=self.bg_color, fg="#FFFFFF",
                                activebackground=self.hover_color, relief="flat",
                                command=lambda r=row, c=col: self.on_click(r, c))
                btn.grid(row=row, column=col, padx=5, pady=5)
                self.buttons[row][col] = btn

        # Reset Button
        reset_btn = tk.Button(self.root, text="Restart Game", font=("Helvetica", 12, "bold"),
                              bg="#6C6F71", fg="#FFFFFF", activebackground="#8A8D8F",
                              relief="flat", padx=10, pady=5, command=self.reset_game)
        reset_btn.pack(pady=10)

        # AB Corp Branding
        branding = tk.Label(self.root, text="Made by AB Corp", font=("Helvetica", 9, "italic"), 
                            bg="#2B2B2B", fg="#8A8D8F")
        branding.pack(side="bottom", pady=5)

    def on_click(self, row, col):
        if self.board[row][col] == "" and not self.check_winner():
            self.board[row][col] = self.current_player
            
            # Update Button Text and Color
            btn = self.buttons[row][col]
            btn.config(text=self.current_player)
            if self.current_player == "X":
                btn.config(fg=self.color_x)
            else:
                btn.config(fg=self.color_o)
                
            # Check for win or draw
            if self.check_winner():
                self.status_label.config(text=f"Player {self.current_player} Wins! 🎉", fg="#FFD700")
                messagebox.showinfo("Game Over", f"Player {self.current_player} Wins!")
            elif self.check_draw():
                self.status_label.config(text="It's a Draw! 🤝", fg="#FFFFFF")
                messagebox.showinfo("Game Over", "It's a Draw!")
            else:
                # Switch Player
                self.current_player = "O" if self.current_player == "X" else "X"
                next_color = self.color_x if self.current_player == "X" else self.color_o
                self.status_label.config(text=f"Player {self.current_player}'s Turn", fg=next_color)

    def check_winner(self):
        # Check rows, columns, and diagonals
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != "": return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != "": return True
        
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "": return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "": return True
        return False

    def check_draw(self):
        for row in self.board:
            if "" in row:
                return False
        return True

    def reset_game(self):
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.status_label.config(text=f"Player {self.current_player}'s Turn", fg=self.color_x)
        
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(text="", fg="#FFFFFF")

if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToe(root)
    root.mainloop()