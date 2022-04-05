def mergerger_first_into_second(arr1, arr2):

i = len(arr) - 1
j = len(arr) - 1
k = len(arr2) - 1

while i >= 0 and j >= 0:
    if arr1[i] <= arr2[j]:
        arr2[k] = arr2[j]
        k -= 1
        j -= 1
    else:
        arr2[k] = arr1[i]
        k -= 1
        i -= 1
#gather phase
while i >= 0:
    arr2[k] = arr1[i]                      
    k -= 1
    i -= 1

while j >= 0:
    arr2[k] = arr2[j]