from typing import Callable

MultiplierOf = Callable[[int], int]


# Create a closure that will be a multiplier
# multiplier_of function will return a multiplier function
# multiplier function will take a number and multiply it with the number passed to multiplier_of function
def multiplier_of(n):
    def multiplier(number):
        return number * n

    return multiplier


# Another way to write the same function using predefined types
def multiplier_of2(n: int) -> MultiplierOf:
    def multiplier(number: int) -> int:
        return number * n

    return multiplier


if __name__ == "__main__":
    print("Closure example")
    multiplywith5 = multiplier_of(5)
    print(multiplywith5(9))
    print(multiplywith5(10))

    print("------------------------------------")
    print("Closure example with predefined types")
    multiplyWith4 = multiplier_of2(4)
    print(multiplyWith4(9))
