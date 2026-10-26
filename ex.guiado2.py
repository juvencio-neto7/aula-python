from collections import Counter
print('Sistema de contagem de reclamações - AtendeBem\n')

reclamacoes = []
qtd = int(input('Quantas reclamações deseja registrar?  '))

for i in range(qtd):
    tipo = input(f'Reclamação {i+1}: ')
    reclamacoes.append(tipo)

contagem = Counter(reclamacoes)

print('\nRelatório de reclamações: ')
for tipo, quantidade in contagem.items():
    print(f'{tipo}: {quantidade} ocorrência(s)')