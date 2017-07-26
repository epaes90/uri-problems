
def main():
    times = int(input())
    for i in range(times):
        m = float(input())
        count = 0
        while m > 1:
            m = m / 2
            count += 1

        print("{} dias".format(count))


main()
