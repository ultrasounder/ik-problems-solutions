def  bubbleSort(A):
    n = size(A)
    for start in range(n):
        for i in range(n-1,start,-1):
            if A[i-1] > A[i]:
                A[i-1], A[i] = A[i], A[i-1]
    return A
