# This is made with my uncle 

from tkinter import *
import random

  
def frage_stellen():
    antwort = eingabefeld.get()
    print("You answer is :", antwort)
    # Hier könntest du etwas mit der Antwort machen, z.B. in einer Datei speichern

    # Frage erneut stellen
    eingabefeld.delete(0, END)  # Lösche den alten Text
    eingabefeld.insert(0, "Whats the  product:")

# Erstelle das Fenster
fenster = Tk()
fenster.title("Math trainer")

# Erstelle ein Label und ein Eingabefeld
label = Label(fenster, text=":")
label.pack()
eingabefeld = Entry(fenster)
eingabefeld.pack()

# Erstelle einen Button, um die Frage zu stellen
button = Button(fenster, text="Frage stellen", command=frage_stellen)
button.pack()

# Starte die Ereignisschleife
fenster.mainloop()
