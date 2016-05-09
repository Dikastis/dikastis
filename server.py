import sys
from server_modules.server_window_handler import MainWindow

try:
    # Python2
    import Tkinter as tk
except ImportError:
    # Python3
    import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    main = MainWindow(root)
    # main.pack(side="top", fill="both", expand=True)
    main.grid(row=0)
    root.mainloop()

 