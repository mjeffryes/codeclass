import argparse

parser = argparse.ArgumentParser()
parser.add_argument("filename", help="the filename to print")
args = parser.parse_args()

with open(args.filename) as f:
  for line in f:
    print(line)
