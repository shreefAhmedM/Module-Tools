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

    stripped = text.strip()
    words = len(stripped.split()) if stripped else 0

    chars = len(text.encode())

    total_lines += lines
    total_words += words
    total_chars += chars

    output = ""

    if not args.l and not args.w and not args.c:
        output += f"{lines:8}{words:8}{chars:8}"
    else:
        if args.l:
            output += f"{lines:8}"
        if args.w:
            output += f"{words:8}"
        if args.c:
            output += f"{chars:8}"

    print(output, file)


if len(args.files) > 1:
    output = ""

    if not args.l and not args.w and not args.c:
        output += f"{total_lines:8}{total_words:8}{total_chars:8}"
    else:
        if args.l:
            output += f"{total_lines:8}"
        if args.w:
            output += f"{total_words:8}"
        if args.c:
            output += f"{total_chars:8}"

    print(output, "total")