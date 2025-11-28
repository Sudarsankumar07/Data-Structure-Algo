# Bubble sort
# The fundamental sort and it will compare the each element and sort out
# Time complexity
# Best O(n)
# Average O(n²)
# Worst O(n²)

arr = [5,7,8,2,4,1,9,7]

for i in range(len(arr)-1):
    for j in range(i,len(arr)):
        if arr[i] > arr[j]:
            arr[i],arr[j] = arr[j],arr[i]

print(arr)