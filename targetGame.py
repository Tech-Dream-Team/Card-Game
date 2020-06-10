#  Target Game
from tkinter import*
import random

# make the window
window = Tk()
window.title('Target Game')


# create the canvas
canvas = Canvas(window, width = 500, height = 500, bg = 'black')
canvas.pack()

# making the welcome screen
title = canvas.create_text(200, 200, text = 'Target Game', \
fill = 'white', font = ('Helvetica',30))
directions = canvas.create_text(300, 300, text = "Hit the targets to get points \
but don't hit the birds", fill = 'white', font = ('Helvetica', 20))

# set up the score display using label widget
score = 0
score_display = Label(window, text = "Score: " + str(score))
score_display.pack()

# set up the level display also using label widget
level = 1
level_display = Label(window, text = 'Level: ' + str(level))
level_display.pack()

# create an image object using the gif file
player_image_file = PhotoImage
