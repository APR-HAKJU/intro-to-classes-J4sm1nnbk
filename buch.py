# TODO: 
# Aufgabe 1:
"""Erstelle eine Klasse Buch mit folgenden Attributen:

- titel
- autor
- seiten
- gelesen (Boolean )

Erstelle zwei Bücher: Eines, das du gelesen hast (setze gelesen=True), 
und eines, das du noch nicht gelesen hast.
"""
class Buch:
    def __init__(self, titel, autor, seiten, gelesen):
        self.titel = titel
        self.autor = autor
        self.seiten = seiten
        self.gelesen = gelesen
        print(f"Neues Buch erstellt: '{self.titel}' von {self.autor}, {self.seiten} Seiten.")
buch1 = Buch(titel="1984", autor="George Orwell", seiten=328, gelesen=True)
buch2 = Buch(titel="Der Alchimist", autor="Paulo Coelho", seiten=197, gelesen=False)

print(f"Buch 1: {buch1.titel}, gelesen: {buch1.gelesen}")


buch3 = Buch("Die drei ???", "Robert Arthur", 150, True)

# TODO: Aufgabe 2:
# Gib für jedes Buch eine Nachricht aus, die angibt, ob du das Buch gelesen hast oder nicht.


print(f"Buch 1: {buch1.titel}, gelesen: {buch1.gelesen}")
print(f"Buch 2: {buch2.titel}, gelesen: {buch2.gelesen}")
print(f"Buch 3: {buch3.titel}, gelesen: {buch3.gelesen}")

