nome_aluno = input("Digite o nome do aluno: ")
rm_aluno = input("Digite o RM: ")
nota1 = float(input("Digite a nota da primeira Ac: "))
nota2 = float(input("Digite a nota da segunda Ac: "))
nota3 = float(input("Digite a nota da terceira Ac: "))

nota_final = int((nota1 + nota2 + nota3)/3)

print(f"Nome: {nome_aluno} \nRM: {rm_aluno}")
print(f"A nota final do aluno {nome_aluno} é: {nota_final}")