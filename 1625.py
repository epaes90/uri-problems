import math


def main():
    times = int(input())
    local_best_length = 0.0000000000
    best_length = 0.0000000000
    for i in range(times): # test cases
        conjunt = int(input())

        for j in range(conjunt): # number of conjunts
            robocopies = int(input())
            list_points = []

            for k in range(robocopies): # number of robocopies
                line = input()
                list_input = line.split()
                x = float(list_input[0])
                y = float(list_input[1])
                list_points.append((x, y))

            for p in range(len(list_points)):
                for p1 in range(p + 1, len(list_points)):
                    d = calc_distance_even(list_points[p], list_points[p1])

                    if d > 0:
                        if d < local_best_length or local_best_length == 0.0:
                            local_best_length = d

            if local_best_length > best_length or best_length == 0.0000000000:
                best_length = local_best_length

            local_best_length = 0.0000000000

        print('{0:.10f}'.format(best_length))


def calc_distance_odd(p1, p2):
    if p1[0] == p2[0]:
        return p1[1] - p2[1]

    if p1[1] == p2[1]:
        return p1[0] - p2[0]

    d = math.sqrt(math.pow((p2[0] - p1[0]), 2) + math.pow((p2[1] - p1[1]), 2))
    return d


def calc_distance_even(p1, p2):
    if p1[0] == p2[0]:
        return p1[1] - p2[1]
    elif p1[1] == p2[1]:
        return p1[0] - p2[0]
    else:
        return 0
main()
