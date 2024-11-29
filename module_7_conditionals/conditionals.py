### Python Exercises Solutions

```python
# Level 1 Exercises

# Exercise 1
age = int(input("Enter your age: "))
if age >= 18:
    print("You are old enough to learn to drive.")
else:
    print(f"You need {18 - age} more years to learn to drive.")

# Exercise 2
my_age = 23  # Replace with your age
your_age = int(input("Enter your age: "))
if your_age > my_age:
    diff = your_age - my_age
    print(f"You are {diff} year{'s' if diff > 1 else ''} older than me.")
elif your_age < my_age:
    diff = my_age - your_age
    print(f"I am {diff} year{'s' if diff > 1 else ''} older than you.")
else:
    print("We are the same age.")

# Exercise 3
a = int(input("Enter number one: "))
b = int(input("Enter number two: "))
if a > b:
    print(f"{a} is greater than {b}")
elif a < b:
    print(f"{a} is smaller than {b}")
else:
    print(f"{a} is equal to {b}")

# Level 2 Exercises

# Exercise 1
score = int(input("Enter your score: "))
if 80 <= score <= 100:
    print("A")
elif 70 <= score <= 79:
    print("B")
elif 60 <= score <= 69:
    print("C")
elif 50 <= score <= 59:
    print("D")
elif 0 <= score <= 49:
    print("F")
else:
    print("Invalid score")

# Exercise 2
month = input("Enter the month: ").capitalize()
if month in ["September", "October", "November"]:
    print("The season is Autumn.")
elif month in ["December", "January", "February"]:
    print("The season is Winter.")
elif month in ["March", "April", "May"]:
    print("The season is Spring.")
elif month in ["June", "July", "August"]:
    print("The season is Summer.")
else:
    print("Invalid month")

# Exercise 3
fruits = ['banana', 'orange', 'mango', 'lemon']
new_fruit = input("Enter a fruit: ").lower()
if new_fruit in fruits:
    print("That fruit already exists in the list.")
else:
    fruits.append(new_fruit)
    print("Updated fruits list:", fruits)

# Level 3 Exercises

# Exercise 1
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

# Check if skills key exists
if 'skills' in person:
    skills = person['skills']
    middle_skill = skills[len(skills) // 2]
    print("Middle skill:", middle_skill)

    # Check for Python skill
    if 'Python' in skills:
        print("The person has Python skill.")
    else:
        print("The person does not have Python skill.")

    # Determine title based on skills
    if set(skills) == {'JavaScript', 'React'}:
        print("He is a front end developer.")
    elif set(skills) >= {'Node', 'MongoDB', 'Python'}:
        print("He is a backend developer.")
    elif set(skills) >= {'React', 'Node', 'MongoDB'}:
        print("He is a fullstack developer.")
    else:
        print("Unknown title.")

# Check marital status and country
if person['is_married'] and person['country'] == 'Finland':
    print(f"{person['first_name']} {person['last_name']} lives in Finland. He is married.")
```
