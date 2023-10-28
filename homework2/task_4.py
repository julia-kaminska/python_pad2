class Vehicle:
    def __init__(self, predkosc_max, przebieg, nazwa_modelu):
        self.predkosc_max = predkosc_max
        self.przebieg = przebieg
        self.nazwa_modelu = nazwa_modelu

    def liczba_miejsc(self, miejsca):
        return f"{self.nazwa_modelu} pomieści {miejsca} osób."

    def opłata(self, liczba_miejsc=5):
        return liczba_miejsc * 100


class Autobus(Vehicle):
    def liczba_miejsc(self, miejsca=50):
        return super().liczba_miejsc(miejsca)

    def opłata(self, liczba_miejsc=50):
        opłata_początkowa = super().opłata(liczba_miejsc)
        return opłata_początkowa + (0.1 * opłata_początkowa)