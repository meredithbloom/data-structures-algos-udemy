
# module to assess time performance. like a mini stopwatch
import time

nemo = ['nemo']
# creating new array with many of same value
large = ['nemo'] * 100
# or can use list comprehension
large = ['nemo' for i in range(100)]
print(large)


def findNemo(array):
    for i in range (len(array)):
        if array[i] == 'nemo':
            print('FOUND NEMO!')


t0 = time.perf_counter()            
findNemo(large)
t1 = time.perf_counter()
print(f'execution time is {t1-t0} seconds')