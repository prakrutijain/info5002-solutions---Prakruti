
import sys

# This is a simple program to demonstrate the use of sets in Python. 
# Sets are collections of unique elements, and they can be used to
# perform various operations like union, intersection, and difference.

# 2 lists have at least 3 that are duplicates

fruitNamesA = ["apples", "peaches", "bananas", "apples", "blueberries", "bananas", "oranges", "oranges"]
fruitNamesB = ["apples", "oranges", "kiwi", "pineapple", "apples", "cherries", "cherries", "watermelon"]

def createSetFromNames(names):

    """
    Converts a list of names into a set to remove any duplicate entries.
    
    Args:
        names (list): A list of strings containing fruit names.
        
    Returns:
        set: A unique collection of names, or None if the input was empt
    """
    nameSet = None

    if names is not None:
        nameSet = set(names)

    return nameSet



def mergeSetNames(*args):      # creating a tool that can accept any number of inputs sets.
    
    """Merges multiple sets of names into a single set containing all unique names."""
# args - a variable-length argument list that allows you to pass any 
# number of sets to the function.

    mergedSet = set()

    if (args and len(args) > 0):    # check if there is actually something in the args list
        for arg in args:             #since there are multiple sets, lets pull them one at a time
                if (arg is not None):
                     print(f"Merging set into main set with {len(arg)} items.")
                mergedSet = mergedSet | arg
                print(f"Newly merged set: {mergedSet}")

        return mergedSet
    else:
        print("No sets included in arguments to function. Ignoring.")

    return mergedSet

def addItemsToSet(nameSet, *args):
    
    """Adds multiple items to a set, ensuring that all items remain unique."""
    
    if nameSet is not None:
        if (args and len(args) > 0):
            for arg in args:
                if (arg is not None):
                    print(f"Adding item {arg} to set of length {len(nameSet)} items.")
                    nameSet.add(arg)        #The Core Action: This command tells the Set to take the new item.
                    print(f"New set length: {len(nameSet)}") # print the new length of the set after adding the item
    
    return nameSet

def removeItemsFromSet(nameSet, *args):
    """
Removes multiple items from a set, if they exist. If an item doesn't exist, it is ignored.

    """
  
    if nameSet is not None:
        if (args and len(args) > 0):
            for arg in args:
                if (arg is not None):
                    print(f"Removing item {arg} from set of length {len(nameSet)} items.")

                    '''.remove("Apple"): If "Apple" isn't in the set, 
                    Python panics and crashes (throws a KeyError).
                    
                    .discard("Apple"): If "Apple" isn't in the set, 
                    Python just says, "Okay, it's not there anyway," and 
                    quietly moves on to the next line of code.'''

                    nameSet.discard(arg)  #The Core Action: This command tells the Set to look for the item and remove it.
                    print(f"New set length: {len(nameSet)}")

    return nameSet

# --- THE COMMAND CENTER ---

def main():
    print("--- Lab Module 04: Set Operations ---")

    # Step 1: Create Sets (Filters duplicates)
    setA = createSetFromNames(fruitNamesA)
    setB = createSetFromNames(fruitNamesB)
    print(f"Set A unique items: {setA}")

    # Step 2: Merge Sets (The Union)
    masterSet = mergeSetNames(setA, setB)
    print(f"Master Merged Set: {masterSet}")

    # Step 3: Add Items (Handles duplicates automatically)
    addItemsToSet(masterSet, "dragonfruit", "apples") 
    print(f"Set after adding dragonfruit: {masterSet}")

    # Step 4: Remove Items (Safe removal)
    removeItemsFromSet(masterSet, "peaches", "cheeku")
    print(f"Final Set: {masterSet}")

# --- THE START PROTOCOL ---
if __name__ == "__main__":
    main()