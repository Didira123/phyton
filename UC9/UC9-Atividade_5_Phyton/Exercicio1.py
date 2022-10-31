print("Diga 10 caracteres separados por um espaço: ", end="")
caracteres = input().split(" ")

todasConsoantes = ""

consoantes=0
for i in range(len(caracteres)):
    if caracteres[i].upper() in ["A", "E", "I", "O", "U"]:
        consoantes += 1
        todasConsoantes+=caracteres[i].upper()+" "
print("Nº consoantes lidas: "+str(consoantes))
print("Leituras: "+todasConsoantes)
