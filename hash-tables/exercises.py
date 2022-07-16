# google question
# given an array, return the first recurring character

a = [2,5,1,2,3,5,1,2,4]
# should return 2


b = [2,1,1,2,3,5,1,2,4]
# should return 1


c = [2,3,4,5]
# should return undefined


# O(n^2) solution is just to iterate through array, store unique elements in separate array

# this solution is O(n) - we still need to iterate through original array but by storing unique values as hashes in a dictionary, checking to see if num has been seen already is O(1) because accessing data in a dict has time complexity O(1)

def first_duplicate(arr):
    uniques = {}
    for num in arr:
        if num in uniques.keys():
            return num
        else:
            uniques[num] = 1
    return "undefined"




print(first_duplicate(a))
print(first_duplicate(b))
print(first_duplicate(c))