def isPar(a):
  if a % 2 == 0:    
    return True
  else:
    return False



b = float(input("Insira um numero"))


print("Número Par") if isPar(b) else print("Númeor Ímpar") 



