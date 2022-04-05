def selectionSort(A):
    n = size(A) 
    for in range(   n-1):
        minval = A[i]
        minindex = i
        for red in range(i + 1, n-1):
            if A[i] < minval:
                minval = A[red]
        A[i], A[minindex] = A[minindex], A[i]
    return A

