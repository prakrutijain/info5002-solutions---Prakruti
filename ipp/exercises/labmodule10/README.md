# Programming in Python - An Introduction: Lab Module 10

### Description

Briefly describe the objectives of the Lab Module:

1) Build a live Python application that fetches real retail sales data from the 
   US Census Bureau MRTS API and visualizes it as an interactive dashboard using 
   Plotly and Dash.

2) Implement a KNN (K-Nearest Neighbors) algorithm to predict next month's retail 
   sales per category based on 14 months of historical data stored locally in JSON format.

3) Apply the software design principles learned throughout the course — separation of 
   concerns, service connector pattern, data parsing, history collection, sorting, 
   and unit testing — into one complete, working application.


### Exercise Activities

List the actions you took in implementing the Lab Module:

1) Created 7 Python classes following the patterns learned in Lab Modules 06-09 — 
   RetailDataClient (service connector), RetailDataParser (data translator), 
   RetailHistoryCollector (JSON storage), RetailKnnPredictor (KNN algorithm), 
   RetailSorter (sorting), RetailDashApp (Plotly/Dash dashboard), and RetailApp 
   (top-level entry point).

2) Fetched 14 months of live retail sales data (January 2025 through February 2026) 
   from the US Census Bureau API, parsed and cleaned the raw JSON response, and saved 
   it to a local retail_history.json file for KNN training.

3) Built an interactive Dash dashboard running at localhost:8050 with a live ticking 
   clock, colorful bar chart, trend line chart, KNN prediction chart, and 4 sort 
   buttons — all updating automatically every 5 minutes.


### Unit and/or Integration Tests Executed

List the tests you exercised in validating your functionality for the Lab Module:

1) TestRetailDataParser — 9 unit tests verifying that raw Census API data is correctly 
   parsed, filtered, and translated into clean records. Tests cover correct category 
   names, correct values, filtering of unknown categories, non-seasonally adjusted rows, 
   wrong data types, and empty input handling.

2) TestRetailSorter — 7 unit tests verifying that sorting works correctly in all 
   directions. Tests cover alphabetical A→Z and Z→A sorting, value-based highest and 
   lowest first sorting, that the original list is not modified, empty list handling, 
   and correct output length.

3) TestRetailHistoryCollector and TestRetailKnnPredictor — 11 unit tests combined. 
   History tests verify saving, loading, duplicate prevention, and category filtering. 
   KNN tests verify predictions return correct types, handle insufficient data gracefully, 
   reject unknown categories, and produce reasonable values within expected ranges. 
   All 27 tests pass.


*Built with Python 3 · Data from US Census Bureau MRTS API · April 2026*