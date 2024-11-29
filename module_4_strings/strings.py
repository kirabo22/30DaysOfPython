# Concatenate strings to form a full sentence
sentence_1 = ' '.join(['Thirty', 'Days', 'Of', 'Python'])
print(sentence_1)  # Output: 'Thirty Days Of Python'

sentence_2 = ' '.join(['Coding', 'For', 'All'])
print(sentence_2)  # Output: 'Coding For All'

# Declare a variable and print it
company = "Coding For All"
print(company)  # Output: Coding For All

# Print the length of the company string
print(len(company))  # Output: 15

# Change characters to uppercase and lowercase
print(company.upper())  # Output: 'CODING FOR ALL'
print(company.lower())  # Output: 'coding for all'

# Format the string using capitalize, title, swapcase
print(company.capitalize())  # Output: 'Coding for all'
print(company.title())  # Output: 'Coding For All'
print(company.swapcase())  # Output: 'cODING fOR aLL'

# Slice out the first word of 'Coding For All'
first_word = company.split()[0]
print(first_word)  # Output: 'Coding'

# Check if 'Coding For All' contains the word 'Coding'
print('Coding' in company)  # Output: True

# Replace 'Coding' with 'Python'
new_company = company.replace('Coding', 'Python')
print(new_company)  # Output: 'Python For All'

# Replace 'Python for Everyone' with 'Python for All'
new_phrase = 'Python for Everyone'.replace('Everyone', 'All')
print(new_phrase)  # Output: 'Python for All'

# Split the string 'Coding For All'
split_company = company.split()
print(split_company)  # Output: ['Coding', 'For', 'All']

# Split the string "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
tech_companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(', ')
print(tech_companies)  # Output: ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# Find character at index 0
print(company[0])  # Output: 'C'

# Find the last index of the string
print(len(company) - 1)  # Output: 14

# Character at index 10
print(company[10])  # Output: 'A'

# Create acronyms
acronym_1 = ''.join([word[0].upper() for word in 'Python For Everyone'.split()])
acronym_2 = ''.join([word[0].upper() for word in 'Coding For All'.split()])
print(acronym_1)  # Output: 'PFE'
print(acronym_2)  # Output: 'CFA'

# Find the position of the first occurrence of C in 'Coding For All'
print(company.index('C'))  # Output: 0

# Find the position of the first occurrence of F in 'Coding For All'
print(company.index('F'))  # Output: 7

# Use rfind to find the position of the last occurrence of 'l' in 'Coding For All People'
print(company.rfind('l'))  # Output: 13

# Find the first occurrence of 'because' in the sentence
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.find('because'))  # Output: 35

# Find the last occurrence of 'because' in the sentence
print(sentence.rindex('because'))  # Output: 47

# Slice out 'because because because' from the sentence
sliced_phrase = sentence[35:67]
print(sliced_phrase)  # Output: 'because because because'

# Check if 'Coding For All' starts with 'Coding'
print(company.startswith('Coding'))  # Output: True

# Check if 'Coding For All' ends with 'coding'
print(company.endswith('coding'))  # Output: False

# Remove leading and trailing spaces from '   Coding For All      '
print('   Coding For All      '.strip())  # Output: 'Coding For All'

# Check which variables return True for isidentifier()
print('30DaysOfPython'.isidentifier())  # Output: True
print('thirty_days_of_python'.isidentifier())  # Output: True

# Join a list of libraries with hash and space
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(' # '.join(libraries))  # Output: 'Django # Flask # Bottle # Pyramid # Falcon'

# Use new line escape sequence
print("I am enjoying this challenge.\nI just wonder what is next.")

# Use tab escape sequence
print("Name\tAge\tCountry\tCity")
print("Asabeneh\t250\tFinland\tHelsinki")

# Use string formatting to display the area of a circle
radius = 10
area = 3.14 * radius ** 2
print(f"The area of a circle with radius {radius} is {area} meters square.")

# String formatting for various operations
print(f"8 + 6 = {8 + 6}")
print(f"8 - 6 = {8 - 6}")
print(f"8 * 6 = {8 * 6}")
print(f"8 / 6 = {8 / 6:.2f}")
print(f"8 % 6 = {8 % 6}")
print(f"8 // 6 = {8 // 6}")
print(f"8 ** 6 = {8 ** 6}")
