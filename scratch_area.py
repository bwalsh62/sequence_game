# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 14:03:13 2020

Sequence board game in Python!

https://en.wikipedia.org/wiki/Sequence_(game)

@author: Ben Walsh
"""

#%% Import libraries

# GUI with tkinter
from tkinter import Tk, Frame, Label, RAISED
# Button, Scale, Frame, Entry, PhotoImage, ttk, OptionMenu, StringVar

#%% Generate deck

cards = ['Ace','2','3','4','5','6','7','8','9','J','Q','K']
cards_hearts = [card+'_Hrt' for card in cards]
cards_spades = [card+'_Spd' for card in cards]
cards_diamonds = [card+'_Dmd' for card in cards]
cards_clubs = [card+'_Clb' for card in cards]
cards_hearts.extend(cards_spades)
cards_hearts.extend(cards_diamonds)
cards_hearts.extend(cards_clubs)
deck = cards_hearts

#%% Layout GUI
root = Tk()
root.title('sequence')
root.geometry('{}x{}'.format(400, 400))

# Grid size
(rows,cols) = (5,5)

# Card size
card_width = 50
card_height = 70

# Create frame containers for each card
#------------
frame_list = [Frame(root, bg='white', width=card_width, height=card_height, pady=2,relief=RAISED) for idx in range(rows*cols)]
lbl_list = [Label(frame_list[idx], text=card, font=("Arial", 12),bg='White') for idx,card in enumerate(deck[:(rows*cols)])]
for row in range(rows):
    for col in range(cols):
        frame_list[row*rows+col].grid(row=row, column=col)
        lbl_list[row*rows+col].grid(row=row, column=col)

root.mainloop()
