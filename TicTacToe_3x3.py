import tkinter as tk
# from tkinter import messagebox
import tkinter.messagebox as Messagebox

class TicTacToe:
    def __init__(self, root, p1_name, p2_name):
        self.root = root
        self.root.title("3x3 Tic-Tac-Toe")
        self.current_player = "X"
        self.current_player_name = p1_name
        self.player1_name = p1_name
        self.player2_name = p2_name
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]

        self.create_board()
        self.create_player_turn_label()
        self.create_menu()

    def create_menu(self):
        self.top_menu = tk.Menu()
        self.menu_file = tk.Menu(master=self.top_menu, tearoff=False)
        self.menu_file.add_command(label='Board Reset', command=self.reset_game)     # 보드 초기화
        self.menu_file.add_command(label='Quit Game', command=self.back_main)       # 메인으로 돌아감
        self.top_menu.add_cascade(label='Game Options', menu=self.menu_file)

        self.root.config(menu=self.top_menu)

    def create_board(self):
        for i in range(3):
            for j in range(3):
                button = tk.Button(self.root, text="", font=("Helvetica", 20), width=15, height=6,
                                   command=lambda row=i, col=j: self.on_button_click(row, col))
                button.grid(row=i, column=j)
                self.buttons[i][j] = button

    def create_player_turn_label(self):
        self.player_turn_label = tk.Label(self.root, text=f"Player {self.current_player_name} {self.current_player}'s turn", font=("Helvetica", 16))
        self.player_turn_label.grid(row=3, columnspan=3)

    def on_button_click(self, row, col):
        if self.board[row][col] == "":
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            if self.check_winner():
                self.show_winner_message()
            elif self.check_draw():
                self.show_draw_message()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                self.current_player_name = self.player1_name if self.current_player == "X" else self.player2_name
                self.player_turn_label.config(text=f"Player {self.current_player_name} {self.current_player}'s turn")

    def disable_buttons(self):
        self.top_menu.entryconfig('Game Options', state=tk.DISABLED)
        for row in self.buttons:
            for button in row:
                button.config(state=tk.DISABLED)

    def enable_buttons(self):
        self.top_menu.entryconfig('Game Options', state=tk.NORMAL)
        for row in self.buttons:
            for button in row:
                button.config(state=tk.NORMAL)

    def show_winner_message(self):
        self.disable_buttons()
        Messagebox.showinfo("Winner", f"{self.current_player_name} {self.current_player} wins!")
        self.enable_buttons()
        self.reset_game()

    def show_draw_message(self):
        self.disable_buttons()
        Messagebox.showinfo("Draw", "The game is a draw!")
        self.enable_buttons()
        self.reset_game()

    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != "":
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != "":
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            return True
        return False

    def check_draw(self):
        for row in self.board:
            for cell in row:
                if cell == "":
                    return False
        return True

    def reset_game(self):
        for i in range(3):
            for j in range(3):
                self.board[i][j] = ""
                self.buttons[i][j].config(text="")
        self.current_player = "X"
        self.current_player_name = self.player1_name
        self.player_turn_label.config(text=f"Player {self.current_player_name} {self.current_player}'s turn")

    def back_main(self):
        self.disable_buttons()
        answer = Messagebox.askyesno('Quit Game', 'Do you really want to quit?')
        if answer is True:
            Messagebox.showinfo('Quit Game', 'Quit the game.\nGood Bye!')
            self.root.destroy()
        else:
            self.enable_buttons()
