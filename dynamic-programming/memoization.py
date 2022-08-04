# MEMOIZATION
# specific form of caching - a way to store values for later use
# i.e. a backpack to school. instead of going home to get a pencil, we have one with us already

def add80(n):
	print('long time')
	return n + 80

# memoization #1 - cache stored as global variable
cache = {}

def memoized_add80(n):
	if n in cache:
		return cache[n]
	else:
		print('first pass')
		cache[n] = n + 80
		return cache[n]


# the first time we run this function we'll create the hash in our cache
#print(memoized_add80(5))
# so if we ever run this function again with the same input, we can just access value in memory rather than recalculating it. O(1) access
#print(memoized_add80(5))

# we want to be cautious of polluting the global scope by defining variables outside of functions. to get around this, we can define another function inside of the function


# memoization 2 - cache stored inside function
def memoized_add80():
	cache1 = {}
	
	def memoize(n):
		if n in cache:
			return cache[n]
		else:
			print('first pass')
			cache[n] = n + 80
			return cache[n]
	return memoize

memoized = memoized_add80()

print('1', memoized(6))
print('2', memoized(7))
print('3', memoized(6))