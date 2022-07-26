
# write two functions that finds the factorial of any numbers. one should use recursion, the other should just use a for loop


def factorial_recursive(number):
    if number > 1:
        return number*factorial_recursive(number-1)
    else:
        return 1
        


def factorial_iterative(number):
    total = 1
    for num in range(number, 0, -1):
        total*=num
    print(total)
    return total


factorial_iterative(5)
print(factorial_recursive(5))