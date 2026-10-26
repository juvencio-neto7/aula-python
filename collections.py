from collections import namedtuple
# 1. Definido do molde da coleção (Nome da estrutura e seus atributos)
pessoa = namedtuple('Pessoa', ['nome', 'idade'])

# 2. Declaração / Instanciação da colção com os dados 
usuario = Pessoa(nome='Ana', idade=25)

# 3. Acesso aos dados por nome do atributo (abstração de dicionário/objeto)
print(usuario.nome) # Saída: Ana 

# 4. Acesso aos dados por índice numérico (comportamento de tupla)
print(usuario[1]) # Saída: 25