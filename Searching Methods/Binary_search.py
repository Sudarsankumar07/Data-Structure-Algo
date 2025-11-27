# Binary Search
# Binary search is better than linear search but the drawback is List or array need to be in sort
# Without recursion just using the While loop
arr = [10, 20, 30, 40, 50, 60, 70]
target = 30
n = len(arr)
low,high = 0,n-1
while low <= high:
    mid = (low + high)//2
    if arr[mid] == target:
        print(f"While loop output index of the output: {arr[mid]}")
        break
    if arr[mid] < target:
        low = mid + 1
    if arr[mid] > target:
        high = mid -1

# With Recursion we need to implement the function for this method
def binary_search(arr, target, low, high):
    if low > high:
        return -1
    mid = (low + high)//2
    if arr[mid] == target:
        return mid
    if arr[mid] < target:
        return binary_search(arr, target, low+1, high)
    if arr[mid] > target:
        return binary_search(arr,target,low,high-1)

print(f"Recursion output index of the target: {binary_search(arr, target, low, high)}")