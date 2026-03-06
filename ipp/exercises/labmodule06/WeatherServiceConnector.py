
import json
import requests
import ipp.common.ConfigConst as ConfigConst
from ipp.common.ConfigUtil import ConfigUtil
from ipp.exercises.labmodule05.LocationData import LocationData
from ipp.exercises.labmodule05.WeatherData import WeatherData
from ipp.exercises.labmodule06.WeatherDataParser import WeatherDataParser

class WeatherServiceConnector():
    # This label tells the app where to look in the settings file
    WEATHER_SVC_SECTION_NAME = "Settings.Weather"

    def __init__(self, dataParser: WeatherDataParser = None):
        """Step 1: The Constructor - Sets up the parser and starts the property search."""
        self.dataParser = dataParser
        self._initProperties()

    def _initProperties(self):
        """Step 2: The Setup - Loads all settings from the IppConfig.props file."""
        self.configUtil = ConfigUtil()
        
        # Load website address and identity settings
        self.baseUrl = \
            self.configUtil.getProperty( \
                WeatherServiceConnector.WEATHER_SVC_SECTION_NAME, "baseUrl")
        self.userAgent = \
            self.configUtil.getProperty( \
                WeatherServiceConnector.WEATHER_SVC_SECTION_NAME, "userAgent")
        self.contentType = \
            self.configUtil.getProperty( \
                WeatherServiceConnector.WEATHER_SVC_SECTION_NAME, "contentType")
        self.serviceName = \
            self.configUtil.getProperty( \
                WeatherServiceConnector.WEATHER_SVC_SECTION_NAME, "serviceName")
        
        # Load timing settings (how long to wait, how often to check)
        self.pollRate = \
            self.configUtil.getInteger( \
                WeatherServiceConnector.WEATHER_SVC_SECTION_NAME, "pollCycleSecs")
        self.requestTimeout = \
            self.configUtil.getInteger( \
                WeatherServiceConnector.WEATHER_SVC_SECTION_NAME, "requestTimeoutSecs")
        
        # Placeholders for the data we will eventually download
        self.latestRawData = None
        self.latestJsonData = None
        self.latestWeatherData = None

        self.clientSession = None
        self.isConnected = False

        print(f"Weather station name and URL -> {self.serviceName} {self.baseUrl}")

    # --- Step 3: Template Methods (To be filled in by future subclasses) ---

    def _createRequestUrl(self, stationID: str = None, locData: LocationData = None):
        """Placeholder for creating the specific URL for a city."""
        pass

    def _getLatestWeatherData(self, requestUrl: str = None, stationID: str = None, locData: LocationData = None) -> dict:
        """Placeholder for the actual download logic."""
        pass

    # --- Step 4: Connection Logic

    def connectToService(self) -> bool:
        """Starts the internet session and sets the ID headers."""
        try:
            self.clientSession = requests.Session()
            
            # Identify ourselves to the weather website
            self.clientSession.headers.update({
                'User-Agent': self.userAgent,
                'Accept': self.contentType
            })
            self.isConnected = True
            return True
        
        except Exception as e:
            print(f"Connection to {self.serviceName} Weather Service failed: {e}")
            return False
            
    def disconnectFromService(self) -> bool:
        """Closes the internet session to save memory."""
        print(f"Disconnecting from weather service {self.serviceName}...")

        if self.clientSession:
            self.clientSession.close()
            self.clientSession = None
            self.isConnected = False
            print(f"Disconnected from {self.serviceName} Weather Service")
            return True
            
        return False

    # --- Step 5: The Main Action (Fetching the Weather) ---

    def requestCurrentWeatherData(self, stationID: str = None, locData: LocationData = None) -> bool:
        """The main routine: Get URL -> Get Data -> Parse Data."""
        requestUrl = self._createRequestUrl(stationID = stationID, locData = locData)
        responseData = self._getLatestWeatherData(requestUrl = requestUrl, stationID = stationID, locData = locData)

        if responseData:
            self.latestRawData = responseData
            # Convert the raw data into a pretty JSON string
            self.latestJsonData = json.dumps(self.latestRawData, indent = 2)

            # If we have a parser, translate the raw data into a WeatherData object
            if self.dataParser:
                self.latestWeatherData = \
                    self.dataParser.parseWeatherData( \
                        rawData = responseData, stationID = stationID, stationName = locData.name)
            
            print(f"Successfully retrieved current weather data from URL: {requestUrl}")
            return True

        print(f"Failed to retrieve current weather data from URL: {requestUrl}")
        return False

    # --- Step 6: Helper Methods (The 'Information Desk') ---

    def getLatestWeatherData(self) -> WeatherData:
        return self.latestWeatherData
    
    def getLatestWeatherDataAsDict(self) -> dict:
        return self.latestRawData
    
    def getLatestWeatherDataAsJson(self) -> str:
        return self.latestJsonData
    
    def getPollRate(self) -> int:
        return self.pollRate
    
    def getRequestTimeout(self) -> int:
        return self.requestTimeout
    
    def getServiceName(self) -> str:
        return self.serviceName
    
    def getBaseUrl(self) -> str:
        return self.baseUrl
    
    def isClientConnected(self) -> bool:
        return self.isConnected