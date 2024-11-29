### Dictionary Exercises

#### Level 1

```python
# Create an empty dictionary called dog
dog = {}

# Add name, color, breed, legs, age to the dog dictionary
dog['name'] = 'Buddy'
dog['color'] = 'Brown'
dog['breed'] = 'Golden Retriever'
dog['legs'] = 4
dog['age'] = 5

# Create a student dictionary
student = {
    'first_name': 'John',
    'last_name': 'Doe',
    'gender': 'Male',
    'age': 20,
    'marital_status': 'Single',
    'skills': ['Python', 'Data Analysis'],
    'country': 'USA',
    'city': 'New York',
    'address': '123 Main Street'
}

# Get the length of the student dictionary
print("Length of student dictionary:", len(student))

# Get the value of skills and check the data type
skills = student['skills']
print("Skills:", skills)
print("Data type of skills:", type(skills))

# Modify the skills values by adding one or two skills
student['skills'].extend(['Machine Learning', 'Deep Learning'])
print("Updated skills:", student['skills'])

# Get the dictionary keys as a list
keys = list(student.keys())
print("Keys:", keys)

# Get the dictionary values as a list
values = list(student.values())
print("Values:", values)

# Change the dictionary to a list of tuples using items() method
tuples_list = list(student.items())
print("List of tuples:", tuples_list)

# Delete one of the items in the dictionary
del student['marital_status']
print("Dictionary after deleting marital_status:", student)

# Delete one of the dictionaries
del dog
print("Dog dictionary deleted.")
```
