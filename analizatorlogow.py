import os
sciezka=os.path.join(os.path.dirname(__file__),"serwer.log")
sciezkazla=os.path.join(os.path.dirname(__file__),"blacklista.txt")
with open(sciezka,"r",encoding="utf-8") as plik:
    nieudana=[]
    statystyki= {}
    for linia in plik.readlines():
        czysta=linia.strip().lower()
        if not czysta:
            continue
        try:
            godzina,ip_syf,akcja=czysta.split(" | ")
        except:
            continue
        ip=ip_syf.replace("ip: ","")
        if akcja=="failed_login":
            nieudana.append([godzina,ip,akcja])
for wiersz in nieudana:
    ip=wiersz[1]
    if ip in statystyki:
        statystyki[ip]+=1
    else: statystyki[ip]=1
liczbadanych=[[ip,ilosc] for ip,ilosc in statystyki.items()]
for ip,ile in liczbadanych:
    if ile>=5:
        print(f"[ALERT] Wykryto atak brute-force z adresu {ip} ({ile} prób)")
        with open(sciezkazla,"a",encoding="utf-8") as plik:
            plik.write(f"{ip},{ile}\n")


    