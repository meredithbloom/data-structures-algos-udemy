# given two arrays, create a function that tells a user whether the arrays have any common items (return true/false)

def are_commons(array1, array2):
    for num in array1:
        if num in array2:
            return True
    return False

a = ['a','b','c','d','e']
b = ['z','g','f','a']

print(are_commons(a, b))