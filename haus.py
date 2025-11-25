# TODO: Aufgabe 1:
# Ändere den Code unten, so dass die Eigenschaften des Hauses als Attribute im Konstruktor definiert sind.
# Aktuell werden die Eigenschaften als separate Variablen definiert.
# Definiere einen Konstruktor (__init__), um die Attribute zu initialisieren.
class Haus:
    def __init__(self, quadratmeter, schlafzimmer, badezimmer): # wird aufgerufen wenn ein neues Objekt erstellt wird
                        # z.B.: Haus()
        self.quadratmeter = quadratmeter 
        self.schlafzimmer = schlafzimmer
        self.badezimmer = badezimmer
        print("Neues Haus wurde erstellt! ")

haus1 = Haus(quadratmeter=120, schlafzimmer=3, badezimmer=2)

haus2 = Haus(quadratmeter=85, schlafzimmer=4, badezimmer=1)

haus3 = Haus(quadratmeter=200, schlafzimmer=5, badezimmer=3)

print(f"Haus: {haus1.quadratmeter}m², {haus1.schlafzimmer} Schlafzimmer")
print(f"Haus: {haus2.quadratmeter}m², {haus2.schlafzimmer} Schlafzimmer")
print(f"Haus: {haus3.quadratmeter}m², {haus3.schlafzimmer} Schlafzimmer")

haus4 = Haus(quadratmeter=150, schlafzimmer=3, badezimmer=2)
print(f"Haus 4 hat {haus4.quadratmeter}m²")

# TODO: Aufgabe 2: Erstelle drei weitere Objekte der Klasse Haus mit unterschiedlichen Eigenschaften.


# TODO: Aufgabe 3: Gib die Anzahl der Schlafzimmer und Badezimmer für jedes Haus aus.