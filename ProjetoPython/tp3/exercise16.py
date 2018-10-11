number = 0
soma = 0

while number >= 0:
    number = int(input('Digite o número: '))
    if number > 0:
        soma += number

print(f'Soma é {soma}.')