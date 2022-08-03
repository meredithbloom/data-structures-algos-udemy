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



# BINARY SEARCH - # O(log n) time complexity
def binary_search(needle, haystack):
	pass