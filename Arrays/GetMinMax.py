
A = [10000, 2, 1, 56, 3, 167]
N = 6

def getMinMaX(A, N):
    min_element = A[0]
    max_element =A[0]
    for j in range(N):
        if min_element > A[j]:
            min_element = A[j] 
        if max_element < A[j]:
            max_element = A[j]
           
    return min_element, max_element


print(getMinMaX(A, N))

# Divide & conquer method







        
        

        

        


