#!/usr/bin/env python3

def multiplication_table(number):
  multiplier = 1
  while multiplier <= 5:
    result = number * multiplier
    if result >= 25:
      break
    print ("{} x {} = {}".format(number,multiplier,result))
    multiplier += 1
    print()

multiplication_table(3)
