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

# 티킨터 생성
window = tk.Tk()
window.title('W.O.T\tWorld Of Tic-Tac-Toe')
window.geometry('800x800+0+0')
window.resizable(False, False)

# 메인 화면에 main_title
main_title = Label(master=window, text='World\nOf\nTic-Tac-Toe', font=('Algerian', 75))
main_title.place(x=30, y=30)


# 메인 화면에 start_bt
def start_game():
    pass


start_bt = tk.Button(master=window, text='Game Start', font=('Arial', 15), width=25, height=3,
                     command=start_game)
start_bt.place(x=450, y=550-70)


# 메인 화면에 quit_bt
def quit_win():
    window.quit()


start_bt = tk.Button(master=window, text='Quit', font=('Arial', 15), width=25, height=3,
                     command=quit_win)
start_bt.place(x=450, y=670-70)

window.mainloop()
