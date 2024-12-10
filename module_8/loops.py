# Level 1

# 1. Iterate 0 to 10 using `for` and `while` loops
print("Iterate 0 to 10 using `for` loop:")
for i in range(11):
    print(i)

print("\nIterate 0 to 10 using `while` loop:")
i = 0
while i <= 10:
    print(i)
    i += 1

# 2. Iterate 10 to 0 using `for` and `while` loops
print("\nIterate 10 to 0 using `for` loop:")
for i in range(10, -1, -1):
    print(i)

print("\nIterate 10 to 0 using `while` loop:")
i = 10
while i >= 0:
    print(i)
    i -= 1

# 3. Print a triangle
print("\nPrint a triangle:")
for i in range(1, 8):
    print('#' * i)

# 4. Create a grid pattern
print("\nCreate a grid pattern:")
for i in range(8):
    print('# ' * 8)

# 5. Print multiplication pattern
print("\nPrint multiplication pattern:")
for i in range(11):
    print(f"{i} x {i} = {i * i}")

# 6. Iterate through a list and print items
print("\nIterate through a list and print items:")
tech_list = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for tech in tech_list:
    print(tech)

# 7. Print only even numbers from 0 to 100
print("\nPrint only even numbers from 0 to 100:")
for i in range(0, 101, 2):
    print(i)

# 8. Print only odd numbers from 0 to 100
print("\nPrint only odd numbers from 0 to 100:")
for i in range(1, 101, 2):
    print(i)

# Level 2

# 1. Sum of all numbers from 0 to 100
print("\nSum of all numbers from 0 to 100:")
total_sum = sum(range(101))
print(f"The sum of all numbers is {total_sum}")

# 2. Sum of even and odd numbers
print("\nSum of even and odd numbers from 0 to 100:")
even_sum = sum(i for i in range(101) if i % 2 == 0)
odd_sum = sum(i for i in range(101) if i % 2 != 0)
print(f"The sum of all evens is {even_sum}")
print(f"The sum of all odds is {odd_sum}")

# Level 3

# 1. Extract countries containing "land"
print("\nExtract countries containing 'land':")
from data.countries import countries  # Adjust import if necessary
land_countries = [country for country in countries if 'land' in country]
print(land_countries)

# 2. Reverse a fruit list
print("\nReverse a fruit list:")
fruit_list = ['banana', 'orange', 'mango', 'lemon']
reversed_list = []
for fruit in reversed(fruit_list):
    reversed_list.append(fruit)
print(reversed_list)

# 3. Total number of languages
print("\nTotal number of languages:")
from data.countries_data import countries_data  # Adjust import if necessary
languages = set()
for country in countries_data:
    languages.update(country['languages'])
print(f"Total number of languages: {len(languages)}")

# 4. Ten most spoken languages
print("\nTen most spoken languages:")
from collections import Counter
language_count = Counter()
for country in countries_data:
    for language in country['languages']:
        language_count[language] += 1
most_spoken_languages = language_count.most_common(10)
print(most_spoken_languages)

# 5. Ten most populated countries
print("\nTen most populated countries:")
most_populated_countries = sorted(countries_data, key=lambda x: x['population'], reverse=True)[:10]
for country in most_populated_countries:
    print(country['name'], country['population'])
