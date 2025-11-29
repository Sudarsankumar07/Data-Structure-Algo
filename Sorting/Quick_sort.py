# Quick sort
# Quick sort is a divide-and-conquer algorithm that sorts an array by selecting a 'pivot' element and 
# partitioning the other elements into two sub-arrays according to whether they are less than or greater than the pivot. 
# The sub-arrays are then sorted recursively.

arr = [5,7,8,2,4,1,9,7]

def Quick_sort(arr):
    
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr)//2]

    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return Quick_sort(left) + mid + Quick_sort(right)

print(Quick_sort(arr))
