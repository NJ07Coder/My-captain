# Python Program to Illustrate Different Set Operations

# Define two set variables
E = {0, 2, 4, 6, 8}
N = {1, 2, 3, 4, 5}

# Union - all elements from both sets
union_result = E | N
print(f"Union of E and N is {sorted(union_result)}")

# Intersection - common elements in both sets
intersection_result = E & N
print(f"Intersection of E and N is {sorted(intersection_result)}")

# Difference - elements in E but not in N
difference_result = E - N
print(f"Difference of E and N is {sorted(difference_result)}")

# Symmetric Difference - elements in either set but not in both
symmetric_diff_result = E ^ N
print(f"Symmetric difference of E and N is {sorted(symmetric_diff_result)}")
