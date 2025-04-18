import os
import zipfile
from pathlib import Path
import csv
list(Path.cwd().iterdir())

def dataset_individuals(zip_folder):
    all_individuals = []
    for file in os.listdir(zip_folder):
        if file.endswith(".zip"):
            zip_path = zip_folder / file
            with zipfile.ZipFile(zip_path) as all_txt:
                for zips_individuals in all_txt.namelist():
                    if  "usu_individual" in zips_individuals.lower() and zips_individuals.endswith(".txt"):
                        print(f'atroden {zips_individuals}')
                        with all_txt.open(zips_individuals) as txt_individuals:
                            reader = csv.DictReader(txt_individuals.read().decode('utf-8').splitlines(), delimiter=';')
                            all_individuals.extend(reader)
    return all_individuals

def dataset_hogares(zip_folder):
    all_hogares =[]
    for file in os.listdir(zip_folder):
        if file.endswith(".zip"):
            zip_path = zip_folder / file
            with zipfile.ZipFile(zip_path) as all_txt:
                for zips_hogares in all_txt.namelist():
                    if  "usu_hogar" in zips_hogares.lower() and zips_hogares.endswith(".txt"):
                        print(f'atroden {zips_hogares}')
                        with all_txt.open(zips_hogares) as txt_hogares:
                            reader = csv.DictReader(txt_hogares.read().decode('utf-8'), delimiter=';')
                            all_hogares.extend(reader)
    return all_hogares
