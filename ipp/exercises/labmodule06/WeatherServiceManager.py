import itertools
from apscheduler.schedulers.background import BackgroundScheduler

from ipp.common.ConfigUtil import ConfigUtil
from ipp.exercises.labmodule05.LocationData import LocationData
from ipp.exercises.labmodule05.WeatherData import WeatherData
from ipp.exercises.labmodule06.NoaaWeatherServiceConnector import NoaaWeatherServiceConnector
from ipp.exercises.labmodule06.WeatherDataListener import WeatherDataListener
from ipp.exercises.labmodule06.WeatherServiceConnector import WeatherServiceConnector

class WeatherServiceManager():
    def __init__(self):
        # Step 1: Initialize the background timer
        self.scheduler = BackgroundScheduler()
        self.isRunning = False
        self.dataListener = None
        self._initProperties()

    def _initProperties(self):
        # Step 2: Load settings from the .props file
        self.configUtil = ConfigUtil()
        self.weatherSvc = NoaaWeatherServiceConnector()
        self.clientSession = None
        self.isConnected = False

        # Get the list of cities (e.g., "KJFK, KBOS")
        self.pollStationIDs = \
            self.configUtil.getProperty( \
                WeatherServiceConnector.WEATHER_SVC_SECTION_NAME, "pollStationIDs")
        
        # Clean up the list into a Python list
        if self.pollStationIDs:
            self.pollStationList = [s.strip() for s in self.pollStationIDs.split(',')]
            print(f"Polling weather station ID's: {self.pollStationIDs}")
            self.pollStationCycle = itertools.cycle(self.pollStationList)
        else:
            self.pollStationIDs = "KBOS"
            self.pollStationList = ["KBOS"]
            self.pollStationCycle = itertools.cycle(self.pollStationList)
            print(f"No stations defined. Using default: {self.pollStationIDs}")

    def _scheduleAndStartWeatherServiceJob(self):
        # Step 3: Configure the background alarm
        pollRate = self.weatherSvc.getPollRate()
        self.scheduler.add_job( \
            func = self.processWeatherData, trigger = 'interval', \
            id = self.pollStationIDs, replace_existing = True, seconds = pollRate, \
            max_instances = 1, coalesce = True, misfire_grace_time = None)
        self.scheduler.start()

    def startManager(self):
        # Step 4: The "ON" button
        success = False
        if not self.isRunning:
            if not self.weatherSvc.isClientConnected():
                self.weatherSvc.connectToService()
            self._scheduleAndStartWeatherServiceJob()
            self.isRunning = True
            print("Weather station manager is now up and running!")
            success = True
        return success
    
    def stopManager(self):
        # Step 4: The "OFF" button
        if self.isRunning:
            if self.weatherSvc.isClientConnected():
                self.weatherSvc.disconnectFromService()
            self.scheduler.shutdown(wait = False)
            self.isRunning = False
            return True
        return False

    def _getLocationData(self, stationID: str = None):
        # Step 5: The "Cheat Sheet" for coordinates
        locData = LocationData()
        if stationID == "KJFK":
            locData.name, locData.city, locData.region = "JFK Airport", "New York", "NY"
            locData.latitude, locData.longitude = 40.63972, -73.77889
        elif stationID == "KORD":
            locData.name, locData.city, locData.region = "O'Hare Airport", "Chicago", "IL"
            locData.latitude, locData.longitude = 41.97861, -87.90472
        elif stationID == "KBOS":
            locData.name, locData.city, locData.region = "Logan Airport", "Boston", "MA"
            locData.latitude, locData.longitude = 42.3631, -71.0064
        else:
            locData.name = locData.city = stationID
            locData.latitude = locData.longitude = 0.0
        return locData

    def processWeatherData(self):
        # Step 6: The actual download and process logic
        stationID = next(self.pollStationCycle)
        locData = self._getLocationData(stationID = stationID)
        
        self.weatherSvc.requestCurrentWeatherData(stationID = stationID, locData = locData)
        jsonData = self.weatherSvc.getLatestWeatherDataAsJson()
        wData = self.weatherSvc.getLatestWeatherData()

        print(f"Data retrieved for {stationID}:\n{jsonData}\n")

        if self.dataListener:
            self.dataListener.handleIncomingWeatherData(data = wData)
        return jsonData

    def setListener(self, listener: WeatherDataListener = None):
        # Step 7: Plug in a display/listener
        if listener:
            self.dataListener = listener
            
    def isClientConnected(self):
        return self.isRunning 