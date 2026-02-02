
def divideTwoNumbersWithExceptionHandling(numerator: int, denominator: int):
    try:
        result = (float) (numerator / denominator)
        print(f"Divided {numerator} by {denominator}: {result}")

        return result
    except ZeroDivisionError:
        print(f"Can't divide {numerator} by {denominator}: ZeroDivisionError!")

        return 0.0
    
    
divideTwoNumbersWithExceptionHandling(5,10.0)  #even if I put a float it accepts as an integer and gives the output