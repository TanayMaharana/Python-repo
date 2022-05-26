#!/usr/bin/env python3

def prime_factor(num):
  prime_factors = []
  factor = 2
  while factor <= num:
    if num % factor == 0:
      prime_factors.append(factor)
      num = num / factor
    else:
      factor += 1
  print (prime_factors)

