#!/usr/bin/env python3

def factorial(n):
  result = 1
  for x in range(1,n+1):
    result = result * x
  return result

for n in range(0,10):
  print("Factorial of {} is {}.".format(n,factorial(n)))
