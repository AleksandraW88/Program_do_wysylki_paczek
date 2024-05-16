MAKSYMALNA_LICZBA_KG_W_PACZCE = 20
ilosc_produktow = 0
waga_produktu = 0
suma_wag = 0
liczba_paczek_wyslanych = 0
aktualna_waga_paczki = 0
suma_pustych_kg_w_paczkach = 0
najwiecej_pustych_kg = 0
nr_paczki_z_max_pustych_kg = 1
max_puste_kg = 0

ilosc_produktow = int(input("Podaj liczbe produktow do wyslania: "))
print("Podaj wage kazdego z produktow w kilogramach. Waga musi byc wieksza od 0 kg i nie moze byc wieksza niz 10 kg.")
for idx in range (ilosc_produktow):
    waga_produktu = float(input(f"Waga produktu {idx + 1}: "));
    if waga_produktu <= 0 or waga_produktu > 10:
        print("Waga produktu musi byc wieksza od 0 kg, ale nie wieksza niz 10 kg. Program przerwany. Podano bledne dane.")
        break
    suma_wag += waga_produktu
    if aktualna_waga_paczki + waga_produktu > MAKSYMALNA_LICZBA_KG_W_PACZCE:
        liczba_paczek_wyslanych += 1
        puste_kg = MAKSYMALNA_LICZBA_KG_W_PACZCE - aktualna_waga_paczki
        if puste_kg > max_puste_kg:
            max_puste_kg = puste_kg
            nr_paczki_z_max_pustych_kg = liczba_paczek_wyslanych
        aktualna_waga_paczki = waga_produktu
    else:
        aktualna_waga_paczki += waga_produktu
if aktualna_waga_paczki > 0:
    liczba_paczek_wyslanych += 1
    puste_kg = MAKSYMALNA_LICZBA_KG_W_PACZCE-aktualna_waga_paczki
    if puste_kg > max_puste_kg:
        max_puste_kg = puste_kg
        nr_paczki_z_max_pustych_kg = liczba_paczek_wyslanych
if aktualna_waga_paczki > suma_pustych_kg_w_paczkach:
    suma_pustych_kg_w_paczkach = liczba_paczek_wyslanych * MAKSYMALNA_LICZBA_KG_W_PACZCE - suma_wag

print("+"*70)
print("\nPODSUMOWANIE: ")
print(f"\nLiczba wyslanych paczek: {liczba_paczek_wyslanych}")
print(f"Liczba wyslanych kilogramow: {suma_wag}")
print(f"Suma pustych kilogramow: {suma_pustych_kg_w_paczkach}")
print(f"Paczka numer {nr_paczki_z_max_pustych_kg} ma najwiecej pustych kilogramow w ilosci: {max_puste_kg}\n")
print("+"*70)


