#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Get the user's name
user_name = input("Enter your name: ")

# Display the welcome message
print("Welcome, " + user_name + "!")


# Display the menu
print("Menu:")
print("1. Add Matrices")
print("2. Check Rotation")
print("3. Invert Dictionary")
print("4. Convert Matrix to Dictionary")
print("5. Check Palindrome")
print("6. Search for an Element & Merge Sort")
print("7. Exit")

# Get the user's choice
choice = input("Enter the number of your choice (1-7): ")

# Check the user's choice and perform the corresponding action
if choice == "1":
    # Implement the functionality for "Add Matrices"
    pass
elif choice == "2":
    # Implement the functionality for "Check Rotation"
    pass
elif choice == "3":
    # Implement the functionality for "Invert Dictionary"
    pass
elif choice == "4":
    # Implement the functionality for "Convert Matrix to Dictionary"
    pass
elif choice == "5":
    # Implement the functionality for "Check Palindrome"
    pass
elif choice == "6":
    # Implement the functionality for "Search for an Element & Merge Sort"
    pass
elif choice == "7":
    print("Goodbye, " + user_name + "!")
else:
    print("Invalid choice. Please select a number between 1 and 7.")

# You can add the actual functionality for each menu option as needed.




# Function to get a matrix from the user
def get_matrix(rows, columns, matrix_name):
    matrix = []
    print(f"Enter elements for {matrix_name} matrix:")
    for i in range(rows):
        row = []
        print(f"Enter elements of row {i + 1} (separated by space):")
        input_row = input().split()
        if len(input_row) != columns:
            print(f"Please enter exactly {columns} elements.")
            return None
        for element in input_row:
            row.append(int(element))
        matrix.append(row)
    return matrix

# Get the user's name
user_name = input("Enter your name: ")
print("Welcome, " + user_name + "!")

# Display the menu
print("Menu:")
print("1. Add Matrices")
print("2. Check Rotation")
print("3. Invert Dictionary")
print("4. Convert Matrix to Dictionary")
print("5. Check Palindrome")
print("6. Search for an Element & Merge Sort")
print("7. Exit")

# Get the user's choice
choice = input("Enter the number of your choice (1-7): ")

# Check the user's choice and perform the corresponding action
if choice == "1":
    # Implement the functionality for "Add Matrices"
    rows = int(input("Enter number of rows: "))
    columns = int(input("Enter number of columns: "))

    # Get the first matrix
    first_matrix = get_matrix(rows, columns, "first")
    if first_matrix is not None:
        # Get the second matrix
        second_matrix = get_matrix(rows, columns, "second")
        if second_matrix is not None:
            # Add the matrices
            result_matrix = []
            for i in range(rows):
                row = []
                for j in range(columns):
                    row.append(first_matrix[i][j] + second_matrix[i][j])
                result_matrix.append(row)

            # Display the result matrix
            print(f"Resulting matrix: {result_matrix}")
else:
    print("Invalid choice. Please select a number between 1 and 7.")

# Function to check if one matrix is a rotation of another
def is_rotation_matrix(matrix1, matrix2):
    if len(matrix1[0]) != len(matrix2) or len(matrix1) != len(matrix2[0]):
        return False

    # Transpose matrix1 to check if it's the same as matrix2
    transposed_matrix1 = [[matrix1[j][i] for j in range(len(matrix1))] for i in range(len(matrix1[0]))]

    return transposed_matrix1 == matrix2

# Function to input a matrix from the user
def input_matrix(rows, columns):
    matrix = []
    print(f"Enter elements for the matrix ({rows}x{columns}):")
    for i in range(rows):
        row = []
        print(f"Enter elements for row {i + 1} (separated by spaces):")
        input_row = input().split()
        if len(input_row) != columns:
            print(f"Please enter exactly {columns} elements for each row.")
            return None
        row = [int(element) for element in input_row]
        matrix.append(row)
    return matrix
# Check the user's choice and perform the corresponding action
if choice == "2":
    # Check Rotation Functionality
    rows1 = int(input("Enter number of rows for the first matrix: "))
    columns1 = int(input("Enter number of columns for the first matrix: "))

    rows2 = int(input("Enter number of rows for the second matrix: "))
    columns2 = int(input("Enter number of columns for the second matrix: "))

    first_matrix = input_matrix(rows1, columns1)
    second_matrix = input_matrix(rows2, columns2)

    if first_matrix is not None and second_matrix is not None:
        is_rotation = is_rotation_matrix(first_matrix, second_matrix)
        result = "are" if is_rotation else "are not"
        print(f"The two matrices {result} rotations of each other.")
else:
    print("Invalid choice. Please select a number between 1 and 7.")

