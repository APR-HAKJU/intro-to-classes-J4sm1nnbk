class Bankkonto:
    def __init__(self, inhaber, startguthaben=0):
        self.inhaber = inhaber
        self.guthaben = startguthaben
        self.transaktionen = []
    
    def einzahlen(self, betrag):
        self.guthaben += betrag
        self.transaktionen.append(f"+{betrag}€")
        return f"Neues Guthaben: {self.guthaben}€"
    
    def abheben(self, betrag):
        if self.guthaben >= betrag:
            self.guthaben -= betrag
            self.transaktionen.append(f"-{betrag}€")
            return f"Abgehoben: {betrag}€"
        return "Nicht genug Guthaben!"
    
    def zeige_verlauf(self):
        print(f"Konto von {self.inhaber}:")
        for t in self.transaktionen:
            print(f"  {t}")

