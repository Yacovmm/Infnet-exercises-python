names = []
nome = ''

while nome.lower() != 'sair':
  nome = input(f'Entre com os nomes desejados ou escreva sair para finalizar a aplicação: ')
  if nome.lower() != 'sair': names.append(nome)

print(names) 



