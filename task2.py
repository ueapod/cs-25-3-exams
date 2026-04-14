def calculate_S(n,k=1, p=1, s=0):
  if k > n:
   return s

  p *=((-1)**(k+1)) /k
  s+= p 
  
  return calculate_S(n,k + 1, p, s)

  n=int(input("Введите натуральное число n:"))
  print(calculate_S(n))