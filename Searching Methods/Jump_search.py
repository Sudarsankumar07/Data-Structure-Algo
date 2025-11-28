# Jump search
# Jump search also work like binary search but instead of dividing the array into halves,
# it divides the array into blocks of fixed size and performs a linear search within the block where the target element is likely to be found. 

# Let’s consider the following array: (0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610). The length of the array is 16. The Jump search will find the value of 55 with the following steps assuming that the block size to be jumped is 4. 
# STEP 1: Jump from index 0 to index 4; 
# STEP 2: Jump from index 4 to index 8; 
# STEP 3: Jump from index 8 to index 12; 
# STEP 4: Since the element at index 12 is greater than 55, we will jump back a step to come to index 8. 
# STEP 5: Perform a linear search from index 8 to get the element 55.

arr = [1,4,7,9,12,15,18,22,27,57,78,83,99,110,134]
target = 78
n = len(arr)
def sqrt(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    for i in range(0,n):
        if (i*i > n or i*i < 0):
            return i-1

steps = sqrt(n)  # Calculate the optimal block size (√n)
prev = 0  # Initialize the starting position of the current block

# First while loop: Jump forward through blocks to find the block containing the target
while arr[int(min(steps,n)-1)] < target:
    prev = steps  # Save the current block's starting position
    steps += sqrt(n)  # Jump to the next block by adding block size
    if prev >= n:  # If we've jumped beyond the array bounds
        print(-1)  # Target not found
        break

# Second while loop: Perform linear search within the identified block
while arr[int(prev)] < target:
    prev += 1  # Move to the next element in the block
    if prev == min(steps,n):  # If we've reached the end of the block
        print(-1)  # Target not found
        break

# Check if the current element is the target
if arr[int(prev)] == target:
    print(f"index of the target : {int(prev)}")
