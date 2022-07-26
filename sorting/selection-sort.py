# SELECTION SORT

# also relatively simple though inefficient method. avg/worst case is O(n^2) time complexity. O(1) space complexity

# scans list for smallest item, then moves that item to corresponding index in the list. i.e. smallest item will go in first spot, second smallest in second slot, and so on


nums = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

def selection_sort(array):
    for n in range(len(nums)): # max number of times we'll need to go through (no number is in the right slot). when we first begin each loop, we know that the first number in the array is the lowest
        lowest = nums[n]
        # we only ever want this to start looking from the nth position
        # once this loop is over, we'll have found the next lowest number
        for i in range(n, len(nums)):
            if nums[i] < lowest:
                lowest = nums[i]
                low_index = i 
        swapping = nums[n]
        nums[n] = lowest
        nums[low_index] = swapping
    print(nums)
        

selection_sort(nums)