#!/usr/local/bin/python3

import random

def phone_number():
  country_code = str(random.choice([1, 44])) # North American or UK numbers
  country_code = random.choice(['', country_code, '+' + country_code])
  area_code = random.sample(range(10), 3)
  prefix = random.sample(range(10), 3)
  line = random.sample(range(10), 4)

  parens = random.choice([True, False])
  linesep = random.choice([' ', '.', '-'])
  areasep = random.choice([' ', '']) if parens else random.choice([' ', linesep])

  if parens:
    area_code = ['('] + area_code + [')']

  if country_code != '':
    country_code = country_code + areasep

  whole = [country_code] + area_code + [areasep] + prefix + [linesep] + line
  return ''.join(map(str, whole))

def shuffled(filename):
  lines = []
  with open(filename) as f:
    for line in f:
      if len(line) > 1: # exclude blank lines
        lines.append(line)
  random.shuffle(lines)
  return lines

def insert_random_numbers(line):
  words = line.split(' ')
  for i in range(len(words)):
    if random.random() < 0.03: # 3% chance of inserting a number after each word
      words.insert(i, phone_number())
  line = ' '.join(words)
  return line

if __name__ == '__main__':
  for line in shuffled('plaintext.txt'):
    print(insert_random_numbers(line))

