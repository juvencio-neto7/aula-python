produtos = []
print('Cadastro de produtos do supermercado Bom Preço \n')

for i in range(3):
    nome = input(f'Nome do produto {i+1}: ')
    categoria = input('Categoria: ')
    preco = float(input('Preço: R$ '))

    produto = {'nome': nome, 'categoria': categoria, 'preco': preco}
    produtos.append(produto)

consulta = input('\nDigite o nome do produto para consultar: ')