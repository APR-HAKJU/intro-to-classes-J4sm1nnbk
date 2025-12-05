# Klasse für Laptops mit den Eigenschaften
# - RAM Größe
# - Marke
# - Modell
# - Bildschirmgröße 

notebook_ram_1 = 16
notebook_ram_2 = 32

notebook_marke_1 = "Dell"
notebook_marke_2 = "Apple"

notebook_modell_1 = "XPS 15"
notebook_modell_2 = "MacBook Pro"

notebook_bildschirm_1 = 15.6
notebook_bildschirm_2 = 16.0

class Notebook: #class + name -> legt neuen Bauplan an
    def __init__(self, ram, marke, modell, bildschirm): #Konstruktor - wird automatisch ausgeführt wenn Objekt erstellt wird
        self.ram = ram
        self.marke = marke
        self.modell = modell
        self.bildschirm = bildschirm
        print(f"Neues Notebook erstellt: {self.marke} {self.modell} mit {self.ram}GB RAM und {self.bildschirm}\" Bildschirm.")  
        nb_1 = Notebook(16, "Dell", "XPS 15", 15.6)