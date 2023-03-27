print("Sistema de calculo de notas e retorno aprovado/reprovado.")

print("Digite o nome do aluno:")
nome = input()

print("Digite a nota da P1:")
nota01 = float(input())

print("Digite a nota da P2:")
nota02 = float(input())

resultado = nota01 + nota02 / 2
print("A media do aluno é ", resultado)
print("Fim")