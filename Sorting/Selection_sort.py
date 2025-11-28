# Selection sort
# Selection sort also work like a Bubble sort but in hear we will not compare the all elements
# Once select the element and compare with all the other element and place in the correct position
# Time complexity
# Best O(n²)
# Average O(n²)
# Worst O(n²)

arr = [5,7,8,2,4,1,9,7]

for i in range(len(arr)):
    min_inx = i
    for j in range(i+1,len(arr)):
        if arr[j] < arr[min_inx]:
            min_inx = j
    arr[i],arr[min_inx] = arr[min_inx],arr[i]

print(arr)