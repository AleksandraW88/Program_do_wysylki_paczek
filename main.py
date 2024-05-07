# wysłane paczki z produktami od użytkownika
# # waga produktów wczytywana na początku
# # ilość produktów wczytywana na początku
# do każdej paczki mieści się max 20 kg
# powiedz w ilu paczkach wysłane zostaną produkty
# powiedz ile kg wysłano
# powiedz ile wysłano pustych kg
# powiedz, ktora paczka miała najwięcej pustych kg

MAKSYMALNA_LICZBA_KG_W_PACZCE = 20

ilosc_produktow =0
waga_produktu = 0
suma_wag = 0
liczba_produktow_w_paczce = 0
liczba_kg_w_wyslanej_paczce = 0
liczba_paczek_wyslanych = 0
najwieksza_liczba_pustych_kg_w_paczce = 0
numer_paczki_z_najwieksza_iloscia_pustych_kg = None

ilosc_produktow = int(input("Podaj liczbe produktow do wyslania: "))
print("Podaj wage kazdego z produktow w kilogramach. Pamietaj, ze waga musi byc wieksza od 0 kg i nie wieksza niz 10 kg. ")
for idx in range (ilosc_produktow):
   waga_produktu = float(input(f"Waga produktu {idx + 1}: "))
   print(f"Produkt {idx + 1}: {waga_produktu} kg")
   suma_wag += waga_produktu
print(f"\nSuma wag wszystkich produktow do wyslania: {suma_wag} kg")

if (liczba_kg_w_wyslanej_paczce + waga_produktu > MAKSYMALNA_LICZBA_KG_W_PACZCE):
   print(f"Bus odjezdza z {liczba_nart_w_busie} parami nart!")
   print(f"Pozostala liczba miejsc na narty w busie: {MAKSYMALNA_LICZBA_NART_W_BUSIE - liczba_nart_w_busie}")
   liczba_busow_wyslanych += 1
   if liczba_nart_w_busie > najwieksza_liczba_nart_w_busie:
      najwieksza_liczba_nart_w_busie = liczba_nart_w_busie
      numer_najbardziej_obladowanego_busa = liczba_busow_wyslanych
      print(f"Nowa najwieksza liczba nart w busie: {najwieksza_liczba_nart_w_busie}")
   liczba_nart_w_busie = 0

liczba_nart_w_busie += liczba_nart_narciarza