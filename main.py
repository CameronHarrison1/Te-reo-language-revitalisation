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

            label = tk.Label(self.root , text = "Te reo learning game" , font = ("Arial" , 25))
            button = tk.Button(self.root , text = "START" , command = self.advance_stage)

        elif stage == 2:

            label = tk.Label(self.root , text = "Test_2")
            button = tk.Button(self.root , text = "Close" , command = root.destroy)
            entry = tk.Entry(self.root)

            entry.pack()


        label.pack()
        button.pack(padx = 10 , pady = 10)


    def advance_stage(self):

        self.stage += 1
        self.create_window(self.stage)


root = tk.Tk()

root.geometry("400x300+760+390")

app(root)


root.mainloop()