import sys


def main(line):
    list = line.split()
    m = int(list[0])
    n = int(list[1])

    print(fatorial(m) + fatorial(n))


def fatorial(n):
    if n <= 1:
        return 1
    else:
        return n * fatorial(n - 1)


for line in sys.stdin:
    main(line)
