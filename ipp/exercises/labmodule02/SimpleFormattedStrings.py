
# Test 1: String append test
salutation = "Hello, World!"
new_salutation = salutation +  "Good to see you."
print (new_salutation)
print("New Salutation Length: ", len(new_salutation))


# Test 2: String multiplication test

lots_of_apples = "apples " *  4
print(lots_of_apples)

# Test 3: String formatting test

selling_apples = "{0} {1} {2}".format("i'm selling", lots_of_apples, "!")
print(selling_apples)
print(selling_apples.capitalize())

#Test 4 (string formatting w/ args)

school_info = "Location: {school}, {city}".format(school = "KV IIT POWAI", city = "MUMBAI")
print(school_info)

school_info = "Location: {school}, {city}, {state}".format(school = "KV IIT POWAI", city = "MUMBAI", state = "Maharashtra")
print(school_info)