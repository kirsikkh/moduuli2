#Kirjoita ohjelma, joka kysyy suorakulmion kannan ja korkeuden.
# Ohjelma tulostaa suorakulmion piirin ja pinta-alan.
# Suorakulmion piiri tarkoittaa sen neljän sivun yhteispituutta.

kanta = float(input("Anna suorakulmion kanta: "))
korkeus = float(input("Anna suorakulmion korkeus: "))
piiri = 2 * kanta + 2 * korkeus
ala = kanta * korkeus
print(f"Suorakulmion piiri on {piiri} ja pinta-ala on {ala}")

