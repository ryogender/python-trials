""" Program to print prime numbers until a given value"""


def main():
    a = int(input("value"))
    for b in range(1, a + 1):
        if b > 1:
            for i in range(2, b):
                if (b % i) == 0:
                    break
            else:
                print(b)


if __name__ == '__main__':
    main()
