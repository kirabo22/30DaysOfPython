# Tuple Exercises: Level 1

# Create an empty tuple
empty_tuple = ()

# Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
sisters = ('Alice', 'Mary', 'Sophia')
brothers = ('John', 'Michael', 'David')

# Join brothers and sisters tuples and assign it to siblings
siblings = sisters + brothers

# How many siblings do you have?
siblings_count = len(siblings)
print(f"I have {siblings_count} siblings.")

# Modify the siblings tuple and add the name of your father and mother and assign it to family_members
family_members = siblings + ('Father', 'Mother')
print("Family members:", family_members)

# Tuple Exercises: Level 2

# Unpack siblings and parents from family_members
*siblings, father, mother = family_members
print("Siblings:", siblings)
print("Father:", father)
print("Mother:", mother)

# Create fruits, vegetables and animal products tuples
fruits = ('apple', 'banana', 'orange')
vegetables = ('carrot', 'broccoli', 'spinach')
animal_products = ('milk', 'eggs', 'cheese')

# Join the three tuples and assign it to a variable called food_stuff_tp
food_stuff_tp = fruits + vegetables + animal_products
print("Food stuff (tuple):", food_stuff_tp)

# Change the food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
print("Food stuff (list):", food_stuff_lt)

# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list
middle_index = len(food_stuff_lt) // 2
if len(food_stuff_lt) % 2 == 0:
    middle_items = food_stuff_lt[middle_index-1:middle_index+1]
else:
    middle_items = food_stuff_lt[middle_index]
print("Middle item(s):", middle_items)

# Slice out the first three items and the last three items from food_stuff_lt list
first_three = food_stuff_lt[:3]
last_three = food_stuff_lt[-3:]
print("First three items:", first_three)
print("Last three items:", last_three)

# Delete the food_stuff_tp tuple completely
del food_stuff_tp

# Check if an item exists in tuple:
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')

# Check if 'Estonia' is a nordic country
is_estonia_nordic = 'Estonia' in nordic_countries
print("Is Estonia a Nordic country?", is_estonia_nordic)

# Check if 'Iceland' is a nordic country
is_iceland_nordic = 'Iceland' in nordic_countries
print("Is Iceland a Nordic country?", is_iceland_nordic)

