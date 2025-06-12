from random import random

for i in range(1, 10):
  for j in range(1, 20):
    if i == 1 or i == 9 or j == 1 or j == 19:
      print("#", end="")
    elif (i % 2 == 1 and j % 2 == 1):
      print("#", end="")
    elif (i % 2 == 1 or j % 2 == 1) and random() > 0.7:
      print("#", end="")
    else:
      print(" ", end="")

  print("")


