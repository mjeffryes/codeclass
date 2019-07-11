#!/bin/bash

for i in {1..2000}
  do
    echo $i
    python3 ./generate_phone_challenge.py | fold > "sample_$i.txt"
  done
