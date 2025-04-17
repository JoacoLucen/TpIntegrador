def function_value (spaces,people):
    density = int(people)/int(spaces)
    if density < 1:
        return ("Bajo")
    elif density >= 1 and density <= 2:
        return ("Medio")
    else:
        return ("Alto")




def key_densidad_hogar (info_hogares):
    """Recibo la lista de diccionarios y creo la nueva key con sus respectivos values"""
    for hog in info_hogares:
        if "II1" in hog:
            spaces = hog["II1"]
            if "IX_TOT" in hog:
                people = hog["IX_TOT"]
                valor = function_value (spaces,people)
            hog["DENSIDAD_HOGAR"] = valor
        else:
            hog["DENSIDAD_HOGAR"] = None

    return (info_hogares)