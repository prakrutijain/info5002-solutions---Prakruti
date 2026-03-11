
import sys
import struct
from array import array

values = [2.99, 5.99, 3.99, 7.99, 1.99]

def displaySizingInfo(val):
    """Prints how a number looks to a computer (hex and binary)."""
    sampleBits = sys.getsizeof(val)
    sampleHex = val.hex()
    # This line converts the float into its raw binary "bits"
    sampleBin = struct.unpack('!I', struct.pack('!f', val))[0]        

    print(f" -> Sizing info: value = {val}, bits = {sampleBits}, hex = {sampleHex}, binary = {sampleBin:032b}")

def createItemPriceArrayUsingFloats():
    """Converts the list into an official 'array' and displays it."""
    itemPrices = array('f', values)

    print(itemPrices)
    print(itemPrices.tolist())

    for i, val in enumerate(itemPrices):
        displaySizingInfo(val)

    return itemPrices

def main():
    """The Command Center: This tells the program what to do first. """

    print("Starting Array Analysis...")
    print("_________________________")
    createItemPriceArrayUsingFloats()

# This is the "Start Button"
if __name__ == "__main__":
    main()