# Function to invert a dictionary
def invert_dictionary(input_dict):
    inverted_dict = {}
    for key, value in input_dict.items():
        if value not in inverted_dict:
            inverted_dict[value] = key
        else:
            if isinstance(inverted_dict[value], list):
                inverted_dict[value].append(key)
            else:
                inverted_dict[value] = [inverted_dict[value], key]
    return inverted_dict
# Check the user's choice and perform the corresponding action
if choice == "3":
    # Invert Dictionary Functionality
    input_dict = {}
    print("Enter key-value pairs for the dictionary (format: key: value). Enter 'done' to finish.")

    while True:
        user_input = input()
        if user_input == "done":
            break
        try:
            key, value = user_input.split(":")
            input_dict[key.strip()] = value.strip()
        except ValueError:
            print("Invalid input. Please use the format: key: value")

    inverted_dict = invert_dictionary(input_dict)

    print("Before inverting:")
    print(input_dict)
    print("After inverting:")
    print(inverted_dict)
elif choice == "7":
    print("Goodbye, " + user_name + "!")
else:
    print("Invalid choice. Please select a number between 1 and 7.")

# Function to convert a matrix of user data into a dictionary
def matrix_to_dictionary(matrix):
    user_dict = {}
    for user_data in matrix:
        user_id = user_data[2]  # Assuming the ID is the third element in the user data
        user_info = user_data[:2] + user_data[3:]  # Exclude the ID
        user_dict[user_id] = user_info
    return user_dict
# Check the user's choice and perform the corresponding action
if choice == "4":
    # Convert Matrix to Dictionary Functionality
    user_data_matrix = []
    print("Enter user data (First Name, Last Name, ID, Job Title, Company) for each user.")
    print("Enter 'done' to finish.")

    while True:
        user_input = input()
        if user_input == "done":
            break
        user_data = user_input.split(", ")
        if len(user_data) != 5:
            print("Invalid input. Please provide all fields for each user.")
        else:
            user_data_matrix.append(user_data)

    user_dict = matrix_to_dictionary(user_data_matrix)
    print("Output:")
    print(user_dict)
elif choice == "7":
    print("Goodbye, " + user_name + "!")
else:
    print("Invalid choice. Please select a number between 1 and 7.")

# Recursive function to check if a string is a palindrome
def is_palindrome_recursive(s):
    # Base case: If the string has 0 or 1 character, it's a palindrome
    if len(s) <= 1:
        return True

    # Check if the first and last characters are the same
    if s[0] == s[-1]:
        # Recursively check the substring without the first and last characters
        return is_palindrome_recursive(s[1:-1])

    return False
# Check the user's choice and perform the corresponding action
if choice == "5":
    # Check Palindrome Functionality
    user_input = input("Enter a string: ")
    is_palindrome = is_palindrome_recursive(user_input)
    result = "is" if is_palindrome else "is not"
    print(f"The string '{user_input}' {result} a palindrome.")
elif choice == "7":
    print("Goodbye, " + user_name + "!")
else:
    print("Invalid choice. Please select a number between 1 and 7.")

# Custom sorting function (quicksort)
def custom_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    left = []
    right = []

    for item in arr[1:]:
        if item < pivot:
            left.append(item)
        else:
            right.append(item)

    return custom_sort(left) + [pivot] + custom_sort(right)

# Function to search for an element in a list, display its index, and sort the list
def search_and_sort_element(arr, element):
    index = -1  # Initialize index as -1 (not found)
    for i, item in enumerate(arr):
        if item == element:
            index = i
            break

    if index != -1:
        print(f"Element '{element}' found at index {index}.")
        sorted_list = custom_sort(arr)  # Sort the list using the custom sort function
        print("Sorted list:", sorted_list)
    else:
        print(f"Element '{element}' not found in the list.")
# Check the user's choice and perform the corresponding action
if choice == "6":
    # Search for an Element & Custom Sort Functionality
    user_input = input("Enter a list of elements separated by spaces: ").split()
    element = input("Enter the element to search for: ")

    search_and_sort_element(user_input, element)
elif choice == "7":
    print("Goodbye, " + user_name + "!")
else:
    print("Invalid choice. Please select a number between 1 and 7.")

# Custom sorting function (quicksort)
def custom_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    left = []
    right = []

    for item in arr[1:]:
        if item < pivot:
            left.append(item)
        else:
            right.append(item)

    return custom_sort(left) + [pivot] + custom_sort(right)

# Function to search for an element in a list, display its index, and sort the list
def search_and_sort_element(arr, element):
    index = -1  # Initialize index as -1 (not found)
    for i, item in enumerate(arr):
        if item == element:
            index = i
            break

    if index != -1:
        print(f"Element '{element}' found at index {index}.")
        sorted_list = custom_sort(arr)  # Sort the list using the custom sort function
        print("Sorted list:", sorted_list)
    else:
        print(f"Element '{element}' not found in the list.")



# In[ ]:




