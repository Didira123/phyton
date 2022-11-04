def adicionaNoVetor(vetor, tamanho):
    for i in range(tamanho):
        vetor.append(int(input("Valor "+str(i+1)+" = ")))

print("Diga 10 números inteiros na mesma linha (separe-os com um espaço): ")
vetor1 = []
adicionaNoVetor(vetor1, 10)
print("Diga mais 10 números inteiros: ")
vetor2 = []
adicionaNoVetor(vetor2, 10)
vetor3 = []
for i in range(10):
    vetor3.append(vetor1[i]);
    vetor3.append(vetor2[i]);

print("lista 1 = ", vetor1)
print("lista 2 = ", vetor2)
print("Juntando as 2 listas de números de forma intercalada, temos:\n", vetor3)

