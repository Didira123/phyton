print("Diga as notas, respectivamente, do 1º, 2º, 3º e 4º bimestre (25pts cada), separando-as com um espaço. ")
print("Notas: ", end="")
notas = input().split(" ")
total = 0
for i in range(4):
    total+= float(notas[i])

if total>=75: print("Aluno aprovado!")
elif total>=60: print("Aluno em recuperação!")
else: print("Aluno reprovado!")
