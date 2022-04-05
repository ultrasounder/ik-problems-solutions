# polish national fla probelm. simpler ver of dutch national flag
def solve(arr):
    odd = -1
    for even in range(len(arr)):
        if arr[even] % 2 == 0:
            odd += 1
            arr[even], arr[odd] = arr[odd], arr[even]
    return arr





