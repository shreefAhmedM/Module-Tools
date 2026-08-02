import argparse
parser = argparse.ArgumentParser(prog="wc")
parser.add_argument("-l", action="store_true", help="Count lines")
parser.add_argument("-w", action="store_true", help="Count words")
parser.add_argument("-c", action="store_true", help="Count bytes")
parser.add_argument("files", nargs="+")

args = parser.parse_args()
total_lines = 0
total_words = 0
total_chars = 0

for file in args.files:
    with open(file, "r") as f:
        text = f.read()

    lines = text.count("\n")
    words = len(text.split())
    chars = len(text)

    total_lines += lines
    total_words += words
    total_chars += chars

    if not args.l and not args.w and not args.c:
        print(lines, words, chars, file)
    else:
        if args.l:
            print(lines, end=" ")
        if args.w:
            print(words, end=" ")
        if args.c:
            print(chars, end=" ")
        print(file)
if len(args.files) > 1:
    if not args.l and not args.w and not args.c:
        print(total_lines, total_words, total_chars, "total")
    else:
        if args.l:
            print(total_lines, end=" ")
        if args.w:
            print(total_words, end=" ")
        if args.c:
            print(total_chars, end=" ")
        print("total")