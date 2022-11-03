print("Diga quanto tempo se passou para que os casais de coelhos possam se reproduzir, em meses: ", end="")
meses = int(input())

casais = 0
anterior = 1
antesAnterior = 0
for i in range(1, meses):
    casais=anterior+antesAnterior
    antesAnterior=anterior
    anterior=casais

if meses == (1 or 0):
    casais=1

print("O número de colehos após", meses,"meses é:", casais)

# 1 1 2 3 5 8 13 21 34 55 89 144 288