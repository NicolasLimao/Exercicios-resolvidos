
num_materias = int(input('Digite o numero de matérias que você cursa na faculdade:'))
provas = int(input('Digite a quantidade de avaliações que você tem no bimestre:'))

notas = []
for c in range(num_materias):
    print(f'\nMatéria {c+1}:')
    nota_total= 0
    for i in range (1,4):
        nota = float(input(f'informe a nota da avaliação:'))
        nota_total += nota
    notas.append(nota_total/num_materias)

print('\nMédias finais:')
for c, nota in enumerate(notas):
    print(f'Matéria {c+1}: {nota:.1f}')
if nota_total >= 6:
    print('Você passou de ano!')
elif nota_total <= 5.9:
    print('Você terá que ficar recuperação :(')

