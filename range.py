'''
Given a sorted array A of size N (1 ≤ N ≤ 5 · 105),
and two numbers x, y (0 ≤ x ≤ y ≤ N ), determine the
number of elements of A in the range [x, y] (inclusive).
'''

def range_count(A:[int], x:int, y:int):
    # implemeneting two binary searches
    # one for the first occurence of x
    x_index = -1
    # one for the last occurence of y
    y_index = -1

    def binary_search(A:[int], x:int):
        # base case
        if len(A) == 1:
            if A[0] == x:
                return 0
            else:
                return -1
            
        # chcecking min and max
        if A[0] > x:
            return 0
        elif A[-1] < x:
            return len(A)-1
        
        low = 0
        high = len(A) - 1
        mid = (low + high) // 2

        while low <= high:
            mid = (low + high) // 2

            if A[mid] > x: # x is in left half
                high = mid - 1
            elif A[mid] < x: # x is in right half
                low  = mid + 1
            else:
                return mid 

    x_index = binary_search(A, x)
    y_index = binary_search(A, y)

    if x_index != -1 and y_index != -1:
        return y_index - x_index + 1

    return None

A = [1, 2, 3, 4, 5, 6, 7, 8, 9]

x = 4
y = 8
print(f"range_count({A}, {x}, {y}) = {range_count(A, x, y)}")