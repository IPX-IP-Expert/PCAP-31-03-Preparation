# Give the following formula: f(x) = 2x2 - 4x + 2
# write a script that resolve it and print the result for a set of values

# Function to print the results, takes a list of values and a function
def print_results(args, fun):
    for x in args:
        print(f"f({x}) = {fun(x)}")


print_results([x for x in range(-2, 3)], lambda x: 2 * x**2 - 4 * x + 2)
