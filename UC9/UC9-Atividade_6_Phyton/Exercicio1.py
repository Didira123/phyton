print("Diga o quanto você ganha por hora e a quantia de horas trabalhadas por")
print("mês (separe os valores com um espaço): ", end="")
ganhoHorasMes = input().split(" ")

ganhoTotal = float(ganhoHorasMes[0])*float(ganhoHorasMes[1])

print("Salário Bruto: ",ganhoTotal)
print("Pagamentos:")
print(" - Imposto de Renda: ",(ganhoTotal*0.11))
print(" - INSS: ",(ganhoTotal*0.08))
print(" - Sindicato: ",(ganhoTotal*0.05))
print("Salário Líquido: ",(ganhoTotal*0.76))
