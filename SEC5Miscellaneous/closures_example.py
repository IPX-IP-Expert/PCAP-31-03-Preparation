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


# Create a closure that will calculate shapes based on the type of shape passed to it
def shape_calculator(shape):
    if shape == "circle":
        # closure for calculation area and perimeter of a circle
        def circle_calculator(radius):
            area = math.pow((math.pi * radius), 2)
            perimeter = 2 * math.pi * radius
            return area, perimeter

        return circle_calculator
    elif shape == "rectangle":

        def rectangle_calculator(length, width):
            area = length * width
            perimeter = 2 * (length + width)
            return area, perimeter

        return rectangle_calculator
    else:
        raise ValueError("Unsupported shape type")


circle_calculator_closure = shape_calculator("circle")
rectangle_calculator_closure = shape_calculator("rectangle")

circle_result = circle_calculator_closure(5)
rectangle_result = rectangle_calculator_closure(4, 6)

print("Circle: Area =", circle_result[0], "Perimeter =", circle_result[1])
print("Rectangle: Area =", rectangle_result[0], "Perimeter =", rectangle_result[1])
