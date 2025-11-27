# For loop
# The for loop iterates through each element in the array to find the target value.
arr = [10, 20, 30, 40, 50]
target = 30
for i in arr:
    if i == target:
        print(f"Found {target} using for loop")
        break
# While loop
# The while loop uses an index to traverse the array until the target value is found.
arr = [10, 20, 30, 40, 50]
target = 30 
i = 0
while i < len(arr):
    if arr[i] == target:
        print(f"Found {target} using while loop")
        break
    i += 1