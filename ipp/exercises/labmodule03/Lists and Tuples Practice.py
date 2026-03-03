
#Lists and Tuples Practice

#Lists

marks = [90, 80, 70, 60, 50]
print(marks)
print(type(marks))
print(marks[4]) #accessing the element at index 4
print(len(marks)) #length of the list
print("")

#List can also have string, int, float, boolean values, 
# Lists are mutable, accessible and changeable
# Strins are immutable, ARE accessible and NOT changeable

# Example 1 - lists

fruits = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]
print (fruits[2])
fruits [4] = "Fig"
print (fruits)
print("")

# Lists Slicing
# List_name [start_index : end_index : step] - ending index is not included

marks = [90, 80, 70, 60, 50]
print(marks[0:3])
print(marks[:2])
print(marks[2:])
print(marks[::2]) #it will give us every 2nd element from the list starting from index 0

# Negative indexing - it starts with -1 from the end of the list
print(marks[-3:-1]) #it will give us [70, 60] because it will start from index -3 and end at index -1 (not included)

# Lists Methods
# 1 - append() - it is used to add an element at the end of the list

marks.append(40)
print(marks)

#2 - sort() - it is used to sort the elements of the list in ascending order
 

print(marks.sort()) #it will give us None because sort() method does not return anything, it modifies the original list
print(marks)

# - sort(reverse = True) - it is used to sort the elements of the list in descending order

list = ["Banana", "Apple", "Cherry", "Date", "Elderberry"]

print(list.sort(reverse = True)) #it will give us None because sort() method does not return anything, it modifies the original list
print(list)

# Reverse() - it is used to reverse the order of the elements in the list

list.reverse()
print(list)

#insert() - insert element at a specific index - list.insert(index, element)
list.insert(2,"Fig")
print(list)
print("")

marks.insert(3,77)
print(marks)
print("")

#list.remove() - it is used to remove the FIRST occurrence of a specific element from the list
marks.remove(70)
print(marks)
print("")

#list.pop() - it is used to remove an element at a specific index and return the removed element
list.pop(2) #it will remove "Fig" from the list and return it
print(list)
print(list)
print("===End of Lists===")
print("")

#Search on GOOGLE  - PYHTON DOCUMENTATION - LIST METHODS


# TUPPLES are immutable sequence of values, ordered and allow duplicate values. 
# They are defined using parentheses ().

list = (1, 2, 3, 4, 5)
print(type(list))
print(list[0])
print ("")

# Empty Tuple
tup= ()
print(tup)
print(type(tup))
print("")

# tuple with one element - (element, ) - note the "comma" after the element - very important
#or it will be considered as an integer/float/string and not a tuple

tup1 = (1,)
tup3 = ("Hello",)
print(tup1, tup3)
print(type((tup1,tup3)))
print("")

tup2 = (1)
print(tup2)
print(type(tup2))
print("")

# Tuple Slicing - same as list slicing

tup = (1, 2, 3, 4, 5,2,2)
print(tup[:3])
print("")

# Tuple Methods
#tup.index(element) - it is used to find the index (place) of the first occurrence of a specific element in the tuple
tup.index(2)
print(tup.index(2))
## tup.count(element) - it is used to count the number of occurrences of a specific element in the tuple
tup.count(2)
print(tup.count(2))

# Practice question - 1

