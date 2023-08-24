N = 5

def PrintTriangle(N):
    for i in range(N):
        for j in range(i + 1):
            print('* ', end='')
        print('')

PrintTriangle(N)
