
from collections import List
from heapq import merge
import random

def bubbleSort(arr: List[int]) -> List[int]:

    n = len(arr)

    for i in range(n):
        isSwapped = False
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                isSwapped = True
        
        if isSwapped == False:
            break
    
    return arr


def mergeSort(arr: List[int]) -> List[int]:

    n = len(arr)
    mid = n // 2
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])

    return mergeArr(left, right)

def mergeArr(left: List[int], right: List[int]) -> List[int]:
    l = 0
    r = 0
    res = []
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            res.append(left[l])
            l += 1
        else:
            res.append(right[r])
            r += 1

    res.extend(left[l:])
    res.extend(right[r:])
    return res


def quickSort(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr
    
    pivot_val = random.randint(len(arr))
    left = [a for a in arr if a < pivot_val]
    mid = [x for x in arr if x == pivot_val]
    right = [x for x in arr if x > pivot_val]

    return quickSort(left) + mid + quickSort(right)

def quickSortWithoutRandomPick(arr: List[int], left: int, right: int) -> List[int]:
    if left < right:
        p = partition(left, right, arr)
        quickSortWithoutRandomPick(left, p-1, arr)
        quickSortWithoutRandomPick(p+1, right, arr)

    return arr

def partition(left: int, right: int, arr: List[int]) -> int:
    pivot_val = arr[right]
    i = left
    for j in range(left, right):
        if arr[j] <= pivot_val:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[i], arr[right] = arr[right], arr[i]
    return i
        