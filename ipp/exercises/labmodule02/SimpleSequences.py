
# Test 1: string iteration

name = "Prakruti";
for c in name:
    print(c)
print()
# Test 2: list iteration and manipulation

class_items = ["notebook", "pen", "power supply"]
class_items.append("laptop")
for item in class_items:
    print(f"Item: {item}")
print()

# Test 3: tuple iteration (and failed manipulation)
immutable_class_items = ("notebook", "pen", "power supply")
for item in immutable_class_items:
    print(f"Item: {item }")

try:
    immutable_class_items.append("laptop")
except:
    print(f"Tuples are immutable! Can't append.")

for item in immutable_class_items:
    print(f"Item: {item}")

print()

# Test 4: range iteration

simple_range = range(10)
bounded_range = range(1,11)
stepwise_range = range(0,30,5)

for number in simple_range:
    print(f"Num: {number}")

print()

for number in bounded_range:
    print(f"Num: {number}")
    
print()

for number in stepwise_range:
    print(f"Num: {number}")