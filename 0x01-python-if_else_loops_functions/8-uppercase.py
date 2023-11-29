#!/usr/bin/python3
def uppercase(str):
  for i in str:
    if ord(i) >= 97and ord(i) <= 123:
      x = chr(ord(i) - 32)
      print(x, end='')
  print("")
