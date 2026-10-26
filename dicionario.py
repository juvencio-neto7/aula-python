# Declaração do dicionário
pessoa = {'nome': 'Ana', 'idade': 25}
# Acesso direto (forma padrão)
print(pessoa['nome'])
# Saída: Ana
# Acesso seguro com método .get()
print(aluno['nome']) # Evita erros se a chave não existir
print(pessoa.get('idade'))
# Saída: 25