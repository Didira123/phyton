print("Diga as notas, respectivamente, da prova e do trabalho do 1º, 2º, 3º e 4º bimestre (25pts cada bimestre),")
print("separando-as com um espaço. Notas: ", end="")
notas = input().split(" ")
total = 0
medias = ""
num=1
for i in range(0, 8, 2):
    total += float(notas[i])+float(notas[i+1])
    medias+=str(num)+"ª Media = "+str((float(notas[i])+float(notas[i+1]))/2)+"\n"
    num+=1
print(medias, end="")
print("Total no Ano = "+str(total))
if total>=75: print("Aluno aprovado!")
elif total>=60: print("Aluno em recuperação!")
else: print("Aluno reprovado!")
