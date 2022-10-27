print("Diga o 1º número: ", end="")
a = float(input())

print("Diga o 2º número: ", end="")
b = float(input())

resultados = [a+b, a-b, a*b, a/b, a**b, a%b]
operacao = ["+", "-", "*", "/", "**", "%"]

for i in range(0, 6, 1):
    print("["+str(a)+"]"+str(operacao[i])+"["+str(b)+"] = ["+str(resultados[i])+"]")
