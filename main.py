# wysłane paczki z produktami od użytkownika
# waga produktów wczytywana na początku
# ilość produktów wczytywana na początku
# do każdej paczki mieści się max 20 kg
# powiedz w ilu paczkach wysłane zostaną produkty
# powiedz ile kg wysłano
# powiedz ile wysłano pustych kg
# powiedz, ktora paczka miała najwięcej pustych kg

MAKSYMALNA_LICZBA_KG_W_PACZCE = 20

ilosc_produktow =0
waga_produktu = 0
liczba_produktow_w_paczce = 0
liczba_kg_w_wyslanej_paczce = 0
liczba_paczek_wyslanych = 0
najwieksza_liczba_pustych_kg_w_paczce = 0
numer_paczki_z_najwieksza_iloscia_pustych_kg = None

print("Podaj liczbe produktow do wyslania: ")
ilosc_produktow =input()
print("Podaj wage kazdego z produktow: ")
waga_produktu = input()
for idx in range (int(ilosc_produktow)):
    print(f"Waga produktu  ")
