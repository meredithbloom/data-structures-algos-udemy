# given a number N, return the number at Nth index value of the fibonacci sequence

def fibonacci_iterative(number):
    fibs = [1,1,2]
    if number > 2:
        for i in range(3, number+1):
            fibs.append(fibs[i-2]+fibs[i-1])
    #print(fibs[number])
    return fibs[number]
    
fibonacci_iterative(2)
fibonacci_iterative(5)    
print([fibonacci_iterative(number) for number in range(10)])

def fibonacci_recursive(number):
    if number > 1:
        return fibonacci_recursive(number-2) + fibonacci_recursive(number-1)
    else:
        return 1

print(fibonacci_recursive(2))
print(fibonacci_iterative(5))

print([fibonacci_recursive(number) for number in range(10)])
