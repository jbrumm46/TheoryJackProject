from tkinter import *
import tkinter as tk
from tkinter import messagebox

Notes = ('C', "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", 'A#', 'B')
chord = []
m3rd = 3
M3rd = 4
p5 = 7

def ChordIdent():
    chord_window = tk.Toplevel(root)
    chord_window.geometry("500x500")
    tk.Label(chord_window, text="*ALL CHORDS WILL BE MADE WITH SHARPS, THIS IDENTIFIER SHALL NOT RECOGNIZE FLATS*").pack()
    tk.Label(chord_window, text="Select notes to make a chord (up to 3 notes):").pack()
    tk.Label(chord_window, text="You have selected the notes:").pack()

    for note in Notes:
        tk.Button(chord_window, text=note, command=lambda n=note: showit(n)).pack()

    tk.Button(chord_window, text="What is this chord?", command=lambda: findChor(chord[0], chord)).pack()
    tk.Button(chord_window, text="Reset Chord List", command=restart).pack()

def ChordProg():
    chord_prog_window = tk.Toplevel(root)
    chord_prog_window.geometry("500x500")
    tk.Label(chord_prog_window, text="Chord Progression Prediction").pack()

def showit(note):
    if len(chord) < 3:
        chord.append(note)
        print(f"Selected notes: {chord}")

def restart():
    chord.clear()
    print("Chord list reset.")

def findChor(rootN, chor):
    if len(chor) < 3:
        messagebox.showwarning("Warning", "Select at least 3 notes to identify a chord.")
        return

    if not (findMinorChord(rootN, chor) or findMajorChord(rootN, chor)):
        messagebox.showinfo("Chord Not Found", "No matching chord found. The chord list has been cleared.")
        restart()

def findMinorChord(rooN, chor):
    for i in range(len(Notes)):
        if Notes[i] == rooN:
            if (Notes[(i + m3rd) % len(Notes)] == chor[1] and
                    Notes[(i + p5) % len(Notes)] == chor[2]):
                messagebox.showinfo("Chord", f"That chord is {rooN} Minor!, Chord list cleared.")
                restart()
                return True 
    return False

def findMajorChord(rooN, chor):
    for i in range(len(Notes)):
        if Notes[i] == rooN:
            if (Notes[(i + M3rd) % len(Notes)] == chor[1] and
                    Notes[(i + p5) % len(Notes)] == chor[2]):
                messagebox.showinfo("Chord", f"That chord is {rooN} Major!")
                restart()
                return True 
    return False  

root = tk.Tk()
root.geometry("400x250")

tk.Label(root, text="Welcome to Theory Jack.").pack()
tk.Label(root, text="To begin using the program, select one of the two buttons below.").pack()
tk.Button(root, text="Chord Identifier", command=ChordIdent).pack(padx=20, pady=20)
tk.Button(root, text="Chord Progression Prediction", command=ChordProg).pack(padx=20, pady=20)

root.mainloop()
