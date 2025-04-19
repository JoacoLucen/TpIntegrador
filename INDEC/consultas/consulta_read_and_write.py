import csv
from pathlib import Path

file = Path(__file__).resolve().parent.parent / 'utils' / 'IndividuosTotal.csv'
list_dic_dataset = []
anio_trimestre = {}
with open (file, encoding="utf-8") as individuos:
    reader = csv.DictReader(individuos, delimiter=';')
    for row in reader:
        años = row ['ANO4']
        trimestre = row ['TRIMESTRE']
        if años not in anio_trimestre:
            anio_trimestre[años] = set()
        anio_trimestre[años].add(trimestre)
        list_dic_dataset.append(row)
def read_and_write (anio_trimestre,list_dic_dataset):
    anio_trimestre = sorted(anio_trimestre.items(), key=lambda x: int(x[0]))
    # CH06 EDAD
    # CH09 si sabe leer o escribir: 1 es que si, 2 es que no, 3 es menor de 2 anios
    for year, trimestres in anio_trimestre:
        ultimo = max(trimestres, key=int)
        cont_poblacion = 0
        cont_sabe = 0
        cont_nosabe = 0
        for dics in list_dic_dataset:
            if dics['ANO4'] == year and dics['TRIMESTRE'] == ultimo:
                if dics['CH06'] >= '6' and dics['CH09'] == '1':
                    cont_poblacion += 1
                    cont_sabe += 1
                elif dics['CH06'] >= '6' and dics['CH09'] == '2':
                    cont_poblacion += 1
                    cont_nosabe += 1          
        print(f'📚 Las personas capaces de leer en el año {year} del {ultimo} trimestre guardado son del {round((cont_sabe/cont_poblacion)*100)}%')
        print(f'🚫📖 Las personas incapaces de leer en el año {year} del {ultimo} trimestre guardado son del {round((cont_nosabe/cont_poblacion)*100)}%')
        print(f'{'-'*100}')
        
read_and_write(anio_trimestre,list_dic_dataset)