import math


# Create a closure that will be a multiplier
# multiplier_of function will return a multiplier function
# multiplier function will take a number and multiply it with the number passed to multiplier_of function
def multiplier_of(n):
    def multiplier(number):
        return number * n

    return multiplier


multiplywith5 = multiplier_of(5)
print(multiplywith5(9))
print(multiplywith5(10))


