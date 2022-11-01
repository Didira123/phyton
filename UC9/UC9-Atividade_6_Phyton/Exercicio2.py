def trianguloDeNumeros(num):
    t = 1
    for a in range(1, num + 1):
        for b in range(1, t + 1, 1):
            print(a, end=" ")
        print()
        t += 1

print("Farei a impressão de um triângulo retângulo formado por")
print("linhas de números. Diga quantas linhas este terá: ")
num = int(input())
trianguloDeNumeros(num)
