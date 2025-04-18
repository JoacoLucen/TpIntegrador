#CREA LAS DOS LISTAS DE DICCIONARIOS PARA USAR CON TODOS LOS DATOS

from pathlib import Path

def clean_field(field):
    """Elimina ;, {, } y espacios alrededor de un campo"""
    return field.strip().replace("{", "").replace("}", "").replace('"', '').replace("'", "")


def cargar_txt_como_diccionarios(carpeta):
    datos = []
    archivos = sorted(Path(carpeta).glob("*.txt"))

    for archivo in archivos:
        with open(archivo, mode='r', encoding='utf-8') as f:
            lineas = (f.readlines())

        if not lineas:
            continue

        #Limpieza de headers
        encabezados = [clean_field(h) for h in lineas[0].strip().split(";")]

        for linea in lineas[1:]:
            valores = linea.strip().split(";")
            if len(valores) == len(encabezados):
                #Limpia valores y crea el diccionario
                valores_limpios = [clean_field(v) for v in valores]
                fila = dict(zip(encabezados, valores_limpios))
                datos.append(fila)

    return datos

def cargar_diccionario (tipo):
    # Definir rutas
    base_path = Path(__file__).resolve().parent.parent
    if tipo == 'individuos':
        ruta_individuos = base_path / "utils" / "data" / "individuos"
        individuos = cargar_txt_como_diccionarios(ruta_individuos)

        # Verificación
        print(f"✅ Se cargaron {len(individuos)} registros de individuos.")
        return individuos
    elif tipo == 'hogares':
        ruta_hogares = base_path / "utils" / "data" / "hogares"
        hogares = cargar_txt_como_diccionarios(ruta_hogares)

        # Verificación
        print(f"✅ Se cargaron {len(hogares)} registros de hogares.")
        return hogares


#RECIBO LA LISTA DE DICCIONARIOS Y CREO UN ARCHIVO CSV CON ESOS DATOS EN CARPETA DATA

import csv
from pathlib import Path

def guardar_como_csv(nombre_archivo, lista_diccionarios, delimitador = ";"):
    if not lista_diccionarios:
        print("⚠️ La lista está vacía, no se creó ningún archivo.")
        return

    # Obtener los nombres de columnas del primer diccionario
    columnas = list(lista_diccionarios[0].keys())

    # Ruta de salida en la carpeta "datos"

    ruta_archivo = Path(__file__).resolve().parent.parent / "utils" / f"{nombre_archivo}.csv"

    with open(ruta_archivo, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=columnas, delimiter=delimitador)
        writer.writeheader()
        writer.writerows(lista_diccionarios)

    print(f"✅ Archivo {nombre_archivo} guardado en: {ruta_archivo}")

    #guardar_como_csv ('IndividuosTotal',individuos)
    #guardar_como_csv ('HogaresTotal',hogares)
