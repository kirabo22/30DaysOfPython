# Day 2: 30 Days of python programming

# Variable declarations
first_name = "Evelyn"
last_name = "Kirabo"
full_name = first_name + " " + last_name
country = "Uganda"
city = "Kampala"
age = 25
year = 2024
is_married = False
is_true = True
is_light_on = True

# Declare multiple variables on one line
a, b, c = 5, 10, 15
# Check data types
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

# Length of first name
print(len(first_name))

# Compare lengths of first name and last name
print(len(first_name) > len(last_name))  # True or False

# Arithmetic operations
num_one = 5
num_two = 4
total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_one % num_two
exp = num_one ** num_two
floor_division = num_one // num_two

print("Total:", total)
print("Difference:", diff)
print("Product:", product)
print("Division:", division)
print("Remainder:", remainder)
print("Exponential:", exp)
print("Floor Division:", floor_division)

# Circle calculations
radius = 30
pi = 3.14159
area_of_circle = pi * radius**2
circum_of_circle = 2 * pi * radius

print("Area of Circle:", area_of_circle)
print("Circumference of Circle:", circum_of_circle)

# User input for radius and calculate area
radius_input = float(input("Enter radius: "))
area_from_input = pi * radius_input**2
print("Area with user radius:", area_from_input)

# User input for personal details
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
country = input("Enter your country: ")
age = int(input("Enter your age: "))

print(f"First Name: {first_name}, Last Name: {last_name}, Country: {country}, Age: {age}")

# Python reserved keywords
help('keywords')

