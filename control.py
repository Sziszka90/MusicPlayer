import pygame
import tkinter as tkr
import globals

def play():
    pygame.mixer.music.load(globals.play_list.get(tkr.ACTIVE))
    globals.var.set(globals.play_list.get(tkr.ACTIVE))
    pygame.mixer.music.play()

def stop():
    pygame.mixer.music.stop()

def pause():
    pygame.mixer.music.pause()

def unpause():
    pygame.mixer.music.unpause()

def next_selection():
    selection_indices = globals.play_list.curselection()
    
    nextselection = 0

    if len(selection_indices) > 0:
        last_selection = int(selection_indices[-1])
        globals.play_list.selection_clear(selection_indices)

        if last_selection < globals.play_list.size() - 1:
            nextselection = last_selection + 1

    globals.play_list.activate(nextselection)
    globals.play_list.selection_set(nextselection)
    play()

