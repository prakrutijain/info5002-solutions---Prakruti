
"""
This program defines indoor temperature limits.
It sets the minimum and maximum allowed indoor temperatures
using floating-point values in degrees Fahrenheit.

"""

# Declare variables

min_indoor_temp_F = 65.0
max_indoor_temp_F = 85.0

# Declare function

def isDesiredIndoorTempRange(temp: float) -> bool:

    if temp >= min_indoor_temp_F and temp <= max_indoor_temp_F:
       # print(f"Input temperature (F) is within desired indoor range: {temp}")
        return True

  #  print(f"Input temperature (F) is outside of desired indoor range: {temp}")
    return False


desiredTemp = isDesiredIndoorTempRange(50.0)
desiredTemp = isDesiredIndoorTempRange(75.0)

if desiredTemp :
      print("It is  the correct range")
else :
     print("it is  the  not correct range")


# Create two temperature conversion functions - F to C and C to F

def convertTempFtoC(tempInF: float = 0.0):
    '''
    Converts the passed in Fahrenheit temperature to Celsius.
    Returns the result as a float.

    Algorithm: C = 5/9 x (F - 32)
    '''
    tempInC = (5 / 9) * (tempInF - 32)
    tempInC = round(tempInC, 1)

    print(f"{tempInF}°F is {tempInC}°C")

    return tempInC


def convertTempCtoF(tempInC: float = 0.0):
    '''
    Converts the passed in Celsius temperature to Fahrenheit.
    Returns the result as a float.

    Algorithm: F = C x (9/5) + 32
    '''
    tempInF = tempInC * (9 / 5) + 32
    tempInF = round(tempInF, 1)

    print(f"{tempInC}°C is {tempInF}°F")

    return tempInF

#Test run for above code

#convertTempFtoC(70)
#convertTempCtoF(21)

orig_f_val = 72.0
c_val = convertTempFtoC(orig_f_val)
f_val = convertTempCtoF(c_val)

print(f"Celsius = {c_val} and Farenheit = {f_val}. Original Farenheit is {orig_f_val}")

if (orig_f_val == f_val):
    print("The temp converter works!")
else:
    print("The temp converter failed!")