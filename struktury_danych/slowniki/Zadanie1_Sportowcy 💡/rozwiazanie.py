"""
Właśnie zostałeś dziennikarzem sportowym i czeka Cię pierwsze poważne zadanie.
Redaktor naczelny wysłał Ci poniższą listę informacji o kilku znanych sportowcach.

Robert, Lewandowski, piłka nożna, mężczyzna, sport zespołowy, 32
Kamil, Stoch, skoki narciarskie, mężczyzna, sport indywidualny. 33
Iga, Świątek, tenis, kobieta, sport indywidualny, 19
Leo, Messi, piłka nożna, mężczyzna, sport zespołowy, 33
Łukasz, Kubot, tenis, mężczyzna, sport indywidualny, 38


1. Stwórz zmienne typu słownik opisujące każdego ze sportowców.
Skonstruuj je tak, aby zawierały różne typy danych: int, str, bool....
Zwróć też uwagę na to, aby zachować identyczne nazewnictwo kluczy we wszystkich zmiennych.
Przyda Ci się to w kolejnych zadaniach ;)

2. Stwórz listę wszystkich sportowców.
3. Wykorzystując stworzoną przed chwilą listę sportowców, stwórz nową listę, która będzie zawierała tylko piłkarzy.
4. Stwórz funkcję, która policzy ilu sportowców uprawia sporty indywidualne, a ilu zespołowe, Wypisz te wartości.
5. Uups, redaktor podesłał Ci niepełną listę. Zaktulizuj informacje o sportowcach, dopisując nowy klucz: 'kraj'.
    Zastanów się, jak zrobić to skutecznie.
"""

# Zadanie 1
athlete1 = {
    "name": "Robert",
    "surname": "Lewandowski",
    "sport": "piłka nożna",
    "gender": "mężczyzna",
    "team_sport": True,
    "age": 32
}

athlete2 = {
    "name": "Kamil",
    "surname": "Stoch",
    "sport": "skoki narciarskie",
    "gender": "mężczyzna",
    "team_sport": False,
    "age": 33
}

athlete3 = {
    "name": "Iga",
    "surname": "Świątek",
    "sport": "tenis",
    "gender": "kobieta",
    "team_sport": False,
    "age": 19
}

athlete4 = {
    "name": "Leo",
    "surname": "Messi",
    "sport": "piłka nożna",
    "gender": "mężczyzna",
    "team_sport": True,
    "age": 33
}

athlete5 = {
    "name": "Łukasz",
    "surname": "Kubot",
    "sport": "tenis",
    "gender": "mężczyzna",
    "team_sport": False,
    "age": 38
}

# Zadanie 2
athletes = [athlete1, athlete2, athlete3, athlete4, athlete5]
print('Wszyscy sportowcy:\n',athletes)

# Zadanie 3 - sposób 1
footballers = []
for athlete in athletes:
    if athlete['sport'] == 'piłka nożna':
        footballers.append(athlete)

print('\nPiłkarze - rozwiązanie 1:\n', footballers)

# Zadanie 3 - sposób 2
footballers = [athlete for athlete in athletes if athlete['sport'] == 'piłka nożna']
print('\nPiłkarze - rozwiązanie 2:\n', footballers)


# Zadanie 4 - sposób 1
team = individual = 0
for athlete in athletes:
    if athlete['team_sport']:
        team += 1
    else:
        individual += 1

print('\nLiczba sportowców - rozwiązanie 1:')
print('Sporty indywidualne : ', individual)
print('Sporty zespołowe: ', team)

# Zadanie 4 - sposób 2
team = len ([athlete for athlete in athletes if athlete['team_sport']])
individual = len ([athlete for athlete in athletes if not athlete['team_sport']])

print('\nLiczba sportowców - rozwiązanie 2:')
print('Sporty indywidualne : ', individual)
print('Sporty zespołowe: ', team)

#Zadanie 5
for athlete in athletes:
    if athlete['surname'] == 'Messi':
        athlete['country'] = ['Argentyna']  # możesz edytować słownik zarówno wykorzystując nawiasy []...
    else:
        athlete.update({'country': 'Polska'}) # ... jak też metodę update()

print('\nZaktulizowana lista sportowców:\n', athletes)
