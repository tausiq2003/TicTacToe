import tkinter as tk
from tkinter import ttk

def main():
    window = tk.Tk()
    window.title('Tic Tac Toe')
    frame(window)
    window.mainloop()

def frame(window):
    #create a frame
    frm_main = tk.Frame(master=window, width=100, height=50, bg="white")
    frm_main.pack(fill = tk.BOTH)


if __name__ == "__main__":
    main()