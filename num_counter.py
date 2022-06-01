#!/usr/bin/env python3

def counter(start, stop):
  x = start
  if x <= stop:
    return_string = "Counting Up: "
    while x <= stop:
      return_string += str(x)
      if x != stop:
        return_string += ","
      x += 1

  else:
    return_string = "Counting Down: "
    while x >= stop:
      return_string += str(x)
      if x != stop:
        return_string += ","
      x -= 1

  return return_string
