
# module to assess time performance. like a mini stopwatch
import time

nemo = ['nemo']
# creating new array with many of same value
large = ['nemo'] * 100
# or can use list comprehension
large = ['nemo' for i in range(100)]
#print(large)

# O(n) - linear time. each item in array will be printed. number of steps increases 1:1 with length of array/input
def findNemo(array):
    for i in range (len(array)):
        if array[i] == 'nemo':
            print('FOUND NEMO!')
            break

# t0 = time.perf_counter()            
# findNemo(large)
# t1 = time.perf_counter()
# print(f'execution time is {t1-t0} seconds')

# O(1) - constant time
nums = [0,1]

def constant(arr):
    print(arr[0])

# even if function has print arr[0], print arr[1], it's still o(1) because the time taken is constant regardless of size of input


# O(n + m)
def two_inputs(n,m):
    for i in range(n):
        print(n)
    for j in range(m):
        print(j)




# O(n^2) - nested loops

pairs = [1,2,3,4,5]

def get_pairs(nums):
    for num in nums:
        for num2 in nums:
            print(num,num2)

#get_pairs(pairs)


# space complexity - O(n) - size of new data structure grows linearly depending on size of input

def growing_array(n):
    hi_array = []
    for i in range(n):
        hi_array.append('hi')
    return hi_array

print(growing_array(6))