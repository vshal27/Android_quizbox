def factorial(x):
    total =1
    while x>=1:
        total *= x
        x-=1
        print (total)
    return total

factorial(10)
