
str1 = "hello"
print(len(str1)) #length of string

str2 = "World"
print(len(str2))

final_str = str1 + str2
final_str = str1 + " " + str2 #concatenation of string - it means to join two strings together

print(final_str)
print(len(final_str)) #length of final_str is 11 because of space

#ch = final_str[7] #indexing - it starts with 0 OR
print (final_str[7])

#Slicing - it is used to get a substring from a string
# str[starting_index:ending_index] - ending index is not included

substring = final_str[0:4] #it will give us "Hello"
print(substring)

#OR
substring = final_str[:5] #it will give us "Hello"
print(substring)

#OR
substring = final_str[6:] #it will give us "World"
print(substring)

#OR
substring = final_str[6:(len(final_str))] #it will give us "World"
print(substring) 

#Negative indexing - it starts with -1 from the end of the string

print(final_str[-1]) #it will give us "d"
print(final_str[:-5]) #it will give us "Hello"

#.endswitth() - it is used to check if a string ends with a specific substring
print(final_str.endswith("orld")) #it will give us True
print(final_str.endswith("llo")) #it will give us False

#capitalize() - it is used to convert the first character of a string to uppercase and the rest to lowercase

print(final_str.capitalize()) #it will give us "Hello world"

#replace() - it is used to replace a specific substring with another substring
print(final_str.replace("o", "a")) #it will give us "Hella Warld"

#find() - it is used to find the index of the first occurrence of a specific substring
print(final_str.find("o")) #it will give us 4
print(final_str.find("o", 5)) #it will give us 7 because it will start searching from index 5
print(final_str.find("x")) #it will give us -1 because "x" is not present in the string

#count() - it is used to count the number of occurrences of a specific substring in a string
print(final_str.count("o")) #it will give us 2
print(final_str.count("Hello")) #it will give us 1 because "Hello" is present in the string

#Practice - 1

name = input("Enter your name: ")
print("Length of your name is: " + str(len(name)))

#Practice - 2

dollar_count = "$I am the $ symbol $999"
print(dollar_count.count("$"))

#Conditional statements

age = 21
if age >= 18:
    print ("Can apply for a driving license and vote")

    #OR
    if(True):
        print ("Can apply for a driving license")
        print ("Can vote")

        #Elif statement - it is used to check multiple conditions
        # difference between if and elif is that if statement will check all 
        # the conditions even if one condition is true 
        # but elif will check the conditions until it finds a true condition and then it will stop checking the rest of the conditions

        light_color = "pink"

        if (light_color == "Red"):
            print("Stop")
        elif (light_color == "Yellow"):
            print("Ready")
        elif (light_color == "Green"):
            print("Go")

        else:
            print("Invalid light color")   

            print("")

    #Practice - 3

    marks = int(input("Enter students marks: "))
    if marks>= 90:
        Grade = "A"

    elif (marks>=80 and marks <= 90):
        Grade = "B"

    elif (marks>=70 and marks <= 80):
        Grade = "C" 
    else: 
        Grade = "D"
    print("Grade of the student is: " + Grade)
    print ("")

# Nesting
    age = 97
    if age >= 18:
        print ("Can apply for a driving license and vote")

        if age >= 80:
            print ("Cannot drive")
else:
    print ("Cannot apply for a driving license and vote") 
    print ("") 
    
#Practice - 4

num = int(input("Enter a number: ")) 

if (num % 2) == 0:
    print("EVEN")
else:
    print("ODD") 