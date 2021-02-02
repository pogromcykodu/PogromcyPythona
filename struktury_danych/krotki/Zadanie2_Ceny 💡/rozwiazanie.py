"""
Właśnie przygotowujesz raport pokazujący zmiany cen napoju Coca Cola po dodaniu nowego podatku cukrowego ;))

Przed: 3.69, 4.5, 3.6, 4.0, 3.99, 3.59
Po:  4.5, 5.5, 4.69, 4.99, 4.00

Twoim zadaniem jest podanie informacji o:
a) najwyższej cenie po nałożeniu podatku
b) najniższa cena biorąc pod uwagę wszystkie ceny (przed i po)
c) średniej cenie przed podwyżką cen
d) średniej cenie po dodaniu nowego podatku
"""

prices_before = (3.69, 4.5, 3.6, 4.0, 3.99, 3.59)
prices_after = (4.5, 5.5, 4.69, 4.99, 4.00)

# a) najwyższa cena po nałożeniu podatku
max_price_after = max(prices_after)
print(f"Najwyższa cena po nałożeniu podatku: {max_price_after}")

# b) najniższa cena biorąc pod uwagę wszystkie ceny (przed i po)
all_prices = prices_before + prices_after
min_price = min(all_prices)
print(f"Najniższa cena: {min_price}")

# c) średnia cena w poprzednim roku
avg_price_before = sum(prices_before) / len(prices_before)
print(f"Srednia cena przed podwyżką cen: {avg_price_before}")

# d) średnia cena po dodaniu nowego podatku
avg_price_after = sum(prices_after) / len(prices_after)
print(f"Srednia cena przed podwyżką cen: {avg_price_after}")
