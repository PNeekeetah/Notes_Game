# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 10:52:40 2021

@author: Nikita
"""

import sounddevice as sd
from math import pi     
import numpy as np
import threading
import tkinter as tk
import random
import time

notes_dictionary = { "A2" : 110.0 ,  "A2#" : 116.54 ,  "B2" : 123.47 ,  "C2" : 130.81 ,  
                "C3#" : 138.59 ,  "D3" : 146.83 ,  "D3#" : 155.56 ,  "E3" : 164.81 ,  
                "F3" : 174.61 ,  "F3#" : 185.0 ,  "G3" : 196.0 ,  "G3#" : 207.65 ,  
                "A3" : 220.0 ,  "A3#" : 233.08 ,  "B3" : 246.94 ,  "C3" : 261.63 ,  
                "C4#" : 277.18 ,  "D4" : 293.66 ,  "D4#" : 311.13 ,  "E4" : 329.63 ,  
                "F4" : 349.23 ,  "F4#" : 369.99 ,  "G4" : 392.0 ,  "G4#" : 415.3 ,  
                "A4" : 440.0 ,  "A4#" : 466.16 ,  "B4" : 493.88 ,  "C4" : 523.25 ,  
                "C5#" : 554.37 ,  "D5" : 587.33 ,  "D5#" : 622.25 ,  "E5" : 659.26 ,  
                "F5" : 698.46 ,  "F5#" : 739.99 ,  "G5" : 783.99 ,  "G5#" : 830.61 }

allowed_intervals = []
string_vars = []
notes = []
interval = 0 
radio_buttons = list()
game_labels = list()
correct_choices = 0
wrong_choices = 0

random.seed(time.time_ns())

sd.sampling_frequency = 8000
samples = np.arange(0,pi, 1/sd.sampling_frequency)

def generate_sound(together : bool):
    global notes
    notes = generate_notes_pair()
    play_sounds(together, notes )

def generate_notes_pair():
    global interval
    if (len(allowed_intervals) > 0):
        root_note = random.choice(list(notes_dictionary.values()))
        interval = allowed_intervals[random.randint(0,len(allowed_intervals)-1)]
        next_note = root_note*2**(interval / 12.0)
        print(root_note, next_note, interval)
        return root_note, next_note
    else:
        return None
    
def play_sound(sound_frequency : float ):
    sound = np.sin(2*pi*samples*sound_frequency)
    sd.play(sound, sd.sampling_frequency )    
    
def play_sounds(together : bool , sounds : list):
   if (together):
       play_2_sounds_together(sounds)
   else:
       play_sequentially(sounds)
        
    
def play_2_sounds_together(sounds : list):
    sound = np.sin(2*pi*samples*sounds[0]) + np.sin(2*pi*samples*sounds[1])
    sd.play(sound, sd.sampling_frequency)
            
        
def play_sequentially (sounds : list):
    if (len(sounds) > 0):
        play_sound(sounds[0])
        time.sleep(2)
        play_sound(sounds[1])
    
    
        
def update_unison():
        if (int_unison.get() == 1):
            allowed_intervals.append(0)
        elif (int_unison.get() == 0):
            allowed_intervals.pop(allowed_intervals.index(0))

def update_minor_second():
        if (int_minor_second.get() == 1):
            allowed_intervals.append(1)
        elif (int_minor_second.get() == 0):
            allowed_intervals.pop(allowed_intervals.index(1))

def update_major_second():
        if (int_major_second.get() == 1):
            allowed_intervals.append(2)
        elif (int_major_second.get() == 0):
            allowed_intervals.pop(allowed_intervals.index(2))

def update_minor_third():
        if (int_minor_third.get() == 1):
            allowed_intervals.append(3)
        elif (int_minor_third.get() == 0):
            allowed_intervals.pop(allowed_intervals.index(3))
        
def update_major_third():
        if (int_major_third.get() == 1):
            allowed_intervals.append(4)
        elif (int_major_third.get() == 0):
            allowed_intervals.pop(allowed_intervals.index(4))
        
def update_perfect_fourth():
        if (int_perfect_fourth.get() == 1):
            allowed_intervals.append(5)
        elif (int_perfect_fourth.get() == 0):
            allowed_intervals.pop(allowed_intervals.index(5))

def update_tritone():
        if (int_tritone.get() == 1):
            allowed_intervals.append(6)
        elif (int_tritone.get() == 0):
            allowed_intervals.pop(allowed_intervals.index(6))
        
def update_perfect_fifth():
        if (int_perfect_fifth.get() == 1):
            allowed_intervals.append(7)
        elif (int_perfect_fifth.get() == 0):
            allowed_intervals.pop(allowed_intervals.index(7))
        
def update_minor_sixth():
        if (int_minor_sixth.get() == 1):
            allowed_intervals.append(8)
        elif (int_minor_sixth.get() == 0):
            allowed_intervals.pop(allowed_intervals.index(8))

def update_major_sixth():
        if (int_major_sixth.get() == 1):
            allowed_intervals.append(9)
        elif (int_minor_sixth.get() == 0):
            allowed_intervals.pop(allowed_intervals.index(9))

def update_minor_seventh():        
        if (int_minor_seventh.get() == 1):
            allowed_intervals.append(10)
        elif (int_minor_seventh.get() == 0):
            allowed_intervals.pop(allowed_intervals.index(10))

def update_major_seventh():
        if (int_major_seventh.get() == 1):
            allowed_intervals.append(11)
        elif (int_major_seventh.get() == 0):
            allowed_intervals.pop(allowed_intervals.index(11))

def update_octave():
        if (int_octave.get() == 1):
            allowed_intervals.append(12)
        elif (int_octave.get() == 0):
            allowed_intervals.pop(allowed_intervals.index(12))
        print(allowed_intervals)
            
def start_game():
    global radio_buttons
    global correct_choices
    global wrong_choices
    global string_vars
    
    if (int_unison.get()):
        radio = tk.Radiobutton(frame, text='Unison', value=0, variable=int_radio)
        radio.pack()
        radio_buttons.append(radio)
    
    if (int_minor_second.get()):
        radio = tk.Radiobutton(frame, text='Minor second', value=1, variable=int_radio)
        radio.pack()
        radio_buttons.append(radio)
        
    if (int_major_second.get()):
        radio = tk.Radiobutton(frame, text='Major second', value=2, variable=int_radio)
        radio.pack()
        radio_buttons.append(radio)
        
    if (int_minor_third.get()):
        radio = tk.Radiobutton(frame, text='Minor third', value=3, variable=int_radio)
        radio.pack()
        radio_buttons.append(radio)
        
    if (int_major_third.get()):
        radio = tk.Radiobutton(frame, text='Major third', value=4, variable=int_radio)
        radio.pack()
        radio_buttons.append(radio)
        
    if (int_perfect_fourth.get()):
        radio = tk.Radiobutton(frame, text='Perfect fourth', value=5, variable=int_radio)
        radio.pack()
        radio_buttons.append(radio)
        
    if (int_tritone.get()):
        radio = tk.Radiobutton(frame, text='Tritone', value=6, variable=int_radio) 
        radio.pack()
        radio_buttons.append(radio)
        
    if (int_perfect_fifth.get()):
        radio = tk.Radiobutton(frame, text='Perfect Fifth', value=7, variable=int_radio)
        radio.pack()
        radio_buttons.append(radio)
        
    if (int_minor_sixth.get()):
        radio = tk.Radiobutton(frame, text='Minor sixth', value=8, variable=int_radio)
        radio.pack()
        radio_buttons.append(radio)
        
    if (int_major_sixth.get()):
        radio = tk.Radiobutton(frame, text='Major sixth', value=9, variable=int_radio)
        radio.pack()
        radio_buttons.append(radio)
        
    if (int_minor_seventh.get()):
        radio = tk.Radiobutton(frame, text='Minor seventh', value=10, variable=int_radio)
        radio.pack()
        radio_buttons.append(radio)
        
    if (int_major_seventh.get()):
        radio = tk.Radiobutton(frame, text='Major seventh', value=11, variable=int_radio)
        radio.pack()
        radio_buttons.append(radio)
        
    if (int_octave.get()):
        radio = tk.Radiobutton(frame, text='Octave', value=12, variable=int_radio)
        radio.pack()
        radio_buttons.append(radio)

    correct_choices = 0
    wrong_choices = 0
    button_start["state"] = "disabled"
    button_end["state"] = "active"
    button_check['state'] = "active"
    
    label_correct = tk.Label(frame, text = "Number of correct choices so far : " )
    label_correct.pack()
    correct = tk.StringVar() 
    correct.set(int(correct_choices))
    label_correct_choices = tk.Label(frame, textvariable = correct)
    label_correct_choices.pack()
    
    game_labels.append(label_correct)
    game_labels.append(label_correct_choices)

    label_wrong = tk.Label(frame, text = "Number of wrong choices so far : " )
    label_wrong.pack()
    wrong = tk.StringVar() 
    wrong.set(int(wrong_choices))
    label_wrong_choices = tk.Label(frame, textvariable = wrong)
    label_wrong_choices.pack()
    
    game_labels.append(label_wrong)
    game_labels.append(label_wrong_choices)
    string_vars.append(correct)
    string_vars.append(wrong)
    
    checkbox_unison ['state'] = "disabled"
    checkbox_minor_second ['state'] = "disabled"
    checkbox_major_second ['state'] = "disabled"
    checkbox_minor_third['state'] = "disabled"
    checkbox_major_third['state'] = "disabled"
    checkbox_perfect_fourth['state'] = "disabled"
    checkbox_tritone['state'] = "disabled"
    checkbox_perfect_fifth['state'] = "disabled"
    checkbox_minor_sixth['state'] = "disabled"
    checkbox_major_sixth['state'] = "disabled"
    checkbox_minor_seventh['state'] = "disabled"
    checkbox_major_seventh['state'] = "disabled"
    checkbox_octave['state'] = "disabled"
    button_generate_note_pair["state"] = "active"

    generate_sound(int_play_together.get())


    root.update()
    
def stop_game():
    global radio_buttons
    global game_labels 
    
    button_start["state"] = "active"
    button_end["state"] = "disabled"
    button_check['state'] = "disabled"

    for radio in radio_buttons:
        radio.destroy()
    
    for label in game_labels:
        label.destroy()
        
    checkbox_unison ['state'] = "active"
    checkbox_minor_second ['state'] = "active"
    checkbox_major_second ['state'] = "active"
    checkbox_minor_third['state'] = "active"
    checkbox_major_third['state'] = "active"
    checkbox_perfect_fourth['state'] = "active"
    checkbox_tritone['state'] = "active"
    checkbox_perfect_fifth['state'] = "active"
    checkbox_minor_sixth['state'] = "active"
    checkbox_major_sixth['state'] = "active"
    checkbox_minor_seventh['state'] = "active"
    checkbox_major_seventh['state'] = "active"
    checkbox_octave['state'] = "active"
    button_generate_note_pair["state"] = "disabled"
    
    string_vars.pop(0)
    string_vars.pop(0)    

    root.update()
    
def check_choice():
    global interval
    global int_radio
    global wrong_choices
    global correct_choices 
    
    if (interval == int_radio.get()):
        print("You're Correct")
        correct_choices += 1
        string_vars[0].set(correct_choices)
        
        
    else:
        print("You're Wrong")
        wrong_choices += 1
        string_vars[1].set(wrong_choices)

    root.update()        
    generate_sound(int_play_together.get())
    
root = tk.Tk()
root.title("Interval Training")
root.geometry("1000x1000")

frame = tk.Frame(root)
frame.pack()

button_generate_note_pair = tk.Button(frame ,text = "Play Notes" , command = lambda:play_sounds(int_play_together.get(),notes))
button_generate_note_pair.pack()
button_generate_note_pair["state"] = "disabled"

int_unison = tk.IntVar()
checkbox_unison = tk.Checkbutton(frame, text = "Unison", variable = int_unison, command = update_unison)
checkbox_unison.pack()

int_minor_second = tk.IntVar()
checkbox_minor_second = tk.Checkbutton(frame, text = "Minor second", variable = int_minor_second, command = update_minor_second)
checkbox_minor_second.pack()

int_major_second = tk.IntVar()
checkbox_major_second = tk.Checkbutton(frame, text = "Major second", variable = int_major_second, command = update_major_second)
checkbox_major_second.pack()

int_minor_third = tk.IntVar()
checkbox_minor_third = tk.Checkbutton(frame, text = "Minor third", variable = int_minor_third, command = update_minor_third)
checkbox_minor_third.pack()

int_major_third = tk.IntVar()
checkbox_major_third = tk.Checkbutton(frame, text = "Major third", variable = int_major_third, command = update_major_third)
checkbox_major_third.pack()

int_perfect_fourth = tk.IntVar()
checkbox_perfect_fourth = tk.Checkbutton(frame, text = "Perfect fourth", variable = int_perfect_fourth, command = update_perfect_fourth)
checkbox_perfect_fourth.pack()

int_tritone = tk.IntVar()
checkbox_tritone = tk.Checkbutton(frame, text = "Tritone", variable = int_tritone, command = update_tritone)
checkbox_tritone.pack()

int_perfect_fifth = tk.IntVar()
checkbox_perfect_fifth = tk.Checkbutton(frame, text = "Perfect fifth", variable = int_perfect_fifth, command = update_perfect_fifth)
checkbox_perfect_fifth.pack()

int_minor_sixth = tk.IntVar()
checkbox_minor_sixth = tk.Checkbutton(frame, text = "Minor sixth", variable = int_minor_sixth, command = update_minor_sixth)
checkbox_minor_sixth.pack()

int_major_sixth = tk.IntVar()
checkbox_major_sixth = tk.Checkbutton(frame, text = "Major sixth", variable = int_major_sixth, command = update_major_sixth)
checkbox_major_sixth.pack()

int_minor_seventh = tk.IntVar()
checkbox_minor_seventh = tk.Checkbutton(frame, text = "Minor seventh", variable = int_minor_seventh, command = update_minor_seventh)
checkbox_minor_seventh.pack()

int_major_seventh = tk.IntVar()
checkbox_major_seventh = tk.Checkbutton(frame, text = "Major seventh", variable = int_major_seventh, command = update_major_seventh)
checkbox_major_seventh.pack()

int_octave = tk.IntVar()
checkbox_octave = tk.Checkbutton(frame, text = "Octave", variable = int_octave, command = update_octave)
checkbox_octave.pack()

int_play_together = tk.IntVar()
checkbox_play_together = tk.Checkbutton(frame, text = "Play together", variable = int_play_together)
checkbox_play_together.pack()

int_radio = tk.IntVar(frame)

button_start = tk.Button(frame, text='Start', command=start_game)
button_start.pack()

button_check = tk.Button(frame, text="Check", command=check_choice)
button_check.pack()
button_check['state'] = "disabled"

button_end = tk.Button(frame, text="End", command=stop_game)
button_end["state"] = "disabled"
button_end.pack()

root.mainloop()



"""
from string import Template

## This small script was used to generate all the notes in the "notes" dictionary
base_frequency = 110.0
half_step = 2**(1/12)
notes = ["A{}","A{}#","B{}","C{}","C{}#","D{}","D{}#", "E{}", "F{}","F{}#", "G{}", "G{}#"]
octave = 2
template = Template(" "$note" : $frequency , ")

dict_entries = ""
for i in range(0, 36):
    dict_entries += template.substitute(note = notes[i%12].format(octave), frequency = round(base_frequency,2))
    base_frequency *= half_step
    if (i % 12 == 3):
        octave += 1
        
print(dict_entries)
"""  

