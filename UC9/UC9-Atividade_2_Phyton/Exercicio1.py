print("Diga quantos produtos pretende comprar de iPhone, Samsung, Tablet, PS5, notebook;")
print("respectivamente separados por espaço: ", end="")
quants = input().split()
print()

produtos = ["iPhone", "Samsung", "Tablet", "PS5", "notebook"]
precos = [2980.0, 2540.0, 1950.0, 2100.0, 2350.0]

total = 0
for i in range(0, 5, 1):
    print(produtos[i]+"s = "+str(int(quants[i])*precos[i]))
    total += int(quants[i])*precos[i]

print("\n Total parcelado em 3 vezes = "+str(total/3))
print("\n Total parcelado em 6 vezes com 5% de juros = "+str(total*1.05/6))
print("\n Total à vista (10% de desconto) = "+str(total*0.9))
