import math


class FunkcjaKwadratowa:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def wypisz(self):
        print(f"Funkcja kwadratowa: {self.a}x^2 + {self.b}x + {self.c}")

    def oblicz_wartosc(self, x):
        return self.a * x ** 2 + self.b * x + self.c

    def rozwiaz(self):
        if self.a == 0:
            if self.b == 0:
                if self.c == 0:
                    return "Nieskończona liczba rozwiązań"
                else:
                    return "Brak rozwiązań"
            else:
                x = -self.c / self.b
                return f"Jedno rozwiązanie: x = {x}"
        else:
            delta = self.b ** 2 - 4 * self.a * self.c
            if delta < 0:
                return "Brak rozwiązań"
            elif delta == 0:
                x = -self.b / (2 * self.a)
                return f"Jedno rozwiązanie: x = {x}"
            else:
                x1 = (-self.b - math.sqrt(delta)) / (2 * self.a)
                x2 = (-self.b + math.sqrt(delta)) / (2 * self.a)
                return f"Dwa rozwiązania: x1 = {x1}, x2 = {x2}"
