from pathlib import Path

path = Path('usu_individual_T324.txt') 

with open (path, "r") as fp:
    text = fp.read()

headers = [x.strip('"') for x in text.split("\n")[0].split(";")]

print(headers)

exit()
data = []

text_line = text.split("\n")[1:]

for line in text_line:
    line_data = {}
    line_split = line.split(";")
    for key,value in enumerate(line_split): # me devuelve a lista con cada elemento con su indice.
        value = value.strip('"') # me elimina las ""
        line_data[headers[key]] = value # me rellena el diccionario de manera que quede como key el header y el valor el value.
    data.append(line_data) #

def add_uni(data):
    for info in data:
        if not info.get("NIVEL_ED") :
            continue # SI NO ENCUENTRA EN UN ELEMENTO DE LA LISTA EL ATRIBUTO NIVEL_ED CONTINUA BUSCANDO
    if info["NIVEL_ED"] <= 3 and info["NIVEL_ED"] >= 7:
        univ = 2
    elif info["NIVEL_ED"] > 3 and info["NIVEL_ED"] <= 5 :
        univ = 0
    elif info["NIVEL_ED"] == 6:
        univ = 1
    info["UNIVERSITARIO"] = univ

add_uni(data)