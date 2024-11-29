### Exercises: Level 1

# 1. Declare an empty list
empty_list = []

# 2. Declare a list with more than 5 items
items = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig']

# 3. Find the length of your list
length_of_items = len(items)

# 4. Get the first item, the middle item, and the last item of the list
first_item = items[0]
middle_item = items[len(items) // 2]
last_item = items[-1]

# 5. Declare a list called mixed_data_types
mixed_data_types = ['John Doe', 25, 5.8, 'Single', '123 Main St']

# 6. Declare a list variable named it_companies
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# 7. Print the list
print(it_companies)

# 8. Print the number of companies in the list
num_companies = len(it_companies)

# 9. Print the first, middle, and last company
first_company = it_companies[0]
middle_company = it_companies[len(it_companies) // 2]
last_company = it_companies[-1]

# 10. Print the list after modifying one of the companies
it_companies[1] = 'Alphabet'
print(it_companies)

# 11. Add an IT company to it_companies
it_companies.append('Tesla')

# 12. Insert an IT company in the middle of the companies list
it_companies.insert(len(it_companies) // 2, 'Spotify')

# 13. Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[0] = it_companies[0].upper()

# 14. Join the it_companies with a string '#; '
joined_companies = '#; '.join(it_companies)

# 15. Check if a certain company exists in the it_companies list
company_exists = 'Google' in it_companies

# 16. Sort the list using sort() method
it_companies.sort()

# 17. Reverse the list in descending order using reverse() method
it_companies.reverse()

# 18. Slice out the first 3 companies from the list
first_three = it_companies[:3]

# 19. Slice out the last 3 companies from the list
last_three = it_companies[-3:]

# 20. Slice out the middle IT company or companies from the list
middle_index = len(it_companies) // 2
if len(it_companies) % 2 == 0:
    middle_companies = it_companies[middle_index - 1:middle_index + 1]
else:
    middle_companies = [it_companies[middle_index]]

# 21. Remove the first IT company from the list
it_companies.pop(0)

# 22. Remove the middle IT company or companies from the list
if len(it_companies) % 2 == 0:
    del it_companies[middle_index - 1:middle_index + 1]
else:
    del it_companies[middle_index]

# 23. Remove the last IT company from the list
it_companies.pop()

# 24. Remove all IT companies from the list
it_companies.clear()

# 25. Destroy the IT companies list
del it_companies

# 26. Join the following lists
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
joined_list = front_end + back_end

# 27. Copy the joined list and insert Python and SQL after Redux
full_stack = joined_list[:]
full_stack.insert(full_stack.index('Redux') + 1, 'Python')
full_stack.insert(full_stack.index('Redux') + 2, 'SQL')

### Exercises: Level 2

# 1. List of student ages
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Sort the list and find the min and max age
ages.sort()
min_age = ages[0]
max_age = ages[-1]

# Add the min age and the max age again to the list
ages.extend([min_age, max_age])

# Find the median age
if len(ages) % 2 == 0:
    median_age = (ages[len(ages) // 2 - 1] + ages[len(ages) // 2]) / 2
else:
    median_age = ages[len(ages) // 2]

# Find the average age
average_age = sum(ages) / len(ages)

# Find the range of the ages
age_range = max_age - min_age

# Compare min-average and max-average
min_avg_diff = abs(min_age - average_age)
max_avg_diff = abs(max_age - average_age)

# 2. Find the middle country(ies)
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
if len(countries) % 2 == 0:
    middle_countries = countries[len(countries) // 2 - 1:len(countries) // 2 + 1]
else:
    middle_countries = [countries[len(countries) // 2]]

# 3. Divide countries list into two equal parts
mid_index = len(countries) // 2
if len(countries) % 2 == 0:
    first_half = countries[:mid_index]
    second_half = countries[mid_index:]
else:
    first_half = countries[:mid_index + 1]
    second_half = countries[mid_index + 1:]

# 4. Unpack first three countries and the rest as scandic countries
china, russia, usa, *scandic_countries = countries

