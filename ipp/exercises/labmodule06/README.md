# Programming in Python - An Introduction: Lab Module 06

### Description

Briefly describe the objectives of the Lab Module:
1) Learning Class Inheritance: Learned how to build a "Parent" class for general weather connections and then create a "Child" class that specifically handles the NOAA weather service rules.

2) Specializing Service Implementation: To implement a specific connector and data parser for the NOAA (National Oceanic and Atmospheric Administration) API. Learnt basic functions in code that could actually reach out to a real government website (api.weather.gov), download raw data, and translate that messy information into a clean report.

3) Managing Concurrency: To implement a background scheduler that automatically rotates through multiple weather stations (like KJFK, KBOS, and KORD) at a specific time interval without freezing the main application.

### Exercise Activities

List the actions you took in implementing the Lab Module:

1) Developed the Connector Hierarchy: Created the base WeatherServiceConnector class for session management and inherited from it to create the NoaaWeatherServiceConnector.

2) Implemented Data Parsing: Created the NoaaWeatherDataParser to extract specific weather metrics (temperature, wind, humidity) from the complex JSON response provided by the NOAA API.

3) Built the Orchestration Layer: Developed the WeatherServiceManager using the apscheduler library to handle automated background polling and station "cycling" using itertools.cycle.

4) Setting up the Tools: I had to manually install the requests library so my Python code could talk to the internet, and the apscheduler library so I could use a background timer.


### Unit and/or Integration Tests Executed

List the tests you exercised in validating your functionality for the Lab Module:

1) Connection Validation: Verified that connectToService() successfully established an HTTP session with the correct User-Agent headers and returned a 200 OK status.

2) Data Mapping Test: Confirmed that the NoaaWeatherDataParser correctly mapped raw JSON values into the WeatherData object attributes (e.g., ensuring Celsius values were correctly retrieved).

3) Scheduler Cycle Test: Validated that the WeatherServiceManager correctly moved from one station ID (e.g., KJFK) to the next (e.g., KORD) after each poll interval expired.

EOF.
