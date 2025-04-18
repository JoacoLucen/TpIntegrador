# from pathlib  import Path
# #import mi_test
# #folder = Path('tp')/'data_zip'
# #list_disc_indi = mi_test.dataset_individuals(folder)
# import csv
# file = Path('tp')/'data'/'usu_individual_T216.txt'
# CH04_str= ''
# list_disc_indi = []
# with open (file, encoding="utf-8") as data:
#     reader = csv.DictReader(data, delimiter=';')
#     for row in reader:
#         list_disc_indi.append(row)

def int_to_str (list_disc_indi):
    """cambia losv alores de CH04 de integer a string
        valor 1 = Masculino.
        valor 2 = Femenino.
        
    Args:
        list_disc_indi (list_disc): recibe los datos en crudo

    Returns:
        _type_: los devuelve ya modificados
    """
    for i,dict in enumerate(list_disc_indi):
        if list_disc_indi[i]['CH04'] == '1':
                list_disc_indi[i]['CH04_str'] = 'Masculino'
        else:
            list_disc_indi[i]['CH04_str'] = 'Femenino'
    return list_disc_indi



    
        