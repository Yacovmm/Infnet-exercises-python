

count = 0
x = 0
while x >= 0:
    x = int(input('Insira a capacidade em GBs do seu Pendrive/HD/Cartão de memória: '))
    count += x

print(f'Você possui {count} GBs no total.')