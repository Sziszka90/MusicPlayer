import tkinter as tkr


music_player = tkr.Tk()
music_player.title("Life is music")
music_player.geometry("450x350")

play_list = tkr.Listbox(music_player, font="Helvetica 12 bold",
                    bg="yellow", selectmode=tkr.SINGLE)

var = tkr.StringVar(music_player)

song_title = tkr.Label(music_player, font="Helvetica 12 bold", textvariable=var)
