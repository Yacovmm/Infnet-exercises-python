notes = []
options = """
(1) - Adicionar
(2) - Remover
(3) - Modificar
(4) - Imprimir
(5) - Sair
\n
"""

option = ''
list = []

while option != '5':
    option = input(options)
    if option == '1':
        list.append(input('Dado a inserir: '))
    elif option == '2':
        remove = input('Dado a remover: ')
        if remove in list: list.remove(remove)
    elif option == '3':
        i = input('Escreva a nota que deseja modificar? ')
        m = input('Modificar por: ')
        list[:] = [m if x == i else x for x in list]
    elif option == '4':
        print(list)