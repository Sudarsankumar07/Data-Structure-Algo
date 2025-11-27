# interpolation_search
# Interpolation search is an improved variant of binary search for instances where the values in a sorted array are uniformly distributed.
# The idea of interpolation search is to go to different locations according to the value of the key being searched.
# The numbers need to be in uniform like (1,2,4,8,11,13,16) not like (1,,4,7,10,22,40,60,100,400,800)

arr = [1,2,4,8,11,13,16,18,20,22,25,28,30]
low,high = 0, len(arr)-1
target = 18

def interpolation_search(arr,target,low,high):
    if (low <= high and target >= arr[low] and target <= arr[high]):
        pos = low + ((high - low) * (target - arr[low])) // (arr[high] - arr[low])
        if arr[pos] == target:
            return pos
        if arr[pos] < target:
            return interpolation_search(arr,target,pos+1,high)
        if arr[pos] > target:
            return interpolation_search(arr,target,low,pos-1)
    return -1

print(f"Interpolation search index of the target: {interpolation_search(arr,target,low,high)}")