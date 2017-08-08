import sys
import math


def main(line_input):
    list_input = line_input.split()
    l = int(list_input[0])
    d = int(list_input[1])
    c = int(list_input[2])

    num_trips = math.floor(l / c)
    if num_trips == 0:
        num_trips = 1

    if l > c:
        m = l % c
        if m > d - 1:
            num_trips += 1
        else:
            l = l - m

    count_snack = (d - 1) * num_trips

    l = l - count_snack
    if 0 < l:
        print(str(l))
    else:
        print("impossivel")


#for line in sys.stdin:
line = '80 10 10'
main(line)
