from pathlib  import Path
import csv
file = Path('tp')/'data'/'usu_hogar_T216.txt'
#import mi_test
#folder = Path('tp')/'data_zip'
#list_disc_hogar = mi_test.dataset_hogares(folder)
MATERIAL_TECHUMBRE = ''
material_durable = ['1','2','3','4']
material_precario = ['5','6','7']
list_disc_hogar = []
with open (file, encoding="utf-8") as data:
    reader = csv.DictReader(data, delimiter=';')
    for row in reader:
        list_disc_hogar.append(row)

cont_du = 0
cont_pre = 0
cont_no = 0
for i,dict in enumerate(list_disc_hogar):
    valor = dict['V4'].strip()
    if valor in material_durable: # valor de 1 a 4 = Material durable
            list_disc_hogar[i]['MATERIAL_TECHUMBRE'] = 'Material durable'
            cont_du += 1
    elif valor in material_precario: # valor de 5 a 7 = Material precario
        list_disc_hogar[i]['MATERIAL_TECHUMBRE'] = 'Material precario'
        cont_pre += 1
    else:
        list_disc_hogar[i]['MATERIAL_TECHUMBRE'] = 'No aplica'
        cont_no += 1
