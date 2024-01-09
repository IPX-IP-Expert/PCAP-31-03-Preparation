import time


# Define a class generator for a Fibonacci
class Fib:
    def __init__(self, number) -> None:
        self.__n = number
        self.__i = 0
        self.__v1 = self.__v2 = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.__i += 1
        if self.__i > self.__n:
            raise StopIteration
        if self.__i in [1, 2]:
            return 1
        stack = self.__v1 + self.__v2
        self.__v1, self.__v2 = self.__v2, stack
        return stack


print("--------FIB---------")
for i in Fib(10):
    print(i)
print("-----------------")


# Define a generator using a yield statement
def fib(number):
    i, v1, v2 = 0, 1, 1
    while i < number:
        if i in [0, 1]:
            yield 1
        else:
            stack = v1 + v2
            v1, v2 = v2, stack
            yield stack
        i += 1


print("USING YIELD")
print("-----------------")
for i in fib(10):
    print(i)
print("-----------------")
