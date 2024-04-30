import tkinter as tk
from tkinter import messagebox
import math

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Крестики-нолики")
        
        self.board = [" "]*9
        self.current_player = "X"
        
        self.buttons = []
        for i in range(3):
            for j in range(3):
                button = tk.Button(self.window, text=" ", font=('Arial', 20), width=6, height=3,
                                   command=lambda row=i, col=j: self.on_button_click(row, col))
                button.grid(row=i, column=j, sticky="nsew")
                self.buttons.append(button)
        
        self.window.mainloop()
    
    def on_button_click(self, row, col):
        index = row * 3 + col
        if self.board[index] == " ":
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)
            
            if self.check_winner():
                messagebox.showinfo("Победа", f"Игрок {self.current_player} выиграл!")
                self.reset_game()
            elif " " not in self.board:
                messagebox.showinfo("Ничья", "Ничья!")
                self.reset_game()
            else:
                self.switch_player()
                if self.current_player == "O":
                    self.computer_move()
    
    def switch_player(self):
        if self.current_player == "X":
            self.current_player = "O"
        else:
            self.current_player = "X"
    
    def computer_move(self):
        best_score = -math.inf
        best_move = None
        for i in range(9):
            if self.board[i] == " ":
                self.board[i] = "O"
                score = self.minimax(self.board, 0, False)
                self.board[i] = " "
                if score > best_score:
                    best_score = score
                    best_move = i
        self.board[best_move] = "O"
        self.buttons[best_move].config(text="O")
        
        if self.check_winner():
            messagebox.showinfo("Победа", "Игрок O выиграл!")
            self.reset_game()
        elif " " not in self.board:
            messagebox.showinfo("Ничья", "Ничья!")
            self.reset_game()
        else:
            self.switch_player()
    
    def minimax(self, board, depth, is_maximizing):
        if self.check_winner():
            if is_maximizing:
                return -1
            else:
                return 1
        elif " " not in self.board:
            return 0
        
        if is_maximizing:
            best_score = -math.inf
            for i in range(9):
                if self.board[i] == " ":
                    self.board[i] = "O"
                    score = self.minimax(self.board, depth+1, False)
                    self.board[i] = " "
                    best_score = max(score, best_score)
            return best_score
        else:
            best_score = math.inf
            for i in range(9):
                if self.board[i] == " ":
                    self.board[i] = "X"
                    score = self.minimax(self.board, depth+1, True)
                    self.board[i] = " "
                    best_score = min(score, best_score)
            return best_score
    
    def check_winner(self):
        lines = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
        for line in lines:
            if self.board[line[0]] == self.board[line[1]] == self.board[line[2]] != " ":
                return True
        return False
    
    def reset_game(self):
        self.board = [" "]*9
        self.current_player = "X"
        for i in range(9):
            self.buttons[i].config(text=" ")
        if self.current_player == "O":
            self.computer_move()

if __name__ == "__main__":
    game = TicTacToe()
