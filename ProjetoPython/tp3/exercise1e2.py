def isPositivo(a):
  if a >= 0:    
    return True
  else:
    return False



b = float(input("Insira um numero"))


print("Número Positivo") if isPositivo(b) else print("Númeor Negativo") 

