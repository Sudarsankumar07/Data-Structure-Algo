# Merge sort
# Merge sort is a divide-and-conquer algorithm that divides the array into halves,
# sorts each half, and then merges the sorted halves back together.
# Time complexity
# Best O(n log n)  
# Average O(n log n)
# Worst O(n log n)

arr = [5,7,8,2,4,1,9,7]

def Merge_sort(arr):

    if len(arr) > 1:
        mid = len(arr)//2

        L = arr[:mid]
        R = arr[mid:]

        Merge_sort(L)
        Merge_sort(R)

        i=j=k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i+=1
            else:
                arr[k] = R[j]
                j+=1
            k+=1
        
        while i < len(L):
            arr[k] = L[i]
            i+=1
            k+=1
        
        while j < len(R):
            arr[k] = R[j]
            j+=1
            k+=1
        
    return arr

print(f"Merge sort implemented: {Merge_sort(arr)}")