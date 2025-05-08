import tkinter as tk

root = tk.Tk()

class app:
    def __init__(self , root):
        self.root = root
        self.stage = 1

        self.create_window(self.stage)

    def create_window(self , stage):

        for widget in self.root.winfo_children():
            widget.destroy()




root.mainloop()