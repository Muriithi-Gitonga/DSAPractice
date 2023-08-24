N = 5


def PrintTriangle(N):
    for i in range(N):
        for j in range(i + 1):
            print('* ', end='')
        print('')

# PrintTriangle(N)


def PrintTriangleInNums(N):
    for i in range(N):
        for j in range(i + 1):
            print(f'{j + 1} ', end='')
        print('')


# PrintTriangleInNums(N)


def PrintTriangleInDups(N):
    for i in range(1, N + 1):
        for j in range(1, i + 1):
            print(i, end=' ')
        print()

PrintTriangleInDups(N)