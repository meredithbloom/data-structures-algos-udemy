strings = ['a','b','c','d']
# 4*4 = 16 bytes of storage


# access
print(strings[2])   # O(1)

# push 
strings.append('e') # O(1)

# pop
strings.pop()   #O(1)

# add first element 
strings.insert(0, 'z')  # O(n) - depending on size of array
# every other element has to be shifted (iterated through)

# splice
strings.insert(2, 'g')  # O(n)
# every other element has to be shifted (iterated through)

#print(strings)

# array native python methods:
# append()  adds an element at the end of the list
# clear()   removes all elements from the list
# copy()    returns a copy of the list
# count()   returns the number of elements with the specified value
# extend()  adds the elements of a list (or any iterable) to the end of the current list
# index()   returns the index of the first element with the specified value
# insert()  adds an element at the specified position
# pop()     removes the element at the specified position
# remove()  removes the first item with the specified value
# reverse() reverses the order of the list
# sort()    sorts the list


# list objects are implemented as arrays
# they are optimized for fast fixed-length operations and incur O(n) memory movement costs for pop(0) and insert(0,v), operations which change both the size and position of the underlying data representation


#For in depth information on arrays
#https://docs.python.org/3/tutorial/datastructures.html

#to implement arrays as a stack
#https://docs.python.org/3/library/collections.html#collections.deque


list1 = strings 
print(list1)
strings.append('k')
print(list1)
list2 = list(list1)
list1.append('q')
print(strings, list1)
print(list2)