import tkinter as tk
from tkinter import ttk
import sys

class Application(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        self.attributes('-alpha', 1)
        self.attributes('-topmost', True)
        self.overrideredirect(True)
        self.resizable(False,False)
        self.title('CPU-RAM usage monitor bar')

        self.set_ui()

    def set_ui(self):
        exitBut = ttk.Button(self, text='Exit', command=self.app_exit)
        exitBut.pack(fill=tk.X)

        self.bar2 = ttk.LabelFrame(self, text='Manual')
        self.bar2.pack(fill=tk.X)

        self.combo_win = ttk.Combobox(self.bar2,
                                      values=["hide","don't hide", 'min'],
                                      width= 10, state='readonly')
        self.combo_win.current(1)
        self.combo_win.pack(side=tk.LEFT)

        ttk.Button(self.bar2, text='move').pack(side=tk.LEFT)
        ttk.Button(self.bar2, text='>>>').pack(side=tk.LEFT)


        self.bar2 = ttk.LabelFrame(self, text='Power')
        self.bar2.pack(fill=tk.BOTH)

        self.bind_class('Tk', '<Enter>', self.enter_mouse)
        self.bind_class('Tk', '<Leave>', self.leave_mouse)

    def enter_mouse(self, event):
        if self.combo_win.current() == 0 or 1:
            self.geometry('')

    def leave_mouse(self, exent):
        if self.combo_win.current() == 0:
            self.geometry(f'{self.winfo_width()}x1')

    def app_exit(self):
        self.destroy()
        sys.exit()
root = Application()
root.mainloop()