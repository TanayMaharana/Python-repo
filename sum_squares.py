#!/usr/bin/env python3

def square(n):
  return n * n #returns the square of a number

def sum_square(number): #this function sums up the squares of the number
  sum = 0
  for n in range(0, number):
    sum += square(n) #using the previous square function
  return sum
