"""
IV3 N (1) 
Los pisos interiores son principalmente de...
    1. mosaico / baldosa / madera / cerámica / alfombra
    2. cemento / ladrillo fijo
    3. ladrillo suelto / tierra
IV6 N(1) 
Tiene agua...
    1. por cañería dentro de la vivienda
    2. fuera de la vivienda pero dentro del terreno
    3. fuera del terreno
IV7 N(1)
El agua es de...
    1. red pública (agua corriente)
    2. perforación con bomba a motor
    3. perforación con bomba manual
IV8 N (1) 
¿Tiene baño / letrina?
    1 = Sí
    2 = No
IV9 N (1) 
El baño o letrina está...
    1. dentro de la vivienda
    2. fuera de la vivienda, pero dentro del terreno
    3. fuera del terreno
IV10 N (1) 
El baño tiene...
    1. inodoro con botón / mochila /cadena y arrastre de agua
    2. inodoro sin botón / cadena y con arrastre de agua (a balde)
    3. letrina (sin arrastre de agua)
IV11 N (1) 
El desague del baño es...
    1. a red pública (cloaca)
    2. a cámara séptica y pozo ciego
    3. solo a pozo ciego
    4. a hoyo/excavación en la tierra

MATERIAL_TECHUMBRE: creado anteriormente
"""
def condicion_de_habitabilidad(h):
    # Inicializa puntaje
    points = 0

    # Condición inmediata de habitabilidad insuficiente
    # Si no hay baño o agua
    if (h["IV8"] == '1' or h["IV6"] == '3'):
        h["CONDICION_DE_HABITABILIDAD"] = "Insuficiente"
    else:
        # Condiciones estructurales básicas del hogar

        # Tipo de vivienda (mejor cuanto menor el número)
        match h["IV3"] :
            case "2":
                points += 1
            case "1":
                points += 2
         # Tipo de baño
        match h["IV6"] :
            case "2":
                points += 1
            case "1":
                points += 2
        # Tipo de agua
        match h["IV7"] :
            case "3":
                points += 1
            case "2":
                points += 2
            case "1":
                points += 3
        # Tipo de desagüe
        match h["IV9"] :
            case "2":
                points += 1
            case "1":
                points += 3
        #Tipo baño
        match h["IV10"] :
            case "2":
                points += 1
            case "1":
                points += 2
        #Manejo de desague
        match h["IV11"] :
            case "2":
                points += 2
            case "1":
                points += 4

        match h["MATERIAL_TECHUMBRE"]:
            case "Material precario":
                points += 1
            case "Material durable":
                points += 2

        # Asignación final según puntaje acumulado
        if points >= 6 :
            h["CONDICION_DE_HABITABILIDAD"] = "Regular"
        elif points >= 10 :
            h["CONDICION_DE_HABITABILIDAD"] = "Saludable"
        else:
            h["CONDICION_DE_HABITABILIDAD"] = "Buena"
        