for i in range(1,6):
    number = int(input(f'Digite o {i}º número: '))
    print(f'Número é {"par" if number % 2 == 0 else "ímpar"}.')