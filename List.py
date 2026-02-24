# Creating a list
numbers = [10, 20, 30, 40, 50]
print("Original list:", numbers)

# Accessing elements
print("First element:", numbers[0])       # Indexing
print("Last element:", numbers[-1])       # Negative indexing

# Slicing
print("First three elements:", numbers[:3])
print("Elements from index 2 onwards:", numbers[2:])

# Updating elements
numbers[1] = 25
print("After updating index 1:", numbers)

# Adding elements
numbers.append(60)        # Add at the end
numbers.insert(2, 15)     # Insert at index 2
print("After adding elements:", numbers)

# Removing elements
numbers.remove(40)        # Remove by value
popped = numbers.pop()    # Remove last element
print("After removing elements:", numbers)
print("Popped element:", popped)

# Searching
print("Index of 30:", numbers.index(30))
print("Is 50 in list?", 50 in numbers)

# Sorting and reversing
numbers.sort()
print("Sorted list:", numbers)
numbers.reverse()
print("Reversed list:", numbers)

# Useful functions
print("Length of list:", len(numbers))
print("Sum of elements:", sum(numbers))
print("Maximum element:", max(numbers))
print("Minimum element:", min(numbers))