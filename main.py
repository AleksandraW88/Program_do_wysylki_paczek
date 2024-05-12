# wysłane paczki z produktami od użytkownika
# # waga produktów wczytywana na początku
# # ilość produktów wczytywana na początku
# do każdej paczki mieści się max 20 kg
# powiedz w ilu paczkach wysłane zostaną produkty
# powiedz ile kg wysłano
# powiedz ile wysłano pustych kg
# powiedz, ktora paczka miała najwięcej pustych kg
#print(f"Produkt {idx + 1}: {waga_produktu} kg")


MAKSYMALNA_LICZBA_KG_W_PACZCE = 20
ilosc_produktow =0
waga_produktu = 0
suma_wag = 0
liczba_produktow_w_paczce = 0
liczba_kg_w_wyslanej_paczce = 0
liczba_paczek_wyslanych = 0
aktualna_waga_paczki = 0
waga_wyslanej_paczki = 0
Nowa_Paczka = 0
najciezsza_paczka = 0
suma_pustych_kg_w_paczce = 0
najwiecej_pustych_kg = 0
numer_paczki_z_najwieksza_iloscia_pustych_kg = None
puste_kg = 0

ilosc_produktow = int(input("Podaj liczbe produktow do wyslania: "))
print("Podaj wage kazdego z produktow w kilogramach. Waga musi byc wieksza od 0 kg i nie moze byc wieksza niz 10 kg.")
for idx in range (ilosc_produktow):
    waga_produktu = float(input(f"Waga produktu {idx + 1}: "));
    if waga_produktu <= 0 or waga_produktu > 10:
        print("Waga produktu musi byc wieksza od 0 kg, ale nie wieksza niz 10 kg. Program przerwany. Podano bledne dane.")
        break
    suma_wag += waga_produktu
    print(f"Suma wag wszystkich produktow do wyslania: {suma_wag} kg")
    #nie wiem jak i gdzie dać sume wag produktów by nie powtarzala sie za kazdym razem po podaniu wagi kolejnego produktu
    # i tak by nie zaburzyc ponizszej petli if...
    if aktualna_waga_paczki + waga_produktu > MAKSYMALNA_LICZBA_KG_W_PACZCE:
        liczba_paczek_wyslanych += 1
        aktualna_waga_paczki = waga_produktu
    else:
        aktualna_waga_paczki += waga_produktu
if aktualna_waga_paczki > 0:
    liczba_paczek_wyslanych += 1
if aktualna_waga_paczki > suma_pustych_kg_w_paczce:
    suma_pustych_kg_w_paczce = liczba_paczek_wyslanych * MAKSYMALNA_LICZBA_KG_W_PACZCE - suma_wag
if puste_kg > najwiecej_pustych_kg:
    najwiecej_pustych_kg = puste_kg
    numer_paczki_z_najwieksza_iloscia_pustych_kg = liczba_paczek_wyslanych + 1


print("+"*70)
print("\nPODSUMOWANIE: ")
print(f"\nLiczba wyslanych paczek: {liczba_paczek_wyslanych}")
print(f"Liczba wyslanych kilogramow: {suma_wag}")
print(f"Suma putych kilogramow: {suma_pustych_kg_w_paczce}")
print(f"Paczka numer {numer_paczki_z_najwieksza_iloscia_pustych_kg} ma najwiecej pustych kilogramow w ilosci: {puste_kg}")
print("+"*70)


