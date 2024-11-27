# 1. Declare variables with different data types
age = 25  # Integer
height = 5.9  # Float
complex_number = 3 + 4j  # Complex number

# 2. Calculate the area of a triangle
base = float(input("Enter base of the triangle: "))
height = float(input("Enter height of the triangle: "))
area_triangle = 0.5 * base * height
print(f"The area of the triangle is {area_triangle}")

# 3. Calculate the perimeter of a triangle
a = float(input("Enter side a of the triangle: "))
b = float(input("Enter side b of the triangle: "))
c = float(input("Enter side c of the triangle: "))
perimeter_triangle = a + b + c
print(f"The perimeter of the triangle is {perimeter_triangle}")

# 4. Calculate the area and perimeter of a rectangle
length = float(input("Enter length of the rectangle: "))
width = float(input("Enter width of the rectangle: "))
area_rectangle = length * width
perimeter_rectangle = 2 * (length + width)
print(f"The area of the rectangle is {area_rectangle}")
print(f"The perimeter of the rectangle is {perimeter_rectangle}")

# 5. Calculate the area and circumference of a circle
radius = float(input("Enter radius of the circle: "))
pi = 3.14
area_circle = pi * radius * radius
circumference_circle = 2 * pi * radius
print(f"The area of the circle is {area_circle}")
print(f"The circumference of the circle is {circumference_circle}")

# 6. Calculate the slope, x-intercept, and y-intercept for y = 2x - 2
x1, y1 = 2, 2
x2, y2 = 6, 10
slope = (y2 - y1) / (x2 - x1)
x_intercept = -2 / 2  # x = -c/m (for y = mx + c)
y_intercept = -2  # For y = mx + c, when x = 0
print(f"Slope is {slope}")
print(f"x-intercept is {x_intercept}")
print(f"y-intercept is {y_intercept}")

# Euclidean distance between (2, 2) and (6, 10)
distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print(f"The Euclidean distance between (2, 2) and (6, 10) is {distance}")

# 7. Compare slopes
slope1 = 2
if slope1 == slope:
    print("The slopes are the same.")
else:
    print("The slopes are different.")

# 8. Solve y = x^2 + 6x + 9 for different x values
x_values = [0, 1, -1, 2, -2]
for x in x_values:
    y = x ** 2 + 6 * x + 9
    print(f"For x = {x}, y = {y}")

# 9. Compare lengths of 'python' and 'dragon'
len_python = len('python')
len_dragon = len('dragon')
if len_python != len_dragon:
    print("The lengths of python and dragon are not the same.")

# 10. Use `and` operator to check if 'on' is in both 'python' and 'dragon'
if 'on' in 'python' and 'on' in 'dragon':
    print("The substring 'on' is found in both 'python' and 'dragon'.")
else:
    print("The substring 'on' is not found in both 'python' and 'dragon'.")

# 11. Use `in` operator to check for 'jargon' in a sentence
sentence = "I hope this course is not full of jargon."
if 'jargon' in sentence:
    print("The word 'jargon' is in the sentence.")
else:
    print("The word 'jargon' is not in the sentence.")

# 12. Length of 'python' and convert to float and string
length_python = len('python')
float_length = float(length_python)
str_length = str(float_length)
print(f"Length of 'python': {length_python}, as float: {float_length}, as string: {str_length}")

# 13. Check if a number is even or not
number = 10
if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")

# 14. Check if floor division of 7 by 3 is equal to int converted value of 2.7
if 7 // 3 == int(2.7):
    print("The condition is true.")
else:
    print("The condition is false.")

# 15. Check if type of '10' is equal to type of 10
if type('10') == type(10):
    print("The types are the same.")
else:
    print("The types are different.")

# 16. Check if int('9.8') is equal to 10
if int(9.8) == 10:
    print("The condition is true.")
else:
    print("The condition is false.")

# 17. Script to calculate weekly earnings
hours = float(input("Enter hours worked: "))
rate_per_hour = float(input("Enter rate per hour: "))
weekly_earning = hours * rate_per_hour
print(f"Your weekly earning is {weekly_earning}")

# 18. Script to calculate seconds a person has lived
years = int(input("Enter number of years you have lived: "))
seconds_in_a_year = 31536000  # 60 * 60 * 24 * 365
total_seconds = years * seconds_in_a_year
print(f"You have lived for {total_seconds} seconds.")

# 19. Script to display a table
for i in range(1, 6):
    print(f"{i} {i**1} {i**2} {i**3} {i**4}")

