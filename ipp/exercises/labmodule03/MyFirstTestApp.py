    

import sys
import SimpleTempConversion


def doWork():
    f_val = 72.0

    c_val = SimpleTempConversion.convertTempFtoC(f_val)

    print(f"Converted temperature values: F = {f_val}; C = {c_val}")


def main():
    print('Hello, world!')

    doWork()

    return 0


if __name__ == '__main__':
    sys.exit(main())