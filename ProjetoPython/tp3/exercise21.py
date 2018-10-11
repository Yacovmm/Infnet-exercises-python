listNotas = []

for i in range(1, 11):
  nota = int(input(f'Entre com a {i}º nota:'))
  listNotas.append(nota)


media = sum(listNotas) / len(listNotas)
maiores = [i for i in listNotas if i >= media]


print(f'Notas maiores que a média: {maiores}. ')