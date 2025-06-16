# Cameron Harrison
# Level 2 Computer science Te Reo Revitilisation project

import tkinter as tk
from tkinter import messagebox

import pygame
pygame.mixer.init()

import random



# Dict of sound names + file paths
sounds = {
    "Whaanau": "sounds/Whanau.mp3",
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
    "Ngaahere": "sounds/Ngahere.mp3",
    "Puku": "sounds/Puku.mp3",
    "Raa": "sounds/Ra.mp3",
    "Roto": "sounds/Roto.mp3",
    "Tama": "sounds/Tama.mp3",
    "Tamariki": "sounds/Tamariki.mp3",
    "Teenaa koutou": "sounds/Tena koutou.mp3",
    "Waiata": "sounds/Waiata.mp3",
    "Waka": "sounds/Waka.mp3",
    "Whare": "sounds/Whare.mp3"
}



class app:

    def __init__(self , root):

        # Initialising variables
        self.root = root
        self.stage = 1
        self.entry = None

        self.current_index = 0

        self.incorrect_guesses = 0


        # Puts sounds keys into a list then randomises them
        self.words_to_play = list(sounds.keys())
        random.shuffle(self.words_to_play)

        self.root.title("Te reo language revitilisation spelling game")

        self.create_window(self.stage)

    # Method for stage system
    # This avoids a function for every new window
    def create_window(self , stage):

        # Loops through all widgets in root window then deletes them
        for widget in self.root.winfo_children():
            widget.destroy()

        if stage == 1:

            self.root.config(bg = "dimgray")

            title = tk.Label(self.root ,
                            text = "Te reo spelling game" ,
                            bg = "dimgray" ,
                            font = ("Arial" , 25))
            
            start_button = tk.Button(self.root ,
                                    text = "START" ,
                                    font = ("Arial" , 10) ,
                                    width = 10 ,
                                    height = 3 ,
                                    bg = "#7ddc34" ,
                                    command = lambda: self.create_window(2))
            
            how_2_play = tk.Label(self.root , 
                                  text = "How to play:\n" \
                                  "Click start\n" \
                                  "Listen to the word by clicking the button\n" \
                                  "Type what you think the spelling of the word is into the box" ,
                                  bg = "dimgray" ,
                                  font = ("Arial"))

            title.pack()
            start_button.pack(padx = 10 , pady = 20)
            how_2_play.pack(pady = 10)


        elif stage == 2:

            self.root.config(bg = "dimgray")

            label = tk.Label(
                            self.root ,
                            text = "Spell this word:" ,
                            bg = "dimgray" ,
                            font = ("Arial" , 25))

            # Sets the current word that should play for the window to be the first in the list
            # As the index increases throughout the game it will go through the list
            self.current_word = self.words_to_play[self.current_index]

            # Indexing through the sounds dict by using self.current_word
            # Fetches correct sound file so it matches with what needs to be typed in entry box
            sound = tk.Button(self.root ,
                                text = "Play sound" ,
                                bg = "#4e4e4d" ,
                                fg = "white" ,
                                command=lambda word=self.current_word: self.sound_effect(sounds[word]))
            
            button = tk.Button(self.root ,
                                text = "Check answer" ,
                                bg = "#4e4e4d" ,
                                fg = "white" ,
                                command = self.is_correct)
            
            hint_label = tk.Label(self.root ,
                                  text = "Hint: make sure to use double vowels\n where the vowel is accentuated" ,
                                  bg = "dimgray" ,
                                  font = ("Arial"))
                                
            
            self.entry = tk.Entry(self.root)
            
            label.pack()
            sound.pack(padx = 10 , pady = 10)
            self.entry.pack(padx = 10 , pady = 10)
            button.pack()
            hint_label.pack(padx = 10 , pady = 10)

        elif stage == 3:

            label = tk.Label(self.root ,
                                text = "You finished !" ,
                                bg = "dimgray" ,
                                font = ("Arial" , 25))
            
            guess_label = tk.Label(self.root ,
                                text = f"You got {self.incorrect_guesses} incorrect guesses" ,
                                bg = "dimgray" ,
                                font = ("Arial" , 25))
            
            button = tk.Button(self.root ,
                                text = "Close" ,
                                command = root.destroy)

            label.pack()
            guess_label.pack()
            button.pack()
            


    # Incorrect window popup
    def is_incorrect(self):

        new_window = tk.Toplevel(self.root)

        new_window.geometry("400x300+760+390")
        new_window.config(bg = "red")

        self.incorrect_guesses += 1

        new_label = tk.Label(new_window ,
                                text = "Incorrect ! Try again" ,
                                bg = "red" ,
                                font = ("Arial" , 25))
        
        new_label.pack(pady = 60)
        new_window.after(1500 , new_window.destroy)


    # Correct window popup
    # Also checks if user shoudl move on or is finished
    def is_correct(self):

        self.correct = self.entry.get().strip()

        # Check word typed in is correct
        if self.correct.lower() == self.current_word.lower():

            # Increase this every time user gets answer correct
            # So that it continues to index through the list
            self.current_index += 1

            new_window = tk.Toplevel(self.root)

            new_window.geometry("400x300+760+390")
            new_window.config(bg = "#7ddc34")

            new_label = tk.Label(new_window ,
                                text = "Correct !" ,
                                bg = "#7ddc34" ,
                                font = ("Arial" , 25))
            
            new_label.pack(pady = 60)
            new_window.after(1500 , new_window.destroy)

            # If the length of the current index is less than the total length of the list of words then continue        
            if self.current_index < len(self.words_to_play):
                root.after(1500 , lambda: self.create_window(2))
            else:
                self.create_window(3)

        else:
            self.is_incorrect()


    # Method to play sound
    # If sound files can't be found then shows an error
    def sound_effect(self , file):

        try:
            pygame.mixer.music.load(file)
            pygame.mixer.music.play()
        except pygame.error as e:
            messagebox.showerror("Sound error" , f"Failed to play sound file for {self.current_word}")



root = tk.Tk()

root.geometry("400x300+760+390")

# Make program run
app(root)


root.mainloop()