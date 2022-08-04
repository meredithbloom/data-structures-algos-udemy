# Fibonacci numbers are great with memoization

calculations = 0

# regular recursive method has time complexity of O(n^2), horribly inefficient
def fibonacci(n):
	calculations += 1
	if n < 2:
		return n
	return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(6))

# we can use memoization to get our time complexity down to O(n)
