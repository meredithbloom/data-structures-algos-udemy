
# module to assess time performance. like a mini stopwatch
import time

nemo = ['nemo']
# creating new array with many of same value
large = ['nemo'] * 100
# or can use list comprehension
large = ['nemo' for i in range(100)]
print(large)

# O(n) - linear time. each item in array will be printed. number of steps increases 1:1 with length of array/input
def findNemo(array):
    for i in range (len(array)):
        if array[i] == 'nemo':
            print('FOUND NEMO!')


# t0 = time.perf_counter()            
# findNemo(large)
# t1 = time.perf_counter()
# print(f'execution time is {t1-t0} seconds')


# O(1) - constant time
nums = [0,1]

def constant(arr):
    print(arr[0])

constant(nums)

# even if function has print arr[0], print arr[1], it's still o(1) because the time taken is constant regardless of size of input