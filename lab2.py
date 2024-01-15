# Pobranie dwóch liczb od użytkownika
liczba1 = int(input("Podaj pierwszą liczbę całkowitą: "))
liczba2 = int(input("Podaj drugą liczbę całkowitą: "))

# Wypisanie kolejnych liczb od mniejszej do większej
if liczba1 < liczba2:
    for liczba in range(liczba1, liczba2 + 1):
        print(liczba)
else:
    print("Pierwsza liczba powinna być mniejsza od drugiej.")
def funkcja_kwadratowa(x):
    return 2 * x**2 - 5 * x - 8

# Wypisanie wartości funkcji dla x z zakresu [-4, 4] z krokiem 0.5
x = -4.0
while x <= 4.0:
    y = funkcja_kwadratowa(x)
    print(f"Dla x = {x}, y = {y}")
    x += 0.5
# Pętla nieskończona pobierająca liczby od użytkownika
while True:
    liczba = int(input("Podaj liczbę całkowitą: "))
    if liczba < 0:
        break  # Wyjście z pętli w przypadku liczby ujemnej
# Pobranie dwóch liczb od użytkownika
liczba1 = int(input("Podaj pierwszą liczbę całkowitą: "))
liczba2 = int(input("Podaj drugą liczbę całkowitą: "))

# Wypisanie tylko liczb parzystych z zakresu
if liczba1 < liczba2:
    for liczba in range(liczba1, liczba2 + 1):
        if liczba % 2 == 0:
            print(liczba)
else:
    print("Pierwsza liczba powinna być mniejsza od drugiej.")