
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
A = [10000, 2, 1, 56, 3, 167]

# print(getMinMaX(A, N))

# Divide & conquer method
def find_max_min(arr, left, right):
    # Base case: If only one element, return it as both max and min
    if left == right:
        return arr[left], arr[left]
    
    # If there are two elements, compare and return max and min
    if left + 1 == right:
        if arr[left] < arr[right]:
            return arr[right], arr[left]
        else:
            return arr[left], arr[right]
    
    # Divide the array into two halves
    mid = (left + right) // 2
    max_left, min_left = find_max_min(arr, left, mid)
    max_right, min_right = find_max_min(arr, mid + 1, right)
    
    # Compare the maximum and minimum values from the two halves
    overall_max = max(max_left, max_right)
    overall_min = min(min_left, min_right)
    
    return overall_max, overall_min

# Example usage
arr = [3, 5, 1, 9, 7, 2, 8, 4,10000, 2, 1, 56, 3, 167]
max_value, min_value = find_max_min(arr, 0, len(arr) - 1)
print("Maximum:", max_value)
print("Minimum:", min_value)






        
        

        

        


