print("Diga 10 caracteres separados por um espaço: ", end="")
caracteres = input().split(" ")

todasConsoantes = ""

consoantes=0
for i in range(len(caracteres)):
    if caracteres[i].upper() in ["B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N",
                                 "P", "Q", "R", "S", "T", "V", "W", "X", "Y", "Z"]:
        consoantes += 1
        todasConsoantes+=caracteres[i].upper()+" "
print("Nº consoantes lidas: "+str(consoantes))
print("Leituras: "+todasConsoantes)
