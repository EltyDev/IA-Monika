from tkinter import Tk

class Window(Tk):

    def __init__(self, width, height, title):
        super().__init__()
        self.title(title)
        print()
        self.geometry(f'{width}x{height}+{int(self.winfo_screenwidth()/2 - width/2)}+{int(self.winfo_screenheight()/2 - width/2)}')
        self.mainloop()

