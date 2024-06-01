#  Create a function that accepts a number as an input. Return a new list that counts down by one,
# from the number (as the 0th element) down to 0 (as the last element).
def countdown_list(n):
    return list(range(n, -1, -1))
# Print list:
myList=(countdown_list(4))
print (myList)
# Create a function that will receive a list with two numbers.
# Print the first value and return the second.
def printreturn_list (list):
    print (list[0])
    return list[1]
printreturn_list (list=[15,9])
#Create a function that accepts a list
# and returns the sum of the first value in the list plus the list's length
def FirstPlusLength (list):
    sum =list[0]+ len(list)
    return sum
list=[6,3,5,20,1]
print( FirstPlusLength (list))
#Write a function that accepts a list and creates a new list 
#containing only the values from the original list that are greater than its 2nd value.
# Print how many values this is and then return the new list.
# If the list has less than 2 elements, have the function return False
def GreaterValues(list):
    if len(list) < 2:
        return False
    second_value = list[1]
    new_list = [i for i in list if i > second_value]
    print(new_list, "Number of values greater than the second value:", len(new_list))
    return new_list
GreaterValues([2])
#Write a function that accepts two integers as parameters: size and value.
# The function should create and return a list whose length is equal to the given size,
# and whose values are all the given value.
def size_value (size ,value):
    return [value]*size
print (size_value(7,5))
