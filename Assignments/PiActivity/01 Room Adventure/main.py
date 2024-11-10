# Name: Reagan Jose
#Description: Room Adventure with a GUI


from tkinter import Tk
from game import Game

import os
from tkinter import PhotoImage

class Room:
    def __init__(self, name, image_path):
        self.name = name
        self.image = image_path


window = Tk()
window.title("Room Adventure Reloaded")
game = Game(window)
game.play()
window.mainloop()
