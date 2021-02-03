"""
Pracujesz w stacji meteorologicznej i dostałeś właśnie nowe zadanie.
Przed Tobą lista wahań temperatury z ostatniego tygodnia:

1.5, 3, 2, 0, -1 , 1.9, 0.1

Twoim zadaniem jest podanie następujących informacji:
a) najwyższa zanotowana temperatua
b) najniższa zanotowana temperatura
c) średnia temperatura
d) posortowana lista temperatur, od najmniejszej do największej
e) posortowana lista temperatur, od największej do najmniejszej

Napisz program, który zwróci odpowiednie dane.
"""

# Przygotowanie struktury danych - listy, listy temperatur
temperatures = [1.5, 3, 2, 0, -1, 1.9, 0.1]

# a) Najwyższa temeperatura
max_temperature = max(temperatures)
print(f"Najwyższa temperatura: {max_temperature}")

# b) Najniższa temeperatura
min_temperature = min(temperatures)
print(f"Najniższa temperatura: {min_temperature}")

# c) Średnia temperatura
avg_temperature = sum(temperatures) / len(temperatures)
print(f"Średnia temperatura: {avg_temperature}")

# Wynik warto zaokrąglić do 2 miejsc po przecinku
avg_temperature = round(avg_temperature, 2)
print(f"Średnia temperatura: {avg_temperature}")

# d) posortowana lista temperatur, od najmniejszej do największej
temperatures.sort()
print(f"Temperatura od najmniejszej do największej: {temperatures}")

# e) posortowana lista temperatur, od największej do najmniejszej
temperatures.sort(reverse=True)
print(f"Temperatura od największej do najmniejszej: {temperatures}")

# Spróbuj też wykonać to zadanie bez wbudowanych funkcji :)
