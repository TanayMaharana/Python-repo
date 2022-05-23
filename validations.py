#!/usr/bin/env python3

def validate_user(username, minlen):
  assert type(username) == str, "username must string."
  if minlen < 1:
    raise ValueError("Minimum length should be greater than 1.")
  if len(username) < minlen:
    return False
  if not username.isalnum():
    return False
  return True
