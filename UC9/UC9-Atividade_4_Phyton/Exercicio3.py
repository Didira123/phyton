
print("Diga 25 números inteiros na mesma linha, separados por um espaço:")
valores = input().split(" ")

matriz25 = []

for i in range(5):
    matriz25.insert(i, [])
num = 0
for l in range(5):
    for c in range(5):
        matriz25[l].insert(c, valores[num])
        num+=1

print("Digite um número para ser buscado na matriz: ")
busca = input()
achou = False
l1 = 0
c1 = 0
for l in range(5):
    for c in range(5):
        if matriz25[l][c] == busca:
            achou = True; l1 = l; c1 = c; break;

if achou: print("Elemento encontrado na posição ["+str(l1)+", "+str(c1)+"]")
else: print("Elemento não encontrado!")
