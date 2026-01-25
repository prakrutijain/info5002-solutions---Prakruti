
# Test 1: simple int calcs

picked_apples = 35
bagged_apples = 8
available_apples = picked_apples + bagged_apples

consumed_apples = 6
remaining_apples = available_apples - consumed_apples

print(f"Apples collected. Picked: {picked_apples}; Bagged: {bagged_apples}; Available: {available_apples}")
print(f"After eating some apples. Consumed: {consumed_apples}; Remaining: {remaining_apples}")

# Test 2: simple product calcs

shopping_trips = 3
apples_per_trip = 3
purchased_apples = shopping_trips * apples_per_trip
total_apples = remaining_apples + purchased_apples

print(f"Total Apples: {total_apples}; Purchased Apples: {purchased_apples}; Remaining: {remaining_apples}")

# Test 3: remainders

days_per_week = 7
daily_apples_for_week = int(total_apples / days_per_week)

left_over_apples_mod =  total_apples % days_per_week

left_over_apples_sub = total_apples - (daily_apples_for_week * days_per_week)

print(f"Apple Daily Consumption: {daily_apples_for_week}; Total_Apples: {total_apples}; Daily Apples For Week: {daily_apples_for_week}")
print(f"Left Over Apples: {left_over_apples_mod}; Left Over Apples: {left_over_apples_mod}")