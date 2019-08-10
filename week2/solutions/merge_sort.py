# Define definition for merge which basically takes two arrays i.e., the left and right part
def merge(left, right):
    if left == []:
        return right
    elif right == []:
        return left
    elif left[0] > right[0]:
        return [right[0]] + merge(left, right[1:])
    else: # left[0] <= right[0]
        return [left[0]] + merge(left[1:], right)

    result = []  # final result array, that is an empty array

# Definition for merge sort
# this takes an input list
def mergesort(lst):
    if(len(lst) <= 1): # this means that the list is already sorted.
        return lst
    mid = int(len(lst)/2)

# left array will be mergesort applied over the list from starting index
# till the mid index
    left = mergesort(lst[:mid])

# right array will be mergesort applied recursively over the list from mid index
# till the last index
    right = mergesort(lst[mid:])

    return merge(left,right)  # finally return merge over left and right

# create an array, assign elements into it
arr = [1,9,4,3,2]
print(mergesort(arr)) # print sorted array
