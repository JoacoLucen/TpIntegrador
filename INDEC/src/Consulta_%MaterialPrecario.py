import csv
from pathlib import Path

# Pedir al usuario que seleccione un año, y busque en el último trimestre almacenado
# del mencionado año, el aglomerado con mayor porcentaje de viviendas de “Material
# precario” y el aglomerado con menor porcentaje de viviendas de “Material precario”.



file = Path(__file__).resolve().parent.parent / 'utils' / 'HogaresTotales.csv'
list_dic_dataset = []
anio_trimestre = {}
with open (file, encoding="utf-8") as hogares:
    reader = csv.DictReader(hogares, delimiter=';')
    for row in reader:
        años = row ['ANO4']
        trimestre = row ['TRIMESTRE']
        if años not in anio_trimestre:
            anio_trimestre[años] = set()
        anio_trimestre[años].add(trimestre)
        list_dic_dataset.append(row)
        
        
def precarious_percentage (anio_trimestre,list_dic_dataset):
    

    year = input(f'ingrese un año: ')
    anio_trimestre = dict(sorted(anio_trimestre.items(), key=lambda x: int(x[0])))
    ultimo = max(anio_trimestre[year], key=int)
    i = 0
    aglomeradom = ''
    aglomeradoM = ''
    cont_max = -1
    cont_min = 10000000000
    while  i < len(list_dic_dataset):
        registro = list_dic_dataset[i]
        
        if registro['ANO4'] == year and registro['TRIMESTRE'] == ultimo:
            aglo_actual = registro['AGLOMERADO']
            total = 0
            precarius = 0
            while i < len(list_dic_dataset) and list_dic_dataset[i]['AGLOMERADO'] == aglo_actual and list_dic_dataset[i]['ANO4'] == year and list_dic_dataset[i]['TRIMESTRE'] == ultimo:
                total += 1
                if list_dic_dataset[i]['MATERIAL_TECHUMBRE'] == 'Material precario':
                    precarius += 1
                i += 1
            porcentaje = round((precarius / total) * 100)
            if porcentaje > cont_max:
                cont_max = porcentaje
                aglomeradoM = aglo_actual
            elif porcentaje < cont_min and porcentaje > 0:
                cont_min = porcentaje
                aglomeradom = aglo_actual
        else:
            i += 1

    print(f'📈El codigo de aglomerado con mayor procetaje de viviendas con materiales precario es {aglomeradoM} con un {cont_max}%')
    print(f'📉El codigo de aglomerado con menor procetaje de viviendas con materiales precario es {aglomeradom} con un {cont_min}%')
 
precarious_percentage(anio_trimestre,list_dic_dataset)