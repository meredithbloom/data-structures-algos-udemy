# BUBBLE SORT

# worst/average case is O(n^2) time complexity. O(1) space complexity.

# bubbling up each number from greatest to least. only ever comparing two adjacent numbers at a time, then flipping their positions if needed.

nums = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

def bubble_sort(array):
    for turn in range(len(nums)): # 0 - 10. the most number of times we need to iterate through the list to check for next highest number
        for i in range(len(nums)-1): # iterate through each number
            current = nums[i]
            next_num = nums[i+1]
            if current > next_num:
                # swap numbers
                nums[i+1] = current
                nums[i] = next_num
    return(array)
    
bubble_sort(nums)