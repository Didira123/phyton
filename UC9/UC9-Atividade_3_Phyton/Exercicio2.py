print("Diga um número inteiro (base para a tabuada), o número de início")
print("e o número de fim da tabuada (separe-os com um espaço): ", end="")
valores = input().split(" ")
print()

r = 1
b = 1
if int(valores[1]) > int(valores[2]):
    r = -1
    b = -1

a = int(valores[1])
b += int(valores[2])

for i in range(a, b, r):
    print("[" + valores[0] + "] * [" + str(i) + "] = [" + str(int(valores[0])*i) + "]")
