# MERGE SORT

# Divide and conquer
# O(n log(n)) time complexity - much more efficient than simpler sorting algorithms
# O(n) space complexity - takes up a bit more space in memory because we're using recursion

# time complexity is n * log(n) because, while we still have to look at every item once O(n), we DO NOT need to compare every item to every other item as we do with O(n^2) and nested loops


nums_odd = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
nums_even = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4]

def merge_sort(array):
    # base case
    if len(array) == 1:
        return array
    # else 
    # split array into left or right
    length = len(array)
    mid = length // 2
    left = array[:mid]
    right = array[mid:]
    print('Left {}'.format(left))
    print('Right {}'.format(right))
    
    return merge(merge_sort(left), merge_sort(right))


def merge(left, right):
    combined = []
    # do the comparison here
    leftindex = 0
    rightindex = 0
    while leftindex < len(left) and rightindex < len(right):
        if left[leftindex] < right[rightindex]:
            combined.append(left[leftindex])
            leftindex+=1
        else:
            combined.append(right[rightindex])
            rightindex+=1
    #print(left, right)
    
    print(combined + left[leftindex:] + right[rightindex:])
    print()
    #print(combined)
    return(combined + left[leftindex:] + right[rightindex:])




answer = merge_sort(nums_odd)
print(answer)