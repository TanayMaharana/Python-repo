#!/usr/bin/env python3

def sum_divisor(n):
  divisors = []
  for number in range (1,n):
    if n % number == 0:
      divisors.append(number)
    else:
      pass
  return sum(divisors)
