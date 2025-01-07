# Aufgabe 1.1


class Zutat:
    def __init__(self, name, kalorien, zeit):
        self.name = name
        self.kalorien = kalorien
        self.zeit = zeit


# Aufgabe 1.2


class Rezept:
    def __init__(self, name, beschreibung):
        self.name = name
        self.beschreibung = beschreibung
        self.zutatenliste = {}

    def zutat_hinzufügen(self, zutat, menge):
        self.zutatenliste[zutat] = menge

    def kalorien(self):
        kalorien_counter = 0
        for zutat in self.zutatenliste:
            kalorien_counter += zutat.kalorien
        print(f"Die Gesamtkalorien betragen: {kalorien_counter} kcal!")

    def kochzeit(self):
        kochzeit = 0
        for zutat in self.zutatenliste:
            if zutat.zeit > kochzeit:
                kochzeit = zutat.zeit
        print(f"Die Kochzeit beträgt {kochzeit} Minuten!")

    def rezept_anzeigen(self):
        print(f"Rezept: {self.name}")
        print("Zutaten:")
        for zutat, menge in self.zutatenliste.items():
            print(f"- {zutat.name}: {menge}")
        print(f"\nBechreibung des Rezepts: {self.beschreibung}")


# Aufgabe 1.3

milch = Zutat("Milch", 50, 5)
eier = Zutat("Eier", 150, 0)
mehl = Zutat("Mehl", 300, 10)
zucker = Zutat("Zucker", 400, 5)

pfannkuchen = Rezept("Pfannkuchen", "Super Leckere und fluffige Pfannkuchen.")
pfannkuchen.zutat_hinzufügen(milch, "250ml")
pfannkuchen.zutat_hinzufügen(eier, "2 Stück")
pfannkuchen.zutat_hinzufügen(mehl, "150g")
pfannkuchen.zutat_hinzufügen(zucker, "50g")

pfannkuchen.rezept_anzeigen()

pfannkuchen.kalorien()

pfannkuchen.kochzeit()
