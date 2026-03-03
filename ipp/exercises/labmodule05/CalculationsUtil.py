
class CalculationsUtil():

    @classmethod
    def convertTempFtoC(cls, tempInF: float) -> float:
        """Converts Fahrenheit to Celsius."""
        # Formula: (F - 32) * 5/9
        return (tempInF - 32.0) * 5.0 / 9.0

    @classmethod
    def convertTempCtoF(cls, tempInC: float) -> float:
        """Converts Celsius to Fahrenheit."""
        # Formula: (C * 9/5) + 32
        return (tempInC * 9.0 / 5.0) + 32.0

    @classmethod
    def divideTwoNumbers(cls, numerator: float, denominator: float) -> float:
        """Divides two numbers with error handling for zero."""
        try:
            return float(numerator / denominator)
        except ZeroDivisionError:
            print(f"Can't divide {numerator} by {denominator}. ZeroDivisionError thrown.")
            return 0.0
        