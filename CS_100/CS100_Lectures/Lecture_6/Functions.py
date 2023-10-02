# Functions - Lecture 6

# Defining a Function
def my_function():
    print("Hello from a function")
my_function()

'''
def: Function definition keyword
my_function: Function name
(): Arguments (Variable Arguments)
'''

x = 16
def sqrt(x):
    return x**0.5
print(sqrt(x))

# Using Function to Caluclate the Area of a Cirlce from User Input
def area_of_circle(radius):
    return 3.14 * radius**2
radius = float(input("Enter the radius of the circle: "))
print(area_of_circle(radius))