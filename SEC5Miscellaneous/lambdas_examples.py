from random import seed, randint

# Give the following formula: f(x) = 2x2 - 4x + 2
# write a script that resolve it and print the result for a set of values


# Function to print the results, takes a list of values and a function
def print_results(args, fun):
    for x in args:
        print(f"f({x}) = {fun(x)}")


def filter_odd_numbers(numbers: list[int]) -> list[int]:
    return list(filter(lambda n: n % 2 == 0 and n > 0, numbers))


# Convert a list of temperatures in Celsius
def cel_to_fah(celsius: float) -> float:
    celsius_temps = [0, 10, 20, 30, 40]
    fahrenheit_temps = list(map(lambda c: (9 / 5) * c + 32, celsius_temps))

    print("-----------------")
    print("Celsius")
    print(celsius_temps)
    print("-----------------")
    print("Fahrenheit")
    print(fahrenheit_temps)


if __name__ == "__main__":
    seed()
    numbers = [randint(-20, 20) for _ in range(10)]
    print(f"Numbers: {numbers}")
    print(f"Odd numbers: {filter_odd_numbers(numbers)}")
