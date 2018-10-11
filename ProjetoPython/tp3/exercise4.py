from ProjetoPython.tp3.functions import isPar, isPositivo

a = int(input("Insira um número:"))




if isPositivo(a):
  if isPar(a):
    print("Número positivo e Pár")
  else:
    print("Número positivo e Ímpar")
else:
  print("Númeor ngativo")
