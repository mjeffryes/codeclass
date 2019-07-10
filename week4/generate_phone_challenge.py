#!/usr/local/bin/python3

import random

def phone_number():
  country_code = random.choice(['', '1', '+1'])
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


if __name__ == '__main__':
  for i in range(10):
    print(phone_number())

