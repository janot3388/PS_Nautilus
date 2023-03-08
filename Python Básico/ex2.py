#FUNÇÃO QUE CALCULA NOTA DE CADA ALUNO E RETORNA A SITUAÇÃO DE APROVAÇÃO DO MESMO
def calculaSit(x1,x2,x3):
    xF=(x1 + x2 + x3)/3
    if xF >= 7:
        return True
    else:
        return False

#INPUT DAS LISTAS DE CADA NOTA
print("\nINSIRA CADA NOTA SEPARADA COM UM ESPAÇO")
notas1 = list(map(float, input("\nINSIRA NOTAS 1 DOS 10 ALUNOS: ").split()))
notas2 = list(map(float, input("\nINSIRA NOTAS 2 DOS 10 ALUNOS: ").split()))
notas3 = list(map(float, input("\nINSIRA NOTAS 3 DOS 10 ALUNOS: ").split()))
print("")

#LOOP QUE CHAMA A FUNÇÃO CALCULASIT E RETORNA AO USUÁRIO A SITUAÇÃO DE CADA UM DOS 10 ALUNOS
for i in range (0,10):
    if calculaSit(notas1[i],notas2[i],notas3[i]) == True:
        print("Aluno", i+1, "foi aprovado.")
    else:
        print("Aluno", i+1 ,"foi reprovado.")




