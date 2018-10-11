list = []

n = int(input('Digite N inicial: '))

for i in range(1, n + 1):
    number = int(input(f'Digite o {i}º número: '))
    list.append(number)

print(f'Média aritmética é {sum(list) / len(list)}.')