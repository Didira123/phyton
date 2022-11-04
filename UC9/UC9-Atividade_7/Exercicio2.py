print("Informe o preço de cada unidade de pão: ")
preco = float(input())

print("Tabela de preços")
for i in range(50):
    print((i+1), " - R$ %.2f" % (preco*(i+1)))
