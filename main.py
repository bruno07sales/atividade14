# Entrada de dados(nome do aluno)
nome = input("Digite o nome do aluno: ")

# /diz quantas avaliações estão disponiveis
quantidade_avaliacoes = int(input('Digite o número de notas avaliadas: '))

# Inicializa a lista de notas e a soma das notas
notas = []
soma_notas = 0

# Para digitar a nota e limitar o progama a quantidade maxima de avaliações!
for i in range(quantidade_avaliacoes):
    nota = str(input(f'Digite a nota do aluno {i + 1}: ')).replace (',', '.')
    nota = float(nota)
    notas.append(nota)
    soma_notas += nota

# Calcula a média
media = soma_notas / quantidade_avaliacoes if quantidade_avaliacoes > 0 else 0

# Exibe o resultado
print(f'A média do aluno {nome} é: {media}')


