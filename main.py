# Cameron Harrison
# Level 2 Computer science Te Reo Revitilisation project

import tkinter as tk

from playsound import playsound



## Note that I haven't put my sound files in yet along with many other things I have talked about in my plan


sounds = {
    "Whanau": r"sounds\Whanau.mp3",
    "Haere Mai": r"sounds\Haere Mai.mp3",
    "Hui": r"sounds\Hui.mp3",
    "Ingoa": r"sounds\Ingoa.mp3",
    "Kai": r"sounds\Kai.mp3",
    "Kaiako": r"sounds\Kaiako.mp3",
    "Kia Ora": r"sounds\Kia Ora.mp3",
    "Kura": r"sounds\Kura.mp3",
    "Marama": r"sounds\Marama.mp3",
    "Maunga": r"sounds\Maunga.mp3",
    "Moana": r"sounds\Moana.mp3",
    "Ngahere": r"sounds\Ngahere.mp3",
    "Puku": r"sounds\Puku.mp3",
    "Ra": r"sounds\Ra.mp3",
    "Roto": r"sounds\Roto.mp3",
    "Tama": r"sounds\Tama.mp3",
    "Tamariki": r"sounds\Tamariki.mp3",
    "Tena koutou": r"sounds\Tena koutou.mp3",
    "Waiata": r"sounds\Waiata.mp3",
    "Waka": r"sounds\Waka.mp3",
    "Whare": r"sounds\Whare.mp3"
}




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

            label = tk.Label(self.root ,
                                text = "Te reo learning game" ,
                                font = ("Arial" , 25))
            
            button = tk.Button(self.root ,
                                    text = "START" ,
                                    font = ("Arial" , 10) ,
                                    width = 10 ,
                                    height = 3 ,
                                    bg = "#7ddc34" ,
                                    command = self.advance_stage)

            label.pack()
            button.pack(padx = 10 , pady = 20)


        elif stage == 2:

            label = tk.Label(self.root ,
                                text = "Spell this word:" ,
                                font = ("Arial" , 25))
            
            sound = tk.Button(self.root ,
                                text = "Play sound" ,
                                command = lambda: self.sound_effect(sounds["Tama"]))
            
            button = tk.Button(self.root ,
                                text = "Check answer" ,
                                command = self.is_correct)
            
            self.entry = tk.Entry(self.root)
            
            label.pack()
            sound.pack(padx = 10 , pady = 10)
            self.entry.pack(padx = 10 , pady = 10)
            button.pack()

        elif stage == 3:

            label = tk.Label(self.root ,
                            text = "Test_3")
            
            button = tk.Button(self.root ,
                                text = "Close" ,
                                command = root.destroy)

            label.pack()
            button.pack()
            



    def advance_stage(self):

        self.stage += 1
        self.create_window(self.stage)


    def is_incorrect(self):

        new_window = tk.Toplevel(self.root)

        new_window.geometry("400x300+760+390")
        new_window.config(bg = "red")

        new_label = tk.Label(new_window ,
                                text = "Incorrect ! Try again" ,
                                bg = "red" ,
                                font = ("Arial" , 25))
        
        new_label.pack(pady = 60)
        new_window.after(3000 , new_window.destroy)


    def is_correct(self):

        self.correct = self.entry.get()

        if self.correct == "Caleb":
            self.advance_stage()

        else:
            self.is_incorrect()


    def sound_effect(self , file):

        self.file = file
        playsound(file)


root = tk.Tk()

root.geometry("400x300+760+390")

app(root)


root.mainloop()