print("Diga uma operação entre 2 números digitando o 1º número, seguido da operação")
print("(digito único), seguida do outro número (sem espaços).", end="")
fim = "s"
while fim.lower() == "s":
    print("Calculo: ", end="")
    calculo = input()

    # Calcula a conta na String automaticamente:
    #
    # calculo = eval(input())
    # print (calculo)

    ANS = 0

    if len(calculo.split("^")) > 1:
        a = calculo.split("^")

        if a[0].casefold().upper() == "ANS":
            print(ANS**float(a[1]))
        elif a[1].casefold().upper() == "ANS":
            print(float(a[0])**ANS)
        else:
            print(float(a[0]) ** float(a[1]))

    elif len(calculo.split("*")) > 1:
        a = calculo.split("*")
        if a[0].casefold().upper() == "ANS":
            print(ANS*float(a[1]))
        elif a[1].casefold().upper() == "ANS":
            print(float(a[0])*ANS)
        else:
            print(float(a[0]) * float(a[1]))

    elif len(calculo.split("/")) > 1:
        a = calculo.split("/")
        if a[0].casefold().upper() == "ANS":
            print(ANS/float(a[1]))
        elif a[1].casefold().upper() == "ANS":
            print(float(a[0])/ANS)
        else:
            print(float(a[0]) / float(a[1]))

    elif len(calculo.split("+")) > 1:
        a = calculo.split("+")
        if a[0].casefold().upper() == "ANS":
            print(ANS + float(a[1]))
        elif a[1].casefold().upper() == "ANS":
            print(float(a[0])+ANS)
        else:
            print(float(a[0])+float(a[1]))
    elif len(calculo.split("-")) > 1:
        a = calculo.split("-")
        if a[0].casefold().upper() == "ANS":
            print(ANS-float(a[1]))
        elif a[1].casefold().upper() == "ANS":
            print(float(a[0])-ANS)
        else:
            print(float(a[0]) - float(a[1]))
    elif len(calculo.split("%")) > 1:
        a = calculo.split("%")
        if a[0].casefold().upper() == "ANS":
            print(ANS%float(a[1]))
        elif a[1].casefold().upper() == "ANS":
            print(float(a[0])%ANS)
        else:
            print(float(a[0]) % float(a[1]))
    else :
        print("Operação não implementada!")

    print("Continuar operação da calculadora? (s/n)")
    fim = input()
