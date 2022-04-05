# from __future__ import division

# class MergeSort(object):

#     def sort(self, data):
#         if data is None:
#             raise TypeEerror('data cannot be None')
#         return self._sort(data)

#     def _sort(self,data):
#         if len(data) > 2:
#             mid = len(data) // 2
#             left = data[:mid]
#             right = data[mid+1:]
#             left = self._sort(left)
#             right = self._sort(right)
#         return self._merge(left, right)

#     def _merge(self, left, right):
#         l = 0
#         r = 0
#         result = [] # auxiliary array for mergeing the two subarrays O(N)

#         while l <= len(left) and r <= len(right):
#             if left[l] < right[r]:
#                 result.append(l)
#                 l += 1
#             else:
#                 result.append(r)
#                 r += 1
#         while l <= len(left):
#             result.append(left[l])
#             l += 1
#         while r <= len(right):
#             result.append(right[r])
#             r += 1
#         return result

def helper(self, arr, start, end):
    
    # we look at the work done by the leafe level worker
    # if the start index is greater than the end index then we know that the leaf level worker has only
    # one level of work to do
    if start >= end:
        return
    # internal intermediate node
    mid = start + (end - start) // 2 # to avoid integer overflow
    
    # left = arr[:mid]
    # right = [mid+1:]
    helper(arr, start, mid)
    helper(arr, mid+1, end)
    # left = sort()
    # right = sort(right)
    i = start
    j = mid + 1
    aux = []
    while i <= len(left) and j <= len(right):
        if a[i] < a[j]:
            aux.append(a[i])
            i += 1
        if a[j] < a[i]:
            aux.append(a[j])
            j += 1
    # now one of the two pointers would have jumped outside the array
    # so we need to still look for either the  i or j pointer to collect the remaining numbers
    while i <= left:
        aux.append(a[i])
        i += 1
    while j <= right:
        aux.append(a[j])
        j += 1
    arr[start:end+1] = aux # copying the merged sub-arrays back into the original array
    return
    
def mergesort(arr):
    helper(arr, 0, len(arr)-1)
    return arr
        
            
    
    



