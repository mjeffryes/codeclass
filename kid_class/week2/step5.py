from random import random

last_row = ["#"] * 20
for i in range(1, 10):
  for j in range(1, 20):
    threshold = 0.5
    if last_row[j] == "#":
      threshold = threshold + 0.2
    if last_row[j-1] == "#":
      threshold = threshold + 0.2

    if i == 1 or i == 9 or j == 1 or j == 19:
      print("#", end="")
    elif (i % 2 == 1 and j % 2 == 1):
      print("#", end="")
    elif (i % 2 == 1 or j % 2 == 1) and random() > threshold:
      print("#", end="")
      last_row[j] = "#"
    else:
      print(" ", end="")
      last_row[j] = " "

  print("")


