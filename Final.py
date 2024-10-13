from tkinter import *
from tkinter.ttk import *
import tkinter as tk

Notes = ('C',"C#","D","D#","E","F","F#","G","G#","A",'A#','B','C',"C#","D","D#","E","F","F#","G","G#","A",'A#','B')
chord = []
m3rd = 3
M3rd = 4
p5 = 7
i = 0

    
def ChordIdent():

    root.destroy()
    ChordIwindow = tk.Tk()
    ChordIwindow.geometry("500x500")
    tk.Label(text="*ALL CHORDS WILL BE MADE WITH SHARPS, THIS IDENTIFIER SHALL NOT RECOGNIZE FLATS*").pack()
    tk.Label(text="select notes,to make a chord (up to 3 notes))").pack()
    tk.Label(text="You have selected the notes : ").pack()
    
    CButton = tk.Button(text="C",command=lambda:showit("C"))
    CButton.pack()

    CSharpButton = tk.Button(text="C#",command=lambda:showit("C#"))
    CSharpButton.pack()

    DButton = tk.Button(text="D",command=lambda:showit("D"))
    DButton.pack()

    DSharpButton = tk.Button(text="D#",command=lambda:showit("D#"))
    DSharpButton.pack()

    EButton = tk.Button(text="E",command=lambda:showit("E"))
    EButton.pack()

    FButton = tk.Button(text="F",command=lambda:showit("F"))
    FButton.pack()

    FSharpButton = tk.Button(text="F#",command=lambda:showit("F#"))
    FSharpButton.pack()

    GButton = tk.Button(text="G",command=lambda:showit("G"))
    GButton.pack()

    GSharpButton = tk.Button(text="G#",command=lambda:showit("G#"))
    GSharpButton.pack()

    AButton = tk.Button(text="A",command=lambda:showit("A"))
    AButton.pack()

    ASharpButton = tk.Button(text="A#",command=lambda:showit("A#"))
    ASharpButton.pack()

    BButton = tk.Button(text="B",command=lambda:showit("B"))
    BButton.pack()

    WCutton = tk.Button(text="What is this chord?",command=lambda:findChor(chord[0],chord))
    WCutton.pack()

    RButton = tk.Button(text="Reset Chord List",command=lambda:restart(chord))
    RButton.pack()

def ChordProg():
    root.destroy()
    ChordProgwindow = tk.Tk()
    ChordProgwindow.geometry("500x500")

def findMinorChord(rooN,chor):
     for i in range(len(Notes)):
          if Notes[i] == rooN:
                    if Notes[i+m3rd] == chor[1]:
                          if Notes[i + p5] == chor[2]:
                            second_window = tk.Toplevel(ChordIdent)
                            second_window.title("Chord")
                            tk.Label(text="That chord is " + rooN + " Major !").pack()

def findMajorChord(rooN,chor):
     for i in range(len(Notes)):
          if Notes[i] == rooN:
                    if Notes[i+M3rd] == chor[1]:
                          if Notes[i + p5] == chor[2]:
                            Chordwindow = tk.Tk()
                            Chordwindow.geometry("300x300")
                            tk.Label(text="That chord is " + rooN + " Major !").pack()


def showit(note):
        chord.append(note)
        
def restart(chor):
        chord.clear()

def findChor(rootN,chor):
        print(rootN,chor)
        findMinorChord(rootN,chor)
        findMajorChord(rootN,chor)



root = tk.Tk()
root.geometry("400x250")

tk.Label(text="welcome to theory jack.").pack()
tk.Label(text="to begin using the program, select one of the two below buttons.").pack()
CMakerButton = tk.Button(text="Chord Identifier",command=ChordIdent)
CMakerButton.pack(padx=20, pady=20)
CProgMakeB = tk.Button(text="Chord Progression Prediction",command=ChordProg)
CProgMakeB.pack(padx=20, pady=20)











root.mainloop()