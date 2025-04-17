def function_value (value_original):
    if value_original == '1':
        return ("Primario incompleto")
    elif value_original == '2':
        return ("Primario completo")
    elif value_original == '3':
        return ("Secundario incompleto")
    elif value_original == '4':
        return ("Secundario completo")
    elif value_original == '5' or value_original == '6':
        return ("Primario incompleto")
    else:
        return ("Sin informacion")

        



def key_nivel_ed_str (info_individuos):
    """Recibo la lista de diccionarios y creo la nueva key con sus respectivos values"""
    for individuos in info_individuos:
        if "NIVEL_ED" in individuos:
            value_original = individuos["NIVEL_ED"]
            individuos["NIVEL_ED_str"] = function_value (value_original)
        else:
            individuos["NIVEL_ED_str"] = None

    return (info_individuos)
