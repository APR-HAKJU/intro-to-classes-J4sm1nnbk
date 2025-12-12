"""
Übung 4: Klassen importieren & Datentypen verstehen

Aufgabe:
In dieser Übung lernst du:
1. Wie man Klassen aus anderen Dateien importiert
2. Dass Klassen eigene Datentypen sind

Schritte:
1. Importiere die Klasse Song aus dem File 05_song.py
2. Erstelle mehrere Song-Objekte mit Titeln und Interpreten deiner Wahl
3. Verwende type() um zu zeigen, dass jedes Objekt vom Typ 'Song' ist
4. Vergleiche mit anderen Datentypen (String, Integer, Liste)

💡 Tipps:
- from dateiname import Klassenname importiert eine Klasse
- type(variable) gibt den Datentyp zurück
- Jede Klasse ist ein eigener Datentyp!
- Du kannst beliebige Songs, Titel und Interpreten verwenden!

Beispiel Ergebnis:
=== Datentypen Vergleich ===
Text: <class 'str'>
Zahl: <class 'int'>
Liste: <class 'list'>
Song1: <class '__main__.Song'>
Song2: <class '__main__.Song'>

Beide Songs haben denselben Datentyp: True

=== Song Playlist ===
▶️ Song 'Summer Vibes' wird gespielt...
▶️ Song 'Neon Lights' wird gespielt...
▶️ Song 'Ocean Wave' wird gespielt...
"""

# TODO: Importiere die Klasse Song aus 05_song
# from 05_song import Songo
from song import Song #from Filename ohne py" import Klassennamen
song_1 = Song(title="Summer Vibes", interpreten=["DJ Max", "Sarah Sound"])
song_1.zeige_info()

# TODO: Erstelle verschiedene Variablen mit unterschiedlichen Datentypen
# text = "Hallo"
# zahl = 42
# liste = [1, 2, 3]

text= "Hallo"
zahl = 42
liste = [1, 2, 3]

print(type(text))
print(type(zahl))
print(type(liste))
print(type(song_1))

class Laptop:
    pass

laptop_1 = Laptop()
laptop_2 = Laptop()
print(type(laptop_1))
print(f"Datentypen von Laptop 2:  {type(laptop_2)}")

song_2 = Song(title="Neon Lights", interpreten=["Electro Beat", "Night Rider"])
print(type(song_2))

listesong = [song_1, song_2]
print(type(listesong[0].title))
print(type(listesong[1].interpreten))

song_3 = Song(title="Fein", interpreten=["Travis Scott"])
listesong.append(song_3)

song_4 = Song(title="Rock On", interpreten=["The Rockers", "Guitar Hero"])
listesong.append(song_4)

for song in listesong:
    print(song.title)


# TODO: Erstelle 3 Song-Objekte mit Titeln und Interpreten deiner Wahl
song1 = Song("Summer Vibes", ["DJ Max", "Sarah Sound"])
song2 = Song("Neon Lights", ["Electro Beat", "Night Rider"])
song3 = Song("Ocean Wave", ["Sea Breeze", "Wave Rider"])

# TODO: Zeige die Datentypen mit type()
# print("=== Datentypen Vergleich ===")
# print(f"Text: {type(text)}")
# print(f"Zahl: {type(zahl)}")
# print(f"Liste: {type(liste)}")
# print(f"Song1: {type(song1)}")
# print(f"Song2: {type(song2)}")
# print()
print("=== Datentypen Vergleich ===")
print(f"Text {type(text)}")
print(f"Zahl: {type(zahl)}")
print(f"Liste: {type(liste)}")
print(f"Song1: {type(song1)}")
print(f"Song2: {type(song2)}")
print()

# TODO: Vergleiche, ob zwei Songs denselben Datentyp haben
# print(f"Beide Songs haben denselben Datentyp: {type(song1) == type(song2)}")
# print()

print(f"Beide Songs haben denselben Datentyp: {type(song1) == type(song2)}")
print()

# TODO: Spiele alle Songs ab
# print("=== Song Playlist ===")
print("=== Song Playlist ===")
song1.play()
song2.play()
song3.play()