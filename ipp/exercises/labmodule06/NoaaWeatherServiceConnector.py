import json
import requests

from ipp.exercises.labmodule05.LocationData import LocationData
from ipp.exercises.labmodule06.NoaaWeatherDataParser import NoaaWeatherDataParser
from ipp.exercises.labmodule06.WeatherServiceConnector import WeatherServiceConnector

class NoaaWeatherServiceConnector(WeatherServiceConnector):

    def __init__(self):
        super().__init__(dataParser = NoaaWeatherDataParser())
 
    def _createRequestUrl(self, stationID: str = None, locData: LocationData = None):
        # GET https://api.weather.gov/stations/{station_id}/observations/latest
        return f"{self.baseUrl}/stations/{stationID}/observations/latest"

    def _getLatestWeatherData(self, requestUrl: str = None, stationID: str = None, locData: LocationData = None) -> dict:
        try:
            print(f"Requesting current weather observations: {requestUrl}")
            weatherResponse = self.clientSession.get(requestUrl, timeout = self.requestTimeout)
            
            if weatherResponse.status_code != 200:
                print(f"Failed to get weather data. Response code: HTTP {weatherResponse.status_code}")
                return None
            
            responseData = weatherResponse.json()
            
            # Add location information to the response
            # (NOAA may not include this, so it prob needs to be added)
            responseData['location'] = {
                'city': locData.city,
                'state': locData.region,
                'country': locData.country
            }

            responseData['geometry'] = {
                'coordinates': [locData.longitude, locData.latitude]
            }

            # Remove JSON-LD specific fields (we won't need them)
            latestRawData = responseData.copy()
            latestRawData.pop('@context', None)
            
            print(f"Successfully retrieved raw weather data")
            return latestRawData
            
        except requests.exceptions.Timeout:
            print(f"Request timed out")
            return None
        
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            return None
        
        except (KeyError, IndexError) as e:
            print(f"Unexpected response format: {e}")
            return None