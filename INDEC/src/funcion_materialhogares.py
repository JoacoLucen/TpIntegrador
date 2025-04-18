# from pathlib  import Path
# import csv
# file = Path('tp')/'data'/'usu_hogar_T216.txt'
# #import mi_test
# #folder = Path('tp')/'data_zip'
# #list_disc_hogar = mi_test.dataset_hogares(folder)
# MATERIAL_TECHUMBRE = ''
# material_durable = ['1','2','3','4']
# material_precario = ['5','6','7']
# # list_disc_hogar = []
# with open (file, encoding="utf-8") as data:
#     reader = csv.DictReader(data, delimiter=';')
#     for row in reader:
#         list_disc_hogar.append(row)
        
def   MATERIAL_TECHUMBRE (list_disc_hogar):
    """Traducir los valores de V4 de integer a strings
        valor de 1 a 4 = Material durable
        valor de 5 a 7 = Material precario
        valor 9 = no aplica

    Args:
        list_disc_hogar (list_dics): almacena los datos de hogar

    Returns:
        list_disc_hogar: los devuelve ya modificados 
    """
    material_durable = ['1','2','3','4']
    material_precario = ['5','6','7']
   
    for i,dict in enumerate(list_disc_hogar):
        valor = dict['V4'].strip()
        if int(valor) in material_durable: # valor de 1 a 4 = Material durable
            list_disc_hogar[i]['MATERIAL_TECHUMBRE'] = 'Material durable'         
        elif int(valor)in material_precario: # valor de 5 a 7 = Material precario
            list_disc_hogar[i]['MATERIAL_TECHUMBRE'] = 'Material precario'
        else:
            list_disc_hogar[i]['MATERIAL_TECHUMBRE'] = 'No aplica'
    return list_disc_hogar