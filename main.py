import pygame
import tkinter as tkr
from tkinter.filedialog import askdirectory
import os
import control
import globals


directory = askdirectory()

os.chdir(directory)
song_list = os.listdir()


for item in song_list:
    pos = 0
    globals.play_list.insert(pos, item)
    pos += 1

pygame.init()
pygame.mixer.init()

Button1 = tkr.Button(globals.music_player, width=5, height=3, font="Helvetica 12 bold", text="PLAY",
                     command=control.play, bg="blue", fg="white")
Button2 = tkr.Button(globals.music_player, width=5, height=3, font="Helvetica 12 bold", text="STOP",
                     command=control.stop, bg="red", fg="white")
Button3 = tkr.Button(globals.music_player, width=5, height=3, font="Helvetica 12 bold", text="PAUSE",
                     command=control.pause, bg="purple", fg="white")
Button4 = tkr.Button(globals.music_player, width=5, height=3, font="Helvetica 12 bold", text="UNPAUSE",
                     command=control.unpause, bg="orange", fg="white")
Button5 = tkr.Button(globals.music_player, width=5, height=3, font="Helvetica 12 bold", text="NEXT",
                     command=control.next_selection, bg="pink", fg="white")

globals.song_title.pack()
Button1.pack(fill="x")
Button2.pack(fill="x")
Button3.pack(fill="x")
Button4.pack(fill="x")
Button5.pack(fill="x")
globals.play_list.pack(fill="both", expand="yes")

globals.music_player.mainloop()

