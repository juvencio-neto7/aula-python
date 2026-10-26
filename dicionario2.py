# 4. Uso do .key() e .values() para listar informações básicas
print(f'Campos do perfil: {list(usuario.keys())}')
print(f'Dados salvos: {list(usuario.values())}')

# 5. Uso do .items() para percorrer e exibir o perfil completo de forma bonita
print('\n--- Perfil atualizado ---')
for chave, valor in usuario.items():
    print(f'{chave.capitalize()}: {valor}')

# 6. Uso do .pop() para remover uma credencial sensível antes de exibir dados públicos
# Remove a chave e guarda o valor removido
nivel_removido = usuario.pop('nível')
print(f"\nNível {nivel_removido} removido por segurança.")

