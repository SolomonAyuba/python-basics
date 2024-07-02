# Creating sets

A = {1, 2, 3, 4}

B = {3, 4, 5, 6}



# Performing union

union_set = A | B

print("Union:", union_set)



# Performing intersection

intersection_set = A & B

print("Intersection:", intersection_set)

# Performing difference

difference_set = A - B

print("Difference:", difference_set)



# Performing symmetric difference

symmetric_difference_set = A ^ B

print("Symmetric Difference:", symmetric_difference_set)



# Checking subset and superset

is_A_subset_of_B = A.issubset(B)

is_A_superset_of_B = A.issuperset(B)

print("Is A a subset of B?", is_A_subset_of_B)

print("Is A a superset of B?", is_A_superset_of_B)



# Expected Output
#
# Union: {1, 2, 3, 4, 5, 6}
#
# Intersection: {3, 4}
#
# Difference: {1, 2}
#
# Symmetric Difference: {1, 2, 5, 6}
#
# Is A a subset of B? False
#
# Is A a superset of B? False