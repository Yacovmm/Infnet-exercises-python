list = []

for i in range(1,6):
    number = int(input(f'Digite o {i}º número: '))
    list.append(number)

result = sum(list) / len(list)

if result > 6:
    print('Média é maior do que 6.')
elif result < 6:
    print('Média é menor do que 6.')
else:
    print('Média é igual a 6.')