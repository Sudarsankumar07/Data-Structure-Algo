''' 
Stack problem
Problem:
Given a list of numbers, print the next greater element for each number.
Example:
Input: [4, 5, 2, 25]
Output: [5, 25, 25, -1] '''


arr = [4, 5, 2, 25, 3]

def without_stack(arr):
    for i in range(len(arr)):
        flag = 0
        for j in range(i+1,len(arr)):
            if arr[i] < arr[j]:
                arr[i] = arr[j]
                flag = 1
                break
        for j in range(0, i):
            if arr[j] > arr[i]:
                arr[i] = arr[j]
                flag = 1
                break
        if flag == 0:
            arr[i] = -1
    return arr

print(without_stack(arr))

def with_stack(arr):
    result = [-1] * len(arr)
    stack = []
    
    for i in range(len(arr) - 1, -1, -1):
        while stack and stack[-1] <= arr[i]:
            stack.pop()
        if stack:
            result[i] = stack[-1]
        stack.append(arr[i])
    
    return result