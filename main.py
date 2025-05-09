import tkinter as tk


class app:
    def __init__(self , root):
        self.root = root
        self.stage = 1

        self.create_window(self.stage)

    def create_window(self , stage):

        for widget in self.root.winfo_children():
            widget.destroy()

        if stage == 1:
            label = tk.Label(self.root , text = "Test")
            button = tk.Button(self.root , text = "Test" , command = self.advance_stage)

        elif stage == 2:
            label = tk.Label(self.root , text = "Test_2")
            button = tk.Button(self.root , text = "Close" , command = root.destroy)


        label.pack()
        button.pack()


    def advance_stage(self):

        self.stage += 1
        self.create_window(self.stage)


root = tk.Tk()

app(root)


root.mainloop()