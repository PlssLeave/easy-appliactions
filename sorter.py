import os
import shutil
import time
sciezka = os.path.join(os.path.expanduser("~"), "Downloads")


KATEGORIE = {
    "Obrazy": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp", ".ico", ".tiff"],
    "Dokumenty": [".pdf", ".doc", ".docx", ".txt", ".rtf", ".odt", ".xls", ".xlsx", ".csv", ".ppt", ".pptx"],
    "Archiwa": [".zip", ".rar", ".7z", ".tar", ".gz", ".iso"],
    "Wideo": [".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv", ".webm"],
    "Audio": [".mp3", ".wav", ".flac", ".aac", ".ogg", ".m4a"],
    "Programy_i_Kod": [".exe", ".msi", ".bat", ".sh", ".py", ".js", ".html", ".css", ".php", ".sql", ".json"]
}
while True:
    pliki=os.listdir(sciezka)
    for nazwa in pliki:
            pelna_nazwa=os.path.join(sciezka, nazwa)
            if os.path.isfile(pelna_nazwa):
                nazwa_p, roz=os.path.splitext(nazwa)
                roz=roz.lower()
                if nazwa == "desktop.ini" or roz in [".crdownload", ".part", ".tmp"]:
                    continue
                if roz in KATEGORIE["Obrazy"]:
                    folder="Obrazy"
                elif roz in KATEGORIE["Dokumenty"]:
                    folder="Dokumenty"
                elif roz in KATEGORIE["Archiwa"]:
                    folder="Archiwa"
                elif roz in KATEGORIE["Wideo"]:
                    folder="Wideo"
                elif roz in KATEGORIE["Audio"]:
                    folder="Audio"
                elif roz in KATEGORIE["Programy_i_Kod"]:
                    folder="Programy" 
                else:
                    folder="Inne"
                cel=os.path.join(sciezka,folder)
                os.makedirs(cel,exist_ok=True)
                try:
                    shutil.move(pelna_nazwa, cel)
                except PermissionError:
                    print("Pominięto (plik jest otwarty):", nazwa)