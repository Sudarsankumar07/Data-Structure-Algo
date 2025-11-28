# Insertion sort
# Insertion sort works by building a sorted portion of the array one element at a time.
# It takes each element from the unsorted portion and inserts it into its correct position in the sorted portion.
# Time complexity
# Best O(n)
# Average O(n²)
# Worst O(n²)

arr = [5,7,8,2,4,1,9,7]

for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1
    while j >= 0 and arr[j] > key:
        arr[j+1] = arr[j]
        j-=1
    arr[j+1] = key

print(arr)
