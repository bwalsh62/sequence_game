# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 14:03:13 2020

Sequence board game in Python!

https://en.wikipedia.org/wiki/Sequence_(game)

@author: Ben Walsh
"""

#%% Import libraries

# GUI with tkinter
from tkinter import Tk, Frame, Label, RAISED, Button, StringVar, OptionMenu
# , Scale, Frame, Entry, PhotoImage, ttk, 

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
root.geometry('{}x{}'.format(400, 500))

# Grid size
(rows,cols) = (6,7)

# Card size
card_width = 50
card_height = 70

#%% Show Red/Blue turn

# Team Label
team_lbl = Label(root, text="TEAM TURN:", font=("Arial", 14))
team_lbl.grid(column=0, columnspan=3,row=9,sticky='W')

# Define list with music mixing options
teamTurnVar = StringVar(root)

teamOptions = ['Red','Blue']
    
teamTurnVar.set(teamOptions[0]) # set the default option

chooseTeamMenu = OptionMenu(root, teamTurnVar, *teamOptions)
chooseTeamMenu.grid(column=0, row=10)

#%% Callback to place marker from button

def place_marker():
    teamTurn = teamTurnVar.get()
    print(teamTurn)
    
    return True


#%% Create frame containers for each card

frame_list = [Frame(root, bg='white', width=card_width, height=card_height, pady=2,relief=RAISED) for idx in range(rows*cols)]
lbl_list = [Label(frame_list[idx], text=card, font=("Arial", 12),bg='White') for idx,card in enumerate(deck[:(rows*cols)])]
btn_list = [Button(frame_list[idx], text='Place', font=("Arial", 12),bg='White',command=place_marker) for idx in range(rows*cols)]
for row in range(rows):
    for col in range(cols):
        frame_list[row*rows+col].grid(row=row, column=col)
        lbl_list[row*rows+col].grid(row=row, column=col)
        btn_list[row*rows+col].grid(row=row+1, column=col)

root.mainloop()
