

# PERGUNTA E ARMAZENA AS 3 NOTAS DO USUÁRIO
nota1=float(input('INSIRA A PRIMEIRA NOTA: '))
nota2=float(input('INSIRA A SEGUNDA NOTA: '))
nota3=float(input('INSIRA A TERCEIRA NOTA: '))

#CALCULA MÉDIA E ARMAZENA EM 'notaF'
notaF=(nota1 + nota2 + nota3)/3

#VERIFICA SITUAÇÃO DO ALUNO E INFORMA A MESMA
if notaF >= 7:
    print("VOCÊ FOI APROVADO NA MATÉRIA.")
else:
    print("VOCÊ REPROVOU A MATÉRIA.")