# Initial data structures
x = [[5, 2, 3], [10, 8, 9]]
students = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]
sports_directory = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer': ['Messi', 'Ronaldo', 'Rooney']
}
z = [{'x': 10, 'y': 20}]

# Change the value 10 in x to 15
x[1][0] = 15

# Change the last_name of the first student from 'Jordan' to 'Bryant'
students[0]['last_name'] = 'Bryant'

# In the sports_directory, change 'Messi' to 'Andres'
sports_directory['soccer'][0] = 'Andres'

# Change the value 20 in z to 30
z[0]['y'] = 30

# Print the updated structures to verify changes
print(x)
print(students)
print(sports_directory)
print(z)

# Function to iterate through a list of dictionaries
def iterateDictionary(some_list):
    for dictionary in some_list:
        result = []
        for key, value in dictionary.items():
            result.append(f"{key} - {value}")
        print(", ".join(result))

# Call the function to test
iterateDictionary(students)

# Function to print values of a specific key from a list of dictionaries
def iterateDictionary2(key_name, some_list):
    for dictionary in some_list:
        if key_name in dictionary:
            print(dictionary[key_name])

# Call the function with 'first_name' and 'last_name'
iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)

# Function to print info from a dictionary with list values
def printInfo(some_dict):
    for key, values in some_dict.items():
        print(f"{key.upper()} ({len(values)})")
        for value in values:
            print(value)
        print()  # for a blank line between different categories

# Call the function to test
printInfo(sports_directory)
