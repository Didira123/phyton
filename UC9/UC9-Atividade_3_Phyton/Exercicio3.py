print("Diga uma operação entre 2 números digitando o 1º número,")
print("seguido da operação (digito único), seguida do outro número (sem espaços): ", end="")

calculo = input()

# Calcula a conta na String automaticamente:
#
# calculo = eval(input())
# print (calculo)

if len(calculo.split("^")) > 1:
    a = calculo.split("^")
    print(float(a[0]) ** float(a[1]))
elif len(calculo.split("*")) > 1:
    a = calculo.split("*")
    print(float(a[0]) * float(a[1]))
elif len(calculo.split("/")) > 1:
    a = calculo.split("/")
    print(float(a[0]) / float(a[1]))
elif len(calculo.split("+")) > 1:
    a = calculo.split("+")
    print(float(a[0])+float(a[1]))
elif len(calculo.split("-")) > 1:
    a = calculo.split("-")
    print(float(a[0]) - float(a[1]))
elif len(calculo.split("%")) > 1:
    a = calculo.split("%")
    print(float(a[0]) % float(a[1]))
else :
    print("Operação não implementada!")
