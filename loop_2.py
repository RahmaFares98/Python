#Biggie Size - Given a list, write a function that
#changes all positive numbers in the list to"big".

def beggie_list (list):
    for i in range (len(list)):
        if list[i]>0:
            list[i]="big"
    return list
list=[1,2,0,-1,-2]
print(beggie_list(list))
# Given a list of numbers, create a function to replace the last value with the number of positive values. 
#(Note that zero is not considered to be a positive number).

def positive_value (list):
    count=0
    for i in range (len(list)):
        if list[i]>0:
            count+=1
    list[len(list)-1]=count
    return list
list=[1,2,4,5,0,-1,-2]
print(positive_value (list))
#Create a function that takes a list and returns the sum of all the values in the list.
def sum_Func (list):
    sum=0 
    for i in range (len(list)):
        sum+=list[i]
    return sum 
list=[1,2,4,5,0,-1,-2]
print(sum_Func (list))
#Create a function that takes a list and returns the average of all the values.
def avg_Func (list):
    sum=0 
    for i in range (len(list)):
        sum+=list[i]
        avg=sum/len(list)
    return avg 
list=[1,2,4,5,0,-1,-2]
print(avg_Func (list))

#Create a function that takes a list and returns the length of the list.
def list_length (list):
    return len(list)
list=[1,2,4,5,0,-1,-2]
print(list_length (list))
#Create a function that takes a list of numbers and returns the minimum value in the list.
# If the list is empty, have the function return False.
def min_value(list):
    min=0
    if (len(list)==0):
        return False
    for i in range (len(list)):
        if list[i]<min:
            min=list[i]
    return min
print(min_value (list=[1,2,4,6,7,0]))


#Create a function that takes a list and returns the maximum value in the list.
# If the list is empty, have the function return False.
def max_value(list):
    if (len(list)==0):
        return False
    max=list[0]
    for i in range (1,len(list)):
        if list[i]>max:
            max=list[i]
    return max
print(max_value (list=[1,2,4,6,9,8]))

#Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
def ultimate_analysis(lst):
    if len(lst) == 0:
        return False
    
    sumTotal = sum(lst)
    average = sumTotal / len(lst)
    minimum = min(lst)
    maximum = max(lst)
    length = len(lst)
    
    return {
        'sumTotal': sumTotal,
        'average': average,
        'minimum': minimum,
        'maximum': maximum,
        'length': length
    }
result = ultimate_analysis([37, 2, 1, -9])
print(result)
#Create a function that takes a list and return that list with values reversed. Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
def reverse_list(lst):
    left = 0
    right = len(lst) - 1
    while left < right:
        lst[left], lst[right] = lst[right], lst[left]
        left += 1
        right -= 1
    return lst
print(reverse_list([37, 2, 1, -9]))