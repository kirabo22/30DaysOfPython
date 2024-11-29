# Sets Exercises: Level 1

# Define the initial set of IT companies
it_companies = {"Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"}

# Find the length of the set it_companies
print("Length of it_companies:", len(it_companies))

# Add 'Twitter' to it_companies
it_companies.add("Twitter")
print("After adding Twitter:", it_companies)

# Insert multiple IT companies at once to the set it_companies
it_companies.update(["Intel", "Netflix", "Adobe"])
print("After adding multiple companies:", it_companies)

# Remove one of the companies from the set it_companies
it_companies.remove("Google")
print("After removing Google:", it_companies)

# What is the difference between remove and discard?
# `remove` raises an error if the item does not exist in the set, while `discard` does not raise an error.

# Sets Exercises: Level 2

# Define sets A and B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# Join A and B
union_set = A.union(B)
print("Union of A and B:", union_set)

# Find A intersection B
intersection_set = A.intersection(B)
print("Intersection of A and B:", intersection_set)

# Is A subset of B
is_subset = A.issubset(B)
print("Is A a subset of B?:", is_subset)

# Are A and B disjoint sets
are_disjoint = A.isdisjoint(B)
print("Are A and B disjoint?:", are_disjoint)

# Join A with B and B with A
A_with_B = A.union(B)
B_with_A = B.union(A)
print("A joined with B:", A_with_B)
print("B joined with A:", B_with_A)

# What is the symmetric difference between A and B
symmetric_diff = A.symmetric_difference(B)
print("Symmetric difference between A and B:", symmetric_diff)

# Delete the sets completely
del A, B

# Sets Exercises: Level 3

# Convert the ages to a set and compare the length of the list and the set
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages_set = set(ages)
print("Length of ages list:", len(ages))
print("Length of ages set:", len(ages_set))
print("The list is larger than the set:", len(ages) > len(ages_set))

# Explain the difference between the following data types:
# String: An immutable sequence of characters.
# List: A mutable, ordered collection of items.
# Tuple: An immutable, ordered collection of items.
# Set: An unordered collection of unique items.

# Find unique words in a sentence
sentence = "I am a teacher and I love to inspire and teach people."
unique_words = set(sentence.split())
print("Unique words in the sentence:", unique_words)
print("Number of unique words:", len(unique_words))
