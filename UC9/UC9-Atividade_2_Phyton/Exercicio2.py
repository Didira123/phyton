print("Diga um valor real: ", end="")
valor = float(input())

print("O valor \""+str(valor)+"\" é ", end="")
if valor > 10:
    print("maior que 10.")
elif valor < 10:
    print("menor que 10.")
elif valor == 10:
    print("igual a 10.")
