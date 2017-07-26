import math
import sys

def main(line):
    list = line.split()
    r1 = float(list[0])
    x1 = float(list[1])
    y1 = float(list[2])
    r2 = float(list[3])
    x2 = float(list[4])
    y2 = float(list[5])

    d = calc_distance(x1, y1, x2, y2)
    if r1 > 0 and (r2 < 0 or r1 >= (d + r2)):
        print("RICO")
    else:
        print("MORTO")


def calc_distance(x1, y1, x2, y2):
    if x1 > x2:
        aux = x2
        x2 = x1
        x1 = aux

    if y1 > y2:
        aux = y2
        y2 = y1
        y1 = aux

    d = math.sqrt(math.pow((x2 - x1), 2) + math.pow((y2 - y1), 2))
    return d


for line in sys.stdin:
    main(line)
