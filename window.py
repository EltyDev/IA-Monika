from tkinter import Tk, PhotoImage

class Window(Tk):

    def __init__(self, width, height, title):
        super().__init__()
        self.title(title)
        self.geometry(f'{width}x{height}+{int(self.winfo_screenwidth()/2 - width/2)}+{int(self.winfo_screenheight()/2 - width/2)}')
        self.attributes('-fullscreen', True)
        self.iconphoto(False, PhotoImage("data/icon.png"))
        self.mainloop()

