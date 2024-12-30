# Set access
a = {1, 3, 5, 7, 9, 0}
print(type(a))  # Output the type of the set
print(len(a))   # Output the length of the set

a_list = list(a)
# Accessing elements by converting to a list
print(a_list[2])  # Access the element at index 2
print(a_list[-2]) # Access the element at index -2
print(a_list[1:4])  # Slice from index 1 to 4
print(a_list[:4])   # Slice from start to index 4
print(a_list[2:])   # Slice from index 2 to end
print(a_list[-4:-1]) # Slice from index -4 to -1