# LINEAR SEARCH
# sequentially checks each item in list to see if it matches the searched item

def linear_search(needle, haystack): 
	# O(1) best case, O(n) worst case
	# worst case either item is at end of list, or not in list at all (we still have to search through every item)
	index = 0
	for item in haystack:
		if item == needle:
			return (index, item)
		index += 1
	return False	



numbers = [0,1,4,6,8,40,42,50,53,54,56,58]
	
# BINARY SEARCH - # O(log n) time complexity
	# works with sorted list
def binary_search(needle, haystack, low, high):
	if high >=low:
		midpoint = len(haystack)//2
		left = haystack[low:midpoint]
		right = haystack[midpoint:high]
		if needle == haystack[midpoint]:
			return True
		elif needle < haystack[midpoint]:
			return binary_search(needle, left, low, midpoint-1)
		elif needle > haystack[midpoint]:
			return binary_search(needle, right, midpoint+1, high)
	else:
		return False


print(binary_search(56, numbers, 0, len(numbers)-1))
print(binary_search(43, numbers, 0, len(numbers)-1))