# Cameron Harrison
# Level 2 Computer science Te Reo Revitilisation project

import tkinter as tk

from playsound import playsound

import random



## Note that I haven't put my sound files in yet along with many other things I have talked about in my plan


sounds = {
    "Whanau": "sounds/Whanau.mp3",
    "Haere Mai": "sounds/Haere Mai.mp3",
    "Hui": "sounds/Hui.mp3",
    "Ingoa": "sounds/Ingoa.mp3",
    "Kai": "sounds/Kai.mp3",
    "Kaiako": "sounds/Kaiako.mp3",
    "Kia Ora": "sounds/Kia Ora.mp3",
    "Kura": "sounds/Kura.mp3",
    "Marama": "sounds/Marama.mp3",
    "Maunga": "sounds/Maunga.mp3",
    "Moana": "sounds/Moana.mp3",
    "Ngahere": "sounds/Ngahere.mp3",
    "Puku": "sounds/Puku.mp3",
    "Ra": "sounds/Ra.mp3",
    "Roto": "sounds/Roto.mp3",
    "Tama": "sounds/Tama.mp3",
    "Tamariki": "sounds/Tamariki.mp3",
    "Tena koutou": "sounds/Tena koutou.mp3",
    "Waiata": "sounds/Waiata.mp3",
    "Waka": "sounds/Waka.mp3",
    "Whare": "sounds/Whare.mp3"
}




class app:

    def __init__(self , root):
        self.root = root
        self.stage = 1
        self.entry = None

        self.current_word = None


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
            
            self.current_word = random.choice(list(sounds.keys()))

            sound = tk.Button(self.root ,
                                text = "Play sound" ,
                                command=lambda word=self.current_word: self.sound_effect(sounds[word])
)
            
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

        self.correct = self.entry.get().strip()

        if self.correct.lower() == self.current_word.lower():
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