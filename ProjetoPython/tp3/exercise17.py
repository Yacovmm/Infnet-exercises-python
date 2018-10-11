colors = ['azul', 'vermelho', 'verde', 'amarelo', 'violeta', 'marrom', 'branco', 'preto']
print(colors)

colors.remove('marrom')
print(colors)

colors.append('cinza')
print(colors)

colors[:] = ['rosa' if x == 'violeta' else x for x in colors]
print(colors)

colorToRemove = input('Digite a cor para remover: ')
if colorToRemove in colors: colors.remove(colorToRemove)
print(colors)