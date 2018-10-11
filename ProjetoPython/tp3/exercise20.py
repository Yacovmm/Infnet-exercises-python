s = int(input('Digite a quantidade da sequencia que deseja:'))
list = []

for number in range(1 , s + 1):
  n = int(input('Digite os números: '))
  list.append(n)

print(f'O maior valor da lista é {max(list)}')