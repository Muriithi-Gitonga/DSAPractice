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

# PrintTriangleInDups(N)


def printTriangleRev(N):
    # Code here
    for i in range(N + 1, 1, -1):
        for j in range(1, i):
            print('*', end=' ')
        print()

# printTriangleRev(N)


def printTriangleRevNums(N):
    for i in range(N + 1, 1, -1):
        for j in range(1, i):
            print(j, end=' ')
        print()


# printTriangleRevNums(N)


def PrintIsoscelesTriangle(N):
    for i in range(1, N + 1):

        for j in range(N - i):
            print(" ", end='')
        
        for k in range(2 * i - 1):
            print('*', end='')

        for l in range(N - i):
            print(" ", end='')
        
        print()

PrintIsoscelesTriangle(N)

        
