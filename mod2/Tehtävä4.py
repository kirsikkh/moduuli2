#Kirjoita ohjelma, joka kysyy kolme kokonaislukua.
# Ohjelma tulostaa lukujen summan, tulon ja keskiarvon.

luku1 = float(input("Anna kokonaisluku: "))
luku2 = float(input("Anna toinen kokonaisluku: "))
luku3 = float(input("Anna kolmas kokonaisluku: "))
summa = luku1 + luku2 + luku3
tulo = luku1 * luku2 * luku3
keskiarvo = summa / 3
print(f"Kokonaislukujen summa on {summa}, tulo on {tulo} ja keskiarvo {keskiarvo}.")
