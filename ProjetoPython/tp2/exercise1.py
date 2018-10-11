capacity = int(input('Informe a capacidade da memória: '))
unity = input('Informe a unidade de medida (B, KB, MB, GB): ')
lowerCase = unity.lower()

if lowerCase == 'b':
  print(f"{capacity} bytes.")
elif lowerCase == 'kb':
  print(f"{capacity * 1024} bytes.")
elif lowerCase == 'mb':
  print(f"{capacity * (1024 ** 2)} bytes.")
elif lowerCase == 'gb':
  print(f"{capacity * (1024 ** 3)} bytes.")
else:
  print('Unidade de medida não encontrada.')