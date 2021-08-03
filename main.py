import numpy as np

# Exponential fib abusing recursion at high n 
def fib(n):
  if n == 0:
    return 0
  if n == 1:
    return 1
  return fib(n-1) + fib(n-2)


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

def fib3(n, memo):
  if n in memo:
    return memo[n]
  if n == 1 or n == 2:
    result = 1
  else:
    result = fib3(n-1, memo) + fib3(n-2, memo)
  memo[n] = result
  return result

# fibbing = int(input("Enter the fib index: "))
# print(fib2(fibbing))

# fibbing = int(input("Enter the fib index: "))
# print(fib(fibbing))
memo = {}

fibbing = int(input("Enter the fib index: "))

for i in range(1,200):
  print(f'fib({i}): ',fib3(i, memo))
