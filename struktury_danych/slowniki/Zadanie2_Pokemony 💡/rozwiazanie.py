"""
Czas na powrót do dzieciństwa!
Zbieramy Pokemony! Ale one nie wskoczą tak łatwo do pokeballa.
Wykonaj kilka zadań, a będziesz miał je wszystkie ;).


1. Mając zdefinowaną listę pokemonów, oblicz dla każdego z nich pełną moc - Total i wypisz jej wartość.
Wskazówka: Total jest sumą atrybutów: ['HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed']

2. Stwórz słownik, w którym kluczami będą imiona pokemonów, a wartościami ilość liter przypisanego imienia,
    np. klucz: 'Pikachu' -  wartość: 7. Wypisz zawartość słownika.
"""


pokemon_list = [
  {
    "Name": "Bulbasaur",
    "Type 1": "Grass",
    "Type 2": "Poison",
    "Total": 318,
    "HP": 45,
    "Attack": 49,
    "Defense": 49,
    "Sp. Atk": 65,
    "Sp. Def": 65,
    "Speed": 45,
    "Generation": 1,
    "Legendary": "False"
  },
  {
    "Name": "Ivysaur",
    "Type 1": "Grass",
    "Type 2": "Poison",
    "Total": 405,
    "HP": 60,
    "Attack": 62,
    "Defense": 63,
    "Sp. Atk": 80,
    "Sp. Def": 80,
    "Speed": 60,
    "Generation": 1,
    "Legendary": "False"
  },
  {
    "Name": "Venusaur",
    "Type 1": "Grass",
    "Type 2": "Poison",
    "Total": 525,
    "HP": 80,
    "Attack": 82,
    "Defense": 83,
    "Sp. Atk": 100,
    "Sp. Def": 100,
    "Speed": 80,
    "Generation": 1,
    "Legendary": "False"
  },
  {
    "Name": "Charmander",
    "Type 1": "Fire",
    "Type 2": "",
    "Total": 309,
    "HP": 39,
    "Attack": 52,
    "Defense": 43,
    "Sp. Atk": 60,
    "Sp. Def": 50,
    "Speed": 65,
    "Generation": 1,
    "Legendary": "False"
  },
  {
    "Name": "Charmeleon",
    "Type 1": "Fire",
    "Type 2": "",
    "Total": 405,
    "HP": 58,
    "Attack": 64,
    "Defense": 58,
    "Sp. Atk": 80,
    "Sp. Def": 65,
    "Speed": 80,
    "Generation": 1,
    "Legendary": "False"
  },
  {
    "Name": "Charizard",
    "Type 1": "Fire",
    "Type 2": "Flying",
    "Total": 534,
    "HP": 78,
    "Attack": 84,
    "Defense": 78,
    "Sp. Atk": 109,
    "Sp. Def": 85,
    "Speed": 100,
    "Generation": 1,
    "Legendary": "False"
  }
]



# Zadanie 1: przedstawiam 3 możliwe sposoby (spróbuj znaleźć jeszcze inne ;))
# Sposób 1 - przechodzimy po wszystkich kluczach pokemona i wybieramy tylko te, które są zdefinowane w liście total_keys
total_keys = ['HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed']
for pokemon in pokemon_list:
    total = 0
    for key, value in pokemon.items():
        if key in total_keys:
            total += value
    print(pokemon['Name'], ': ' 'Total:', total)

print('------')
# Sposób 2 - od razu wybieramy tylko te klucze, które nas interesują -> mniej iteracji po słownikach
for pokemon in pokemon_list:
    total = 0
    for key in total_keys:
        total += pokemon[key]
    print(pokemon['Name'], ': ' 'Total:', total)

print('------')

# Sposób 3 - zamiast klasycznego for ...  in ... wykorzystujemy metodę wbudowaną sum() i wyrażenie listowe
for pokemon in pokemon_list:
    total = sum([pokemon[key] for key in total_keys])
    print(pokemon['Name'], ': ' 'Total:', total)


# Zadanie 2
pokemons_names = dict()

for pokemon in pokemon_list:
    name = pokemon['Name']
    pokemons_names[name] = len(name)

print(pokemons_names)
