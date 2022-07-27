# INSERTION SORT

# useful when we're pretty sure the list is mostly/almost sorted AND the dataset is relatively small
# best case is O(n) time complexity

# probably pretty similar to how our brain would actually work if we had numbered blocks in front of us that we had to order

nums = [99,44,6,2,1,5,63,87,283,4,0]

def insertion_sort(array):
    length = len(array)
    # need to manage i outside of a standard loop because we will be moving things around, so index of specific numbers will change
    i = 1
    # highest number that we've already seen will always start at 0
    end = array[0]
    # first loop that puts as at a baseline of O(n)
    while i < length: # O(n)
        # if current number is less than the highest number we've seen, we want to remove it and then move it
        if array[i] < end: # if everything is already mostly sorted, we might not even need to go to second loop, which is why best case is O(n)
            temp = array.pop(i)
            # we only want to check numbers we've already seen before, starting at 0 index
            for j in range(0, i): 
                # the first time temp encounters a number higher than it, we know we've found where it needs to go
                if temp < array[j]:
                    # insert temp before first number higher than temp
                    array.insert(j, temp)
                    break
        # shift the highest number we've seen before
        end = array[i]
        # next round
        i += 1
    print(array)
    return array

insertion_sort(nums)