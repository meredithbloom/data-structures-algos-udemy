# Fibonacci numbers are great with memoization

calculations = 0

# regular recursive method has time complexity of O(n^2), horribly inefficient
def fibonacci(n):
	calculations += 1
	if n < 2:
		return n
	return fibonacci(n-1) + fibonacci(n-2)


# we can use memoization to get our time complexity down to O(n)

# memoization package built by python
from functools import lru_cache

@lru_cache(maxsize=None)
# helper function
def fib(n):
	if n < 2: 
		return n
	return fib(n-1) + fib(n-2)

#fibs = [fib(n) for n in range(16)]
#print(fibs)
#print(fib.cache_info())

# memoization with cache defined outside of function (globally)

cache = {}

def memoized_fib(n):
	if n in cache:
		print('pulling from cache')
		return cache[n]
	elif n < 2:
		print(f'first time calculating fib {n}')
		cache[n] = n
		return cache[n]
	else:
		print(f'first time calculating fib '+ str(n))
		cache[n] = fib(n-1) + fib(n-2)
	print(cache)
	return cache[n]
	
x = memoized_fib(8)
# first time calculating 8th fib number
print(x)
# pulling 8th fib number from cache
print(x)
print(memoized_fib(3))
# print(fib(1))
# print(fib(2))

# memoization with cache defined inside the function

def fibo(): # time complexity is O(n), though we increase space complexity
	cache1 = {}
	
	def memoize(n):
		if n in cache1:
			return cache1[n]
		else:
			if n < 2:
				return n
			else:
				next = fib(n-1) + fib(n-2)
				cache1[n] = next
				return cache1[n]
	return memoize

memo_fib = fibo()
print(memo_fib(4))
# print(memo_fib(5))
