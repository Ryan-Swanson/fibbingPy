# Exponential fib abusing recursion at high n 
# def fib(n):
#   if n == 0:
#     return 0
#   if n == 1:
#     return 1
#   return fib(n-1) + fib(n-2)

# fibbing = int(input("Enter the fib index: "))

# print(fib(fibbing))

#Polynomial fib with array generation
def fib2(n):
  if n == 0:
    return 0
  if n == 1:
    return 1

  f = [0,1]
  for i in range(2, n+1):
    f.append(f[i-1] + f[i-2])

  return f[n]

fibbing = int(input("Enter the fib index: "))
print(fib2(fibbing))
