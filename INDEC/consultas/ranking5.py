from pathlib import Path
import csv
from collections import defaultdict

def max_año_trimestre(ruta_hogares):
    """
    Encuentra el año y trimestre más reciente en el archivo de hogares.
    
    Args:
        ruta_hogares (str): Ruta al archivo CSV de hogares
        
    Returns:
        tuple: (año, trimestre) más recientes
    """
    max_año = 0
    max_trimestre = 0
    
    with open(ruta_hogares, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=';')
        for r in reader:
            año = int(r['ANO4'])
            trimestre = int(r['TRIMESTRE'])
            
            # Actualizamos máximo año y trimestre en una sola comparación
            if año > max_año or (año == max_año and trimestre > max_trimestre):
                max_año, max_trimestre = año, trimestre
    
    print(f"El año seleccionado fue {max_año} y el trimestre fue {max_trimestre}")
    return max_año, max_trimestre

def cargar_individuos(ruta_individuos, año, trimestre):
    """
    Precarga los datos de individuos en un diccionario para acceso rápido.
    
    Args:
        ruta_individuos (str): Ruta al archivo CSV de individuos
        año (int): Año a filtrar
        trimestre (int): Trimestre a filtrar
        
    Returns:
        defaultdict: Diccionario con {CODUSU: cantidad con educación superior}
    """
    # Usamos defaultdict para evitar comprobar si la clave existe
    individuos_dict = defaultdict(int)
    
    with open(ruta_individuos, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=';')
        for ind in reader:
            # Filtramos por año, trimestre y nivel educativo en una sola pasada
            if (int(ind['ANO4']) == año and 
                int(ind['TRIMESTRE']) == trimestre and 
                ind.get('NIVEL_ED_str') == 'Superior o universitario'):
                
                # Incrementamos el contador para este CODUSU
                individuos_dict[ind['CODUSU']] += 1
    
    return individuos_dict

def procesar_hogares(ruta_hogares, año, trimestre, individuos_dict):
    """
    Procesa los hogares y calcula los resultados usando el diccionario precargado.
    
    Args:
        ruta_hogares (str): Ruta al archivo CSV de hogares
        año (int): Año a procesar
        trimestre (int): Trimestre a procesar
        individuos_dict (dict): Diccionario precargado de individuos
        
    Returns:
        defaultdict: Resultados por aglomerado
    """
    # defaultdict con valores por defecto para Total y Tiene Superior
    resultados = defaultdict(lambda: {'Total': 0, 'Tiene Superior': 0})
    
    with open(ruta_hogares, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=';')
        for r in reader:
            # Filtramos hogares por año y trimestre
            if int(r['ANO4']) == año and int(r['TRIMESTRE']) == trimestre:
                aglomerado = r['AGLOMERADO']
                codusu = r['CODUSU']
                ix_tot = int(r['IX_TOT'])
                
                # Siempre incrementamos el total de hogares
                resultados[aglomerado]['Total'] += 1
                
                # Solo verificamos educación superior si IX_TOT >= 2
                if ix_tot >= 2 and individuos_dict.get(codusu, 0) >= 2:
                    resultados[aglomerado]['Tiene Superior'] += 1
    
    return resultados

def top5(resultados):
    """
    Calcula el top 5 de aglomerados por porcentaje de educación superior.
    
    Args:
        resultados (dict): Resultados completos por aglomerado
        
    Returns:
        dict: Top 5 aglomerados con sus estadísticas
    """
    # Lista para almacenar (aglomerado, promedio)
    aglomerados = []
    
    for aglomerado, data in resultados.items():
        total = data['Total']
        superior = data['Tiene Superior']
        # Calculamos el porcentaje, evitando división por cero
        promedio = superior / total if total > 0 else 0
        aglomerados.append((aglomerado, promedio))
    
    # Ordenamos descendente por promedio
    aglomerados.sort(key=lambda x: x[1], reverse=True)
    
    # Creamos diccionario con top 5 incluyendo todos los datos relevantes
    return {
        k: {
            'Total': resultados[k]['Total'], 
            'Tiene Superior': resultados[k]['Tiene Superior'],
            'Porcentaje': v * 100
        } 
        for k, v in aglomerados[:5]
    }

def ranking_englomerados_nivelSup():
    """
    Función principal que coordina el cálculo del ranking.
    
    Returns:
        dict: Top 5 aglomerados con mayor porcentaje de educación superior
    """
    # Construimos rutas a los archivos
    ruta_individuos = Path(__file__).resolve().parent.parent / "utils" / "IndividuosTotal.csv"
    ruta_hogares = Path(__file__).resolve().parent.parent / "utils" / "HogaresTotal.csv"
    
    # Obtenemos el año y trimestre más reciente
    año, trimestre = max_año_trimestre(ruta_hogares)
    
    # Precargamos todos los individuos relevantes en un diccionario
    # Esto evita tener que leer el archivo múltiples veces
    individuos_dict = cargar_individuos(ruta_individuos, año, trimestre)
    
    # Procesamos los hogares usando el diccionario precargado
    resultados = procesar_hogares(ruta_hogares, año, trimestre, individuos_dict)
    
    # Calculamos y retornamos el top 5
    return top5(resultados)