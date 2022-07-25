import heapq

x = [1,5,88,73,4,7,9,14]

# heapify method sorts list, min heap
heapq.heapify(x)
print(x)

# push to heap
heapq.heappush(x, 30)
print(x)

# pop from heap
print(heapq.heappop(x))
print(x)

# use pop and push to push element in at same time
heapq.heappushpop(x, 90)
print(x)

# used to get n largest elements in heap
print(heapq.nlargest(5, x))

# used to get n smallest elements in heap
print(heapq.nsmallest(2, x))
