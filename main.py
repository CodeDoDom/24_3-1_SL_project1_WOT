import logging
logging.basicConfig(
    level=logging.INFO,
    format='%(filename)s(%(lineno)d): %(asctime)s - %(levelname)s - %(message)s'
)

from logging import info as info, debug as debug, warning as warning

from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog

import tkinter as tk

from TicTacToe_3x3 import TicTacToe
from FourMok_6x6 import FourMok

# 티킨터 생성
window = tk.Tk()
window.title('W.O.T\tWorld Of Tic-Tac-Toe')
window.geometry('800x800+0+0')
# window.resizable(False, False)

# 메인 화면에 main_title
main_title = Label(master=window, text='World\nOf\nTic-Tac-Toe', font=('Algerian', 75))
main_title.place(x=30, y=30)


# 메인 화면에 start_bt
# 플레이어1과 플레이어2의 닉네임 입력 받음
def enter_name():
    # 이름 입력창 생성
    name_win = tk.Toplevel(window)
    name_win.title('Enter Player Names')
    name_win.resizable(False, False)
    name_win.grab_set()

    label_player1 = tk.Label(name_win, text="Player 1 Name:", font=('Arial', 12))
    label_player1.grid(row=0, column=0, padx=10, pady=10)
    entry_player1 = tk.Entry(name_win, font=('Arial', 12))
    entry_player1.grid(row=0, column=1, padx=10, pady=10)

    label_player2 = tk.Label(name_win, text="Player 2 Name:", font=('Arial', 12))
    label_player2.grid(row=1, column=0, padx=10, pady=10)
    entry_player2 = tk.Entry(name_win, font=('Arial', 12))
    entry_player2.grid(row=1, column=1, padx=10, pady=10)

    def start_game():    # 게임 시작 버튼 생성
        global player1_name
        player1_name = entry_player1.get()
        global player2_name
        player2_name = entry_player2.get()
        info(f"Player 1: {player1_name}, Player 2: {player2_name}")
        name_win.destroy()  # 이름 입력창 닫기
        # 게임 모드 선택 함수 호출
        select_game_mode()

    start_button = tk.Button(name_win, text="Start Game", font=('Arial', 12), command=start_game)
    start_button.grid(row=2, columnspan=2, padx=10, pady=10)

    def back_main():    # 메인 화면으로 되돌아감
        name_win.destroy()  # 이름 입력창 닫기

    back_button = tk.Button(name_win, text="Back", font=('Arial', 12), command=back_main)
    back_button.grid(row=3, columnspan=2, padx=10, pady=10)

    name_win.protocol("WM_DELETE_WINDOW", lambda: None)     # 이름 입력창 못끔/못내림


enter_name_bt = tk.Button(master=window, text='Game Start', font=('Arial', 15), width=25, height=3,
                          command=enter_name)
enter_name_bt.place(x=450, y=480)


# 메인 화면에 quit_bt
def quit_win():
    window.quit()


enter_name_bt = tk.Button(master=window, text='Quit', font=('Arial', 15), width=25, height=3,
                          command=quit_win)
enter_name_bt.place(x=450, y=600)


def select_game_mode():
    select_mode_win = tk.Toplevel(window)
    select_mode_win.title('Select Game Mode')
    select_mode_win.resizable(False, False)
    select_mode_win.grab_set()

    def play_game_3x3():
        info(f"Play 3x3 tic-tac-toe")
        select_mode_win.destroy()

        game_3x3_win = tk.Toplevel(window)
        game_3x3_win.resizable(False, False)
        game_3x3_win.grab_set()
        game_3x3 = TicTacToe(game_3x3_win, player1_name, player2_name)

        game_3x3_win.protocol("WM_DELETE_WINDOW", lambda: None)

    def play_game_6x6():
        info(f"Play 6x6 FourMok")
        select_mode_win.destroy()

        game_6x6_win = tk.Toplevel(window)
        game_6x6_win.resizable(False, False)
        game_6x6_win.grab_set()
        game_6x6 = FourMok(game_6x6_win, player1_name, player2_name)

        game_6x6_win.protocol("WM_DELETE_WINDOW", lambda: None)

    game_3x3_bt = tk.Button(select_mode_win, text="3X3 Tic-Tac-Toe", font=('Arial', 15), width=25, height=3,
                            command=play_game_3x3)
    game_3x3_bt.grid(row=0, column=0, padx=10, pady=10)

    game_6x6_bt = tk.Button(select_mode_win, text="6x6 FourMok", font=('Arial', 15), width=25, height=3,
                            command=play_game_6x6)
    game_6x6_bt.grid(row=1, column=0, padx=10, pady=10)


window.mainloop()
