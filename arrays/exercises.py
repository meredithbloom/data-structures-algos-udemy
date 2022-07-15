# create a function that reverses a string

def reverse(string):
    split = list(string)
    split.reverse()
    joined = "".join(split)
    print(joined)
    
    
reverse('Hi my name is Meredith')


# merge sorted arrays
a = [0,3,4,31]
b = [4,6,30]

c = [1, 3, 4, 6, 20]
d = [2, 3, 4, 5, 6, 9, 11, 76]

def merge_sorted_arrays(array1, array2):
    if len(array1)==0 or len(array2)==0:
        return a+b
    new_list = []
    i = 0
    j = 0
    while i<len(array1) and j<len(array2):
        if array1[i]<=array2[j]:
            new_list.append(array1[i])
            i+=1
        elif array2[j]<array1[i]:
            new_list.append(array2[j])
            j+=1
    return new_list+array1[i:]+array2[j:]
    
print(merge_sorted_arrays(c, d))