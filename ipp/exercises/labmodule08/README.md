# Programming in Python - An Introduction: Lab Module 08

### Description

Briefly describe the objectives of the Lab Module:

1) Learn how to create a live data visualization dashboard using the
   matplotlib library that displays real-time weather data as bar charts
   for temperature, humidity, wind speed, and pressure across multiple
   weather stations.

2) Learn how to use threading and locks to safely handle data coming in
   from multiple weather stations at the same time, making sure the
   charts and the data storage don't conflict with each other.

3) Learn how to use matplotlib's FuncAnimation to automatically refresh
   and update charts every 2 seconds as new weather data arrives,
   creating a live updating dashboard experience.


### Exercise Activities

List the actions you took in implementing the Lab Module:

1) Created LiveWeatherDataClientVisualizer.py in the labmodule08
   directory. The class extends WeatherDataListener and sets up a
   matplotlib window with 4 bar charts arranged in a 2x2 grid showing
   temperature, humidity, wind speed, and pressure data.

2) Implemented the _processWeatherData() method to store incoming
   WeatherData objects in a dictionary indexed by station name, and
   the _updateVisualization() method to redraw all 4 charts every
   2 seconds using FuncAnimation.

3) Added a main block to the file that simulates live weather data
   for 3 stations (KBOS, KLGA, KJFK) using random values and a
   background thread, so the visualizer could be tested without
   needing a real weather API connection.


### Unit and/or Integration Tests Executed

List the tests you exercised in validating your functionality for the Lab Module:

1) Ran testHandleIncomingWeatherData to verify that when a WeatherData
   object is sent to the visualizer, it gets correctly stored in the
   liveWeatherDataTable dictionary under the right station name.

2) Ran testHandleMultipleStations to verify that weather data from
   all 3 stations (KBOS, KLGA, KJFK) can be stored simultaneously
   and none of the entries overwrite or conflict with each other.

3) Ran testHandleNoneWeatherData to verify that passing None into
   the visualizer does not cause a crash, and that the
   liveWeatherDataTable remains empty as expected.

EOF.