from tkinter import *
from tkinter.ttk import *
import tkinter as tk


def ChordIdent():
    window.destroy()
    Notes = (
    ('C', False), 
    ('C#', False), 
    ('D', False), 
    ('D#', False), 
    ('E', False), 
    ('F', False), 
    ('F#', False), 
    ('G', False), 
    ('G#', False), 
    ('A', False), 
    ('A#', False), 
    ('B', False)
)
    ChordIwindow = tk.Tk()
    ChordIwindow.geometry("500x500")

    tk.Label(text="*ALL CHORDS WILL BE MADE WITH SHARPS, THIS IDENTIFIER SHALL NOT RECOGNIZE FLATS*").pack()
    tk.Label(text="select notes,to make a chord").pack()

    CButton = tk.Button(text="C")
    CButton.pack()

    CSharpButton = tk.Button(text="C#")
    CSharpButton.pack()

    DButton = tk.Button(text="D")
    DButton.pack()

    DSharpButton = tk.Button(text="D#")
    DSharpButton.pack()

    EButton = tk.Button(text="E")
    EButton.pack()

    FButton = tk.Button(text="F")
    FButton.pack()

    FSharpButton = tk.Button(text="F#")
    FSharpButton.pack()

    GButton = tk.Button(text="G")
    GButton.pack()

    GSharpButton = tk.Button(text="G#")
    GSharpButton.pack()

    AButton = tk.Button(text="A")
    AButton.pack()

    ASharpButton = tk.Button(text="A#")
    ASharpButton.pack()

    BButton = tk.Button(text="B")
    BButton.pack()

def ChordProg():
    window.destroy()
    ChordProgwindow = tk.Tk()
    ChordProgwindow.geometry("500x500")

window = tk.Tk()
window.geometry("400x250")

tk.Label(text="welcome to theory jack.").pack()
tk.Label(text="to begin using the program, select one of the two below buttons.").pack()
CMakerButton = tk.Button(text="Chord Identifier",command=ChordIdent)
CMakerButton.pack(padx=20, pady=20)
CProgMakeB = tk.Button(text="Chord Progression Prediction",command=ChordProg)
CProgMakeB.pack(padx=20, pady=20)











window.mainloop()