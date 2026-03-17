# Programming in Python - An Introduction: Lab Module 07

### Description

Briefly describe the objectives of the Lab Module:

1) Learn how to create data and utility classes that calculate and store
   statistical information (count, mean, median, min, max, and standard
   deviation) from a list of float values.

2) Learn how to work with files in Python by creating a FileUtil class
   that can read and write text files, and check if files and directories
   exist on the computer.

3) Learn how to convert Python objects to JSON format and back again,
   and how to save and load that data to and from files using the
   DataConverterUtil class.


### Exercise Activities

List the actions you took in implementing the Lab Module:

1) Created StatsData.py to store statistical results, and
   StatsCalculationsUtil.py to calculate statistics from a list of
   numbers using Python's built-in statistics library. Also wrote
   unit tests for both in the tests/labmodule07 directory.

2) Created FileUtil.py with class methods to read text files, write
   text files, and check whether a file or directory exists on the
   computer. Also wrote unit tests to verify each method works correctly.

3) Created DataConverterUtil.py with methods to convert WeatherData and
   StatsData objects to JSON strings and back, and to save and load
   those objects as JSON files using FileUtil. Also wrote unit tests
   to verify the conversions and file operations work correctly.


### Unit and/or Integration Tests Executed

List the tests you exercised in validating your functionality for the Lab Module:

1) Ran test_StatsData.py and test_StatsCalculationsUtil.py to verify
   that StatsData default and custom values are set correctly, and that
   StatsCalculationsUtil correctly calculates count, mean, median, min,
   max, and standard deviation from a list of numbers.

2) Ran test_FileUtil.py to verify that FileUtil can successfully write
   a text file, read it back, and correctly detect whether a file or
   directory exists on the computer.

3) Ran test_DataConverterUtil.py to verify that WeatherData and StatsData
   objects can be correctly converted to JSON and back, and that they
   can be saved to a file and loaded back with all values intact.

EOF.