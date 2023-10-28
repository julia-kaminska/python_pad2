from homework2.task_1 import tetranacci
from homework2.task_2 import repeat
from homework2.task_3 import Pojazd
from homework2.task_4 import Autobus, Vehicle
from homework2.task_5 import FunkcjaKwadratowa

# task 1
steps = 10
for i in range(steps + 1):
    result = tetranacci(i)
    print(f"Tetranacci({i}) = {result}")

# task 2
generator_1 = repeat(10,3)
for val in generator_1:
    print(val, end=' ')

generator_2 = repeat(10,5)
print("\n")
for val in generator_2:
    print(val, end=' ')

# The code below works, it is commented out due to its infinite operation
# generator_3 = repeat(5)
# print("\n")
# for val in generator_3:
#     print(val, end=' ')
#
# generator_4 = repeat(5)
# print("\n")
# for val in generator_4:
#     print(val, end=' ')

# task 3
print("\n")
pojazd1 = Pojazd(240, 50)
pojazd2 = Pojazd(180, 17)
print(pojazd1.kolor)
print(pojazd2.kolor)

# task 4
autobus1 = Autobus(300, 20, "Autobus XYZ")
pojazd3 = Vehicle(300, 20, "Pojazd XYZ")
#The default number of seats for a bus is 50, and for a vehicle is 5 when charging a fee.
print(autobus1.opłata())
print(pojazd3.opłata())

# task 5
f1 = FunkcjaKwadratowa(2, 3, 1)
f1.wypisz()
print(f1.oblicz_wartosc(0))
print(f1.oblicz_wartosc(1))

print(FunkcjaKwadratowa(0, 0, 0).rozwiaz())
print(FunkcjaKwadratowa(0, 0, 1).rozwiaz())
print(FunkcjaKwadratowa(0, 2, 3).rozwiaz())
print(FunkcjaKwadratowa(1, 2, 3).rozwiaz())
print(FunkcjaKwadratowa(1, -5, 6).rozwiaz())
print(FunkcjaKwadratowa(1, 4, 4).rozwiaz())
