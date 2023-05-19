import os
import shutil

# Adresář na SD kartě, kam chcete kopírovat soubory
destination_directory = "/mnt/sdcard"

# Seznam přípon souborů, které chcete kopírovat
file_extensions = [".jpg", ".png", ".jpeg", ".wav", ".mp3"]

# Rekurzivně prochází všechny soubory a složky v daném adresáři
def process_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Zkontrolujte, zda souborová přípona odpovídá seznamu přípon
            if file.lower().endswith(tuple(file_extensions)):
                # Vytvořte cestu ke zdrojovému a cílovému souboru
                source_path = os.path.join(root, file)
                destination_path = os.path.join(destination_directory, file)
                # Kopírujte soubor na SD kartu
                shutil.copy2(source_path, destination_path)

# Projde všechny jednotky (disky) na počítači
drives = [chr(i) + ":" for i in range(65, 91)]
for drive in drives:
    if os.path.exists(drive):
        process_directory(drive)

print("Kopírování souborů dokončeno.")
