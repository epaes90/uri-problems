
def main():
    times = int(input())
    for i in range(times):
        line = str(input())
        list = line.split()
        num1 = int(list[0])
        num2 = int(list[1])

        piles = mdc(num1, num2)

        print(str(piles))


def mdc(num1, num2):
    resto = None
    while resto is not 0:
        resto = num1 % num2
        num1 = num2
        num2 = resto

    return num1

main()
