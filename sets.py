# Create an empty set
s = set()

# Add some elements
s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(3)
s.add(1)

# Remove 2 from the set
s.remove(2)

# Print the set
print(s)

# Find the size of the set
print(f"The set has {len(s)} elements.")

"""
    This is a python multi-line comment:
    Output:
    {1, 3, 4}
    The set has 3 elements.

    Notice how we cannot have multiple of the same value in a set!
"""
