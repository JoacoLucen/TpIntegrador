from pathlib import Path
import csv 


def max_año_trimestre (ruta_hogares):

    max_año = 0
    max_trimestre = 0

    with open (ruta_hogares, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader (file, delimiter=';') #lee el archivo csv y convierte cada fila en un diccionario
        for r in reader:
            año = int (r['ANO4'])
            trimestre = int (r['TRIMESTRE'])

            if año > max_año:
                max_año = año
                max_trimestre = trimestre
            elif año == max_año and trimestre > max_trimestre:
                max_trimestre = trimestre
    
    print (f"El año seleccionado fue {max_año} y el trimestre fue {max_trimestre}")

    return max_año, max_trimestre

def recorrer_individuos (ruta_individuos, año, trimestre, codusu):
    total_uni_sup = 0
    with open (ruta_individuos, mode='r',encoding='utf-8') as individuos_file:
        individuos_reader = csv.DictReader (individuos_file, delimiter=';')
        for ind in individuos_reader:
            if int(ind['ANO4']) == año and int(ind['TRIMESTRE']) == trimestre:
                if (ind['CODUSU'] == codusu and ind.get('NIVEL_ED_str') == 'Superior o universitario'):
                    total_uni_sup += 1
    return total_uni_sup


def recorrer_csvS (ruta_hogares,ruta_individuos,año,trimestre,resultados):
    with open (ruta_hogares, mode='r',encoding='utf-8') as file:
        reader = csv.DictReader (file, delimiter=';') #lee el archivo csv y convierte cada fila en un diccionario
        for r in reader:
            if int(r['ANO4']) == año and int(r['TRIMESTRE']) == trimestre:
                aglomerado = r['AGLOMERADO']
                codusu = r['CODUSU']
                ix_tot = int(r['IX_TOT'])

                if aglomerado not in resultados:
                    resultados[aglomerado] = {'Total': 0, 'Tiene Superior': 0}

                if ix_tot < 2:
                    resultados[aglomerado]['Total'] += 1
                else:
                    total_uni_sup = 0

                    total_uni_sup = recorrer_individuos (ruta_individuos,año,trimestre,codusu)
                    resultados[aglomerado]['Total'] += 1
                    
                    if total_uni_sup >= 2:
                        resultados[aglomerado]['Tiene Superior'] += 1
    return resultados

def top5 (resultados):

    promedios = {}

    #Calculo promedio por englomerado y lo guardo en un diccionario promedios
    for aglomerado, data in resultados.items():
        total_viviendas = data ['Total']
        con_superior = data ['Tiene Superior']

        promedio = con_superior / total_viviendas if total_viviendas > 0 else 0
        promedios[aglomerado] = promedio
    
    #ordeno el diccionario resultados por promedio y obtengo una lista de tuplas (clave,valor)
    ordenado = sorted (resultados.items(), key=lambda item: promedios[item[0]],reverse=True)

    print (ordenado)

    #Creo el diccionario nuevo con el top 5
    top_five = dict(ordenado[ :5])

    return top_five

def ranking_englomerados_nivelSup ():

    ruta_individuos = Path(__file__).resolve().parent.parent / "utils" / "IndividuosTotal.csv"
    ruta_hogares = Path(__file__).resolve().parent.parent / "utils" / "HogaresTotal.csv"

    año,trimestre = max_año_trimestre (ruta_hogares)

    resultados = {}
    recorrer_csvS (ruta_hogares,ruta_individuos,año,trimestre,resultados)
    
    return top5 (resultados)