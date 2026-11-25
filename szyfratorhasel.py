import os
import time
zapis=os.path.join(os.path.dirname(__file__),"sekret.txt")
while True:
    print("=-=-=-=-=-=-=-=-=-=-=")
    print("Wynierz co chcesz zrobić: ")
    dzialanie=input(f"\n a.Zaszyfruj wiadomość do pliku \n b.Odszyfruj plik \n c.Łamacz PIN-ów \n d.Wyjdź \n").lower()
    if dzialanie=="a":
        tresc=input("Podaj treśc:")
        haslo = input("Podaj hasło do szyfru: ")
        klucz=0
        for litera in haslo:
            klucz+=ord(litera)
        klucz=klucz%10000
        wynik=""
        for znak in tresc:
            wynik+=chr(ord(znak)+klucz)
        with open(zapis, "w", encoding="utf-8") as plik:
            plik.write(wynik)
        print("Zaszyfrowano! Wynik:", wynik)
    if dzialanie=="b":
        with open(zapis,"r",encoding="utf-8") as plik:
            wynik=plik.read()
        haslo=input("Podaj hasło by odszyfrować: ")
        tresc=wynik
        klucz=0
        for litera in haslo:
            klucz +=ord(litera)
        klucz=klucz%10000
        wynik=""
        for znak in tresc:
            wynik+=chr(ord(znak)-klucz)
        print(wynik)
    if dzialanie=="d":
        break
    if dzialanie=="c":
        pin=input("wpisz 7 cyfrowy pin: ")
        dlugosc=len(pin)
        start=time.time()
        for i in range(10**dlugosc):
            proba=str(i).zfill(dlugosc)
            if proba== pin:
                koniec=time.time()
                print(f"Złamano PIN: {proba} w {round(koniec - start, 4)} sekundy!")
                break