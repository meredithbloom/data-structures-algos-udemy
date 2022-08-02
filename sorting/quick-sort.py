# QUICK SORT
# divide and conquer
# O(n*logn) time complexity
# worst case O(logn) space complexity

# use pivoting technique to break list into smaller lists
# we use last/first elem in list as initial pivot point. either end of list

# quick sort is usually fastest sort on average. HOWEVER, worst cases are particularly bad. if i can't guarantee no bad data, can't guarantee that pivot number will be good, stay away from quick sort

numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

# left, right are index numbers
def quicksort(array, left, right):
	if left < right:
		pivot = right
	# select first and last index as 2nd and 3rd parameters
		partitionindex = partition(array, pivot, left, right)
		quicksort(array, left, partitionindex-1)
		quicksort(array, partitionindex+1, right)
	return array

# splits list into two partitions
def partition(array, pivot, left, right):
	pivotval = array[pivot]
	# on the left of the pivot
	partitionindex = left

	for i in range(left, right):
		if array[i] < pivotval:
			swap(array, i, partitionindex)
			partitionindex += 1

	swap(array, right, partitionindex)
	return partitionindex
		

# actually swaps numbers at given indices
def swap(array, firstindex, secondindex):
	temp = array[firstindex]
	end = array[secondindex]
	array[firstindex], array[secondindex] = end, temp
	#return array

print(quicksort(numbers, 0, len(numbers)-1))