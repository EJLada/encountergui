from tkinter import *
from tkinter import ttk

class EncounterBuilder(Frame):

    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.parent.title("5e Encounter Builder")

        message = Label(self, text="Hello, World!")
        message2 = ttk.Label(self, text="Thanks for All The Fish!")
        message.pack()
        message2.pack()


if __name__ == "__main__":
    root = Tk()

    windowWidth = 600
    windowHeight = 400

    screenWidth = root.winfo_screenwidth()
    screenHeight = root.winfo_screenheight()

    centerX = int(screenWidth / 2 - windowWidth / 2)
    centerY = int(screenHeight / 2 - windowHeight / 2)

    root.geometry(f'{windowWidth}x{windowHeight}+{centerX}+{centerY}')

    EncounterBuilder(root).pack(side='top', fill='both', expand=True)
    try:
        from ctypes import windll
        windll.shcore.SetProcessDpiAwareness(1)
    finally:
        root.mainloop()