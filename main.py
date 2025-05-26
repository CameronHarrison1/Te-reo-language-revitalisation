import tkinter as tk

from playsound import playsound



## Note that I haven't put my sound files in yet along with many other things I have talked about in my plan



class app:
    def __init__(self , root):
        self.root = root
        self.stage = 1
        self.entry = None

        self.create_window(self.stage)

    def create_window(self , stage):


        for widget in self.root.winfo_children():
            widget.destroy()

        if stage == 1:

            label = tk.Label(self.root , text = "Te reo learning game" , font = ("Arial" , 25))
            button = tk.Button(self.root , text = "START" , command = self.advance_stage)

            label.pack()
            button.pack(padx = 10 , pady = 10)


        elif stage == 2:

            label = tk.Label(self.root , text = "Test_2")
            button = tk.Button(self.root , text = "Check answer" , command = self.is_correct)
            self.entry = tk.Entry(self.root)
            
            label.pack()
            self.entry.pack(padx = 10 , pady = 10)
            button.pack()

        elif stage == 3:

            label = tk.Label(self.root , text = "Test_3")
            button = tk.Button(self.root , text = "Close" , command = root.destroy)

            label.pack()
            button.pack()
            


        label.pack()
        button.pack()

    def advance_stage(self):

        self.stage += 1
        self.create_window(self.stage)

    def is_correct(self):
        self.correct = self.entry.get()

        if self.correct == "Caleb":
            self.advance_stage()

    def sound_effect(self , file):
        self.file = file
        playsound(file)


root = tk.Tk()

root.geometry("400x300+760+390")

app(root)


root.mainloop()