print("Diga uma operação entre 2 números digitando o 1º número, seguido da operação")
print("(digito único), seguida do outro número (sem espaços).", end="")
fim = "s"
ANS = 0
while fim.lower() == "s":
    print("Calculo: ", end="")
    calculo = input().replace(" ", "")
    # Calcula a conta na String automaticamente:
    #
    # calculo = eval(input())
    # print (calculo)

    if len(calculo.split("^")) > 1:
        a = calculo.split("^")
        if a[0].casefold().upper() == "ANS":
            ANS **= float(a[1])
        elif a[1].casefold().upper() == "ANS":
            ANS = float(a[0])**ANS
        elif a[0].casefold().upper() == a[1].casefold().upper() == "ANS":
            ANS **= ANS
        else:
            ANS = float(a[0]) ** float(a[1])
        print(ANS)
    elif len(calculo.split("*")) > 1:
        a = calculo.split("*")
        if a[0].casefold().upper() == "ANS":
            ANS *= float(a[1])
        elif a[1].casefold().upper() == "ANS":
            ANS *= float(a[0])
        elif a[0].casefold().upper() == a[1].casefold().upper() == "ANS":
            ANS *= ANS
        else:
            ANS = float(a[0]) * float(a[1])
        print(ANS)
    elif len(calculo.split("/")) > 1:
        a = calculo.split("/")
        if a[0].casefold().upper() == "ANS":
            ANS /= float(a[1])
        elif a[1].casefold().upper() == "ANS":
            ANS = float(a[0])/ANS
        elif a[0].casefold().upper() == a[1].casefold().upper() == "ANS":
            ANS = 1
        else:
            ANS = float(a[0]) / float(a[1])
        print(ANS)
    elif len(calculo.split("+")) > 1:
        a = calculo.split("+")
        if a[0].casefold().upper() == "ANS":
            ANS += float(a[1])
        elif a[1].casefold().upper() == "ANS":
            ANS += float(a[0])
        elif a[0].casefold().upper() == a[1].casefold().upper() == "ANS":
            ANS += ANS
        else:
            ANS = float(a[0])+float(a[1])
        print(ANS)
    elif len(calculo.split("-")) > 1:
        a = calculo.split("-")
        if a[0].casefold().upper() == "ANS":
            ANS -= float(a[1])
        elif a[1].casefold().upper() == "ANS":
            ANS = float(a[0])-ANS
        elif a[0].casefold().upper() == a[1].casefold().upper() == "ANS":
            ANS = 0
        else:
            ANS = float(a[0]) - float(a[1])
        print(ANS)
    elif len(calculo.split("%")) > 1:
        a = calculo.split("%")
        if a[0].casefold().upper() == "ANS":
            ANS %= float(a[1])
        elif a[1].casefold().upper() == "ANS":
            ANS = float(a[0])%ANS
        elif a[0].casefold().upper() == a[1].casefold().upper() == "ANS":
            ANS = 0
        else:
            ANS = float(a[0]) % float(a[1])
        print(ANS)
    else:
        print("Operação não implementada OU valor inválido!")

    print("Continuar operação da calculadora? (s/n)")
    fim = input()
    if fim.upper() == "S": print("ANS = "+str(ANS))
