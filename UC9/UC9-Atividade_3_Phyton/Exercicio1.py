print("Diga em que turno você estuda, digitando a letra \ninicial M-matutino ou V-Vespertino ou N-Noturno: ", end="")
turno = str(input()).upper()

match turno:
    case 'M':
        print("Bom dia!")
    case "V":
        print("Boa tarde!")
    case "N":
        print("Boa noite!")
    case _:
        print("Valor inválido!")
