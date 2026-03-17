
import sys

fruitNames = ("apples", "peaches", "pineapples", "cherry", "blueberries", "oranges", "kiwi") #removed duplicates and made it a tuple since we won't be changing it.
fruitLocations = ("Massachusetts", "Georgia", "Hawaii", "Washington", "Maine", "Florida", "California")

def createDictionaryFromKeyValuePairs(names, locations):
    """
    """
    itemDict = None

    if names is not None and locations is not None:
        if len(names) == len(locations):  #This is the "Perfect Pair" check. A dictionary requires every key to have exactly one value.
            itemDict = {}               # If the lengths match, it creates an empty dictionary.

            print(f"Length of item names and item locations are the same. Creating dictionary of size {len(names)}")

            # --- UPDATED SECTION START ---
            for index, n in enumerate(names):   #using enumerate to get both the index and the name from the names list. 
                                                #This allows us to pull the corresponding location from 
                                                # the locations list using the same index.
                itemDict[n] = locations[index]

            # --- UPDATED SECTION END ---

        else:
            print(f"Can't create dictionary of names and locations. Lengths of lists are different.")

    return itemDict

def mergeDictionaries(*args):
    """
    Merges multiple dictionaries into a single dictionary containing all unique key-value pairs.
    """
    mergedDict = dict()
    #mergedDict = {}

    if (args and len(args) > 0):
        for arg in args:
            if (arg is not None):
                print(f"Merging dictionary into main dictionary with {len(arg)} items.")
                mergedDict = mergedDict | arg
                print(f"Newly merged dictionary: {mergedDict}")

        return mergedDict
    else:
        print("No dictionaries included in arguments to function. Ignoring.")

    return mergedDict

def addItemsToDictionary(itemDict, **kwargs):
    """
    While *args was an "expandable suitcase" for a list of items,
    **kwargs (Keyword Arguments) is like a "Box of Labeled Envelopes."
    It allows you to pass named arguments into a function, 
    like apples="fridge" or bananas="counter".
    Inside the function, Python turns these into a 
    dictionary where the name (k) is the Key and the assigned value (v) is the Value.
    """
    
    if itemDict is not None:
        if (kwargs and len(kwargs) > 0):
            for k, v in kwargs.items(): #This is how we open the envelopes. 
                                        #.items() gives us both the Key (k) 
                                        # and the Value (v) at the same time.

                if (k is not None and v is not None):
                    print(f"Adding key {k} and value {v} to dictionary of length {len(itemDict)} items.")
                    itemDict[k] = v      #The Core Action: This command tells the Dictionary to take the new key and value.
                    print(f"New dictionary length: {len(itemDict)}")
    
    return itemDict

def removeItemsFromDictionary(itemDict, *args):
    """
    Removes multiple items from a dictionary, if they exist. If a key doesn't exist, it is ignored.
    """
    if itemDict is not None:
        if (args and len(args) > 0):
            for arg in args:
                if (arg is not None):
                    print(f"Removing key {arg} from dictionary of length {len(itemDict)} items.")
                    
                    # NOTE: there are other ways, but this avoids raising an exception
                    # if 'arg' is not a key in the dictionary

                    itemDict.pop(arg, None)
                    print(f"New dictionary length: {len(itemDict)}")

    return itemDict


# --- THE COMMAND CENTER ---

def main():
    print("--- Starting SimpleDictionaries Lab ---")

    # Call Function 1: Create
    
    myFruitDict = createDictionaryFromKeyValuePairs(fruitNames, fruitLocations)
    print(f"Dictionary 1: {myFruitDict}\n")

    # Call Function 2: Merge
    # Adding a second dictionary with a duplicate key to see the overwrite
    moreFruits = {"apples": "New York"} 
    masterDict = mergeDictionaries(myFruitDict, moreFruits)
    print(f"After Merge (Apples moved to NY): {masterDict}\n")

    # Call Function 3: Add
    addItemsToDictionary(masterDict, dragonfruit="Vietnam")
    print(f"After Add: {masterDict}\n")

    # Call Function 4: Remove
    removeItemsFromDictionary(masterDict, "peaches")
    
    print("-" * 30)         #tried something new here to make the final output stand out more clearly
    print(f"FINAL TERMINAL OUTPUT: {masterDict}")
    print("-" * 30)

if __name__ == "__main__":
    main()