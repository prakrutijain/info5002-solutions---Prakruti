# Programming in Python - An Introduction: Lab Module 04

### Description

Briefly describe the objectives of the Lab Module:

1) Understand and Implement Collection Types: Gain hands-on experience with Python Sets and Dictionaries, focusing on their unique properties such as uniqueness of keys and unordered storage.

2) Master Flexible Function Arguments: Utilize *args and **kwargs to create versatile functions that can accept a variable number of positional and keyword arguments.

3) Develop Robust Logic: Practice "defensive programming" by implementing safety checks (like is not None and .pop(key, None)) to ensure the application does not crash when encountering missing or invalid data.


### Exercise Activities

List the actions you took in implementing the Lab Module:

1) Dynamic Dictionary Creation: Developed a function that pairs two separate collections (names and locations) into a single dictionary, handling the logic to ensure the data stays synchronized.

2) Dictionary Manipulation: Implemented functions to merge multiple dictionaries using the Union operator (|) and added items using keyword arguments to explore the **kwargs dictionary packing mechanism.

3) Exception-Free Operations: Created safe removal functions that allow for deleting items from sets and dictionaries without triggering KeyError or AttributeError exceptions.

### Unit and/or Integration Tests Executed

List the tests you exercised in validating your functionality for the Lab Module:

1) Duplicate Key Test: Changed "apples" to "cherries" in the source list and observed how the dictionary handles the mapping when duplicate names are present (verifying the last-in-wins rule).

2) Safety Removal Test: Executed removeItemsFromDictionary with a list containing both an existing key ("peaches") and a non-existent key ("pizza") to verify that the function completes without crashing.

3) Flexible Argument Test: Passed multiple dictionaries into the mergeDictionaries function simultaneously to confirm that the *args tuple was correctly unpacking and combining all data into a single master dictionary. 

EOF.

### Simple Sets -  

2 - IPP-DEV-04-002: Working with sets #68

## Question 1  to answer in the README.md: What's happening with this code?

This function 'createSetFromNames(names)' acts as a duplicate filter that takes a list of names and converts it into a Set.
It automatically removes any repeat items because Python Sets only allow unique values.
It includes a safety check (if names is not None) to ensure the program doesn't crash if the input list is empty or missing.

# Question 2 - Question to answer in the README.md: What's happening with this code? Specifically, what does *args do?

This function uses *args to accept multiple sets at once. It uses the Union (|) operator to merge them all into a single collection, automatically filtering out any duplicate names across all input groups. When another programmer sees *args, they immediately know, this function accepts a bunch of extra arguments.

# Question 3 - What's happening with this code? What would happen if you added one or more items of the same name?
addItemsToSet(nameSet, *args)

Creating a tool that needs two things: an existing set (nameSet) and any number of new items (*args) we want to add in.
Absolutely nothing changes in the set. Because a Set strictly enforces uniqueness. If awe try to add "Apple" to a set that already contains "Apple", the .add() function will simply ignore the request.

The code will still run.

The print statement will show up in your terminal.

But, the len(nameSet) (the count of items) will not increase.

# Question 4 - What's happening with this code? What would happen if you removed an item that doesn't exist in the set?

This function demonstrates safe deletion from a Set. By using the .discard() method instead of .remove(), the function can attempt to delete items that aren't present without triggering a KeyError or crashing the script.

# IPP-DEV-04-003: Working with dictionaries #69
# Question 1 - What's happening with this code? What are the potential issues with this code? How would you resolve these potential issues?

This function pairs two lists into a dictionary. While it works for unique keys, a primary risk is data loss if the names list contains duplicates, as Python dictionaries only store the final value assigned to a specific key. Using zip() is the recommended way to resolve manual indexing errors.

# Question 2 - What's happening with this code? Specifically, what does *args do? line by line explain
Without *args, I would have to define exactly how many dictionaries I want to merge (e.g., dict1, dict2).
With *args, the function can take one, two, ten, or zero dictionaries. It packs them all into a single tuple called args so the code can loop through them.
This function utilizes *args to accept a variable number of dictionary arguments. It iterates through each provided dictionary and uses the Merge Operator (|) to combine them into a single master dictionary. If keys overlap, the value from the dictionary being merged most recently will take precedence

# Question 3 - hat's happening with this code? What would happen if you added one or more items of the same name?
If I try to add a key that is already in the dictionary, Python will overwrite the old value with the new one.
The result:
The value will be updated to the newest one.
The len(itemDict) (total count) will not increase because I didn't add a new slot; I just changed what was inside an existing one.
This function uses **kwargs to allow for dynamic, named data entry into a dictionary. It demonstrates the overwriting behavior of dictionaries: if a provided key already exists, its value is updated, but the overall size of the dictionary remains the same

# Question 4 - What's happening with this code? What would happen if you removed an item that doesn't exist in the dictionary?

If I try to delete a key that isn't there using the del command or a standard .pop(), 
Python will throw a KeyError and stop your program immediately.

Because of that second argument (None) in itemDict.pop(arg, None):
If the key exists: It is removed, and the dictionary length decreases.

If the key is missing: Python says "I didn't find that," ignores it, and moves to the next item in the loop.