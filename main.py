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
najwieksza_liczba_pustych_kg_w_paczce = 0
numer_paczki_z_najwieksza_iloscia_pustych_kg = None

ilosc_produktow = int(input("Podaj liczbe produktow do wyslania: "))
print("Podaj wage kazdego z produktow w kilogramach. Pamietaj, ze waga musi byc wieksza od 0 kg i nie wieksza niz 10 kg. ")
for idx in range (ilosc_produktow):
    waga_produktu = float(input(f"Waga produktu {idx + 1}: "));
    if waga_produktu <= 0 or waga_produktu > 10:
        print("Waga produktu musi byc wieksza od 0 kg, ale nie wieksza niz 10 kg. Program przerwany z powodu podania blednych danych.")
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
print(f"\nLiczba paczek potrzebnych do wysłania: {liczba_paczek_wyslanych}")

