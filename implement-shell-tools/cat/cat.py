import argparse
import sys

parser = argparse.ArgumentParser(prog="cat")
parser.add_argument("-n", action="store_true")
parser.add_argument("-b", action="store_true")
parser.add_argument("files", nargs="+")

args = parser.parse_args()

line_number = 1

for file in args.files:
    with open(file) as f:
        for line in f:
            if args.b:
                if line.strip():
                    print(f"{line_number:6}\t{line}", end="")
                    line_number += 1
                else:
                    print(line, end="")
            elif args.n:
                print(f"{line_number:6}\t{line}", end="")
                line_number += 1
            else:
                print(line, end="")