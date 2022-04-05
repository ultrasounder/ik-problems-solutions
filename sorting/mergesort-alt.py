def merge_sort(arr):
    
    aux = [-1]*len(arr)
    
    def helper(A, start, end):
        if start >= end:
            return
        
        mid = start + (end-start) //2
        helper(A, start, mid)
        helper(A, mid+1, end)
        
        i = start
        j = mid+1
        k = start
        aux=[]
        while i <= mid and j <= end:
            if A[i] <= A[j]:
                aux[k] = A[i]
                i += 1
                k += 1
            else:
                aux[k] = A[j]
                j += 1
                k += 1
                
        while i <= mid:
           aux[k] = A[i]
            i += 1
            k += 1
        while j <= end:
           aux[k] = A[j]
            j += 1
            k += 1
        A[start:end+1] = aux[start:end+1]
        return
    
helper(arr, 0, len(arr)-1)
return arr
            
             