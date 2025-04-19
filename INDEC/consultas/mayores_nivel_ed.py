from pathlib import Path
import csv

def aglomerados_map ():
    return {
        '2': 'Gran La Plata',
        '3': 'Bahía Blanca - Cerri',
        '4': 'Gran Rosario',
        '5': 'Gran Santa Fé',
        '6': 'Gran Paraná',
        '7': 'Posadas',
        '8': 'Gran Resistencia',
        '9': 'Comodoro Rivadavia - Rada Tilly',
        '10': 'Gran Mendoza',
        '12': 'Corrientes',
        '13': 'Gran Córdoba',
        '14': 'Concordia',
        '15': 'Formosa',
        '17': 'Neuquén - Plottier',
        '18': 'Santiago del Estero - La Banda',
        '19': 'Jujuy - Palpalá',
        '20': 'Río Gallegos',
        '22': 'Gran Catamarca',
        '23': 'Gran Salta',
        '25': 'La Rioja',
        '26': 'Gran San Luis',
        '27': 'Gran San Juan',
        '29': 'Gran Tucumán - Tafí Viejo',
        '30': 'Santa Rosa - Toay',
        '31': 'Ushuaia - Río Grande',
        '32': 'Ciudad Autonoma de Buenos Aires',
        '33': 'Partidos del GBA',
        '34': 'Mar del Plata',
        '36': 'Río Cuarto',
        '38': 'San Nicolás - Villa Constitución',
        '91': 'Rawson - Trelew',
        '93': 'Viedma - Carmen de Patagones'
    }

def planilla_mas18_conAglomerado ():
    
    planilla = {}

    ruta_individuos = Path(__file__).resolve().parent.parent / "utils" / "IndividuosTotal.csv"

    mapa_aglomerados = aglomerados_map()
    # Mostrar aglomerados disponibles con formato "Código - Nombre"
    print("Aglomerados disponibles:")
    for codigo, nombre in sorted(mapa_aglomerados.items(), key=lambda x: int(x[0])):
        print(f"{codigo} - {nombre}")

    # Solicitar selección (solo el número)
    seleccion_aglomerado = input('Seleccione el número de aglomerado: ').strip()
    
    # Validar que la selección sea válida
    while seleccion_aglomerado not in mapa_aglomerados:
        print("Código inválido. Intente nuevamente.")
        seleccion_aglomerado = input('Seleccione el número de aglomerado: ').strip()

    print('')
    print('')
    
    # Procesar el archivo filtrando por el aglomerado seleccionado
    with open(ruta_individuos, mode='r', encoding='utf-8') as individuos_file:
        individuos_reader = csv.DictReader(individuos_file, delimiter=";")
        for ind in individuos_reader:
            # Filtrar por aglomerado seleccionado
            if ind.get('AGLOMERADO') == seleccion_aglomerado:
                año = ind['ANO4']
                trimestre = ind['TRIMESTRE']
                clave = f'{año} - T {trimestre}'

                if clave not in planilla:
                    planilla[clave] = {
                        'Primario incompleto': 0,
                        'Primario completo': 0,
                        'Secundario incompleto': 0,
                        'Secundario completo': 0,
                        'Superior o universitario': 0
                    }
                
                # Sumar al nivel educativo correspondiente
                nivel_ed = ind.get('NIVEL_ED_str', '')
                if nivel_ed in planilla[clave]:
                    planilla[clave][nivel_ed] += 1
    
    if planilla:
        print(f"\nPlanilla de personas +18 según su nivel de estudios para el aglomerado de {mapa_aglomerados[seleccion_aglomerado]}:\n")
        print("{:<20} {:<20} {:<20} {:<20} {:<20} {:<20}".format(
            'Año-trimestre', 'Primario inc.', 'Primario comp.', 
            'Secundario inc.', 'Secundario comp.', 'Superior'))
        print("-" * 120)
        
        for año_trimestre in sorted(planilla.keys()):
            datos = planilla[año_trimestre]
            print("{:<20} {:<20} {:<20} {:<20} {:<20} {:<20}".format(
                año_trimestre,
                datos['Primario incompleto'],
                datos['Primario completo'],
                datos['Secundario incompleto'],
                datos['Secundario completo'],
                datos['Superior o universitario']))
    else:
        print("No hay datos para el aglomerado seleccionado.")


