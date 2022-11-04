def fatorial(valorFinal, num):
    if num < 0:
        return 0
    elif num == 2:
        return valorFinal*2
    elif num == 0 or num == 1:
        return 1
    else:
        valorFinal*=num
        num-=1
        return fatorial(valorFinal, num)


print("Diga um número inteiro para calcular o fatorial: ", end="")
num = int(input())
valorFatorial = fatorial(1, num)

print("O fatorial de", num, "é:", valorFatorial)

