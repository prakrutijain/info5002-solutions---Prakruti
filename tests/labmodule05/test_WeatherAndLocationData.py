
import logging
import unittest
import time
from datetime import datetime

# --- IMPORTS ---
from ipp.exercises.labmodule05.LocationData import LocationData
from ipp.exercises.labmodule05.TimeAndDateUtil import TimeAndDateUtil
from ipp.exercises.labmodule05.WeatherData import WeatherData

class WeatherAndLocationDataTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Sets up logging so we can see the test progress."""
        logging.basicConfig(format='%(asctime)s:%(module)s:%(levelname)s:%(message)s', level=logging.DEBUG)
        logging.info("Testing WeatherData and LocationData containers...")

    def testWeatherDataContainerDefaultValues(self):
        """Checks if a new WeatherData object starts with empty/zero values."""
        wData = WeatherData()
        isoTimeDate = TimeAndDateUtil.getCurrentIso8601LocalDate()
        
        self.assertEqual(wData.source, "")
        self.assertEqual(wData.url, "")
        self.assertEqual(wData.description, "")
        self.assertEqual(wData.temperature, 0.0)
        self.assertEqual(wData.humidity, 0.0)
        self.assertEqual(wData.pressure, 0.0)
        self.assertEqual(wData.windspeed, 0.0)

        # Ensure the timestamp created by the object is current (within 5 seconds)
        timestampA = datetime.fromisoformat(wData.timestamp).timestamp()
        timestampB = datetime.fromisoformat(isoTimeDate).timestamp()
        self.assertAlmostEqual(timestampA, timestampB, delta=5.0)
        
        self.assertIsNotNone(wData.location)

    def testWeatherDataContainerCustomValues(self):
        """Checks if WeatherData correctly stores values we manually assign."""
        isoTimeDate = TimeAndDateUtil.getCurrentIso8601LocalDate()
        locData = LocationData()
        wData = WeatherData()

        # Setting custom values
        wData.source = "test"
        wData.url = "https://www.example.com"
        wData.description = "My weather site."
        wData.timestamp = isoTimeDate
        wData.temperature = 15.0
        wData.humidity = 45.0
        wData.pressure = 1005.0
        wData.windspeed = 5.0
        wData.location = locData

        # Verifying they were saved
        self.assertEqual(wData.source, "test")
        self.assertEqual(wData.url, "https://www.example.com")
        self.assertEqual(wData.description, "My weather site.")
        self.assertEqual(wData.timestamp, isoTimeDate)
        self.assertEqual(wData.temperature, 15.0)
        self.assertEqual(wData.humidity, 45.0)
        self.assertEqual(wData.pressure, 1005.0)
        self.assertEqual(wData.windspeed, 5.0)
        self.assertEqual(wData.location, locData)

    def testLocationDataContainerDefaultValues(self):
        """Checks if LocationData starts with empty strings and 0.0 coordinates."""
        locData = LocationData()

        self.assertEqual(locData.name, "")
        self.assertEqual(locData.city, "")
        self.assertEqual(locData.region, "")
        self.assertEqual(locData.country, "")
        self.assertEqual(locData.latitude, 0.0)
        self.assertEqual(locData.longitude, 0.0)
        self.assertEqual(locData.elevation, 0.0)

    def testLocationDataContainerCustomValues(self):
        """Checks if LocationData saves custom names and coordinates."""
        locData = LocationData()

        locData.name = "My Location"
        locData.city = "Boston"
        locData.region = "MA"
        locData.country = "USA"
        locData.latitude = 42.36
        locData.longitude = -71.05

        self.assertEqual(locData.name, "My Location")
        self.assertEqual(locData.city, "Boston")
        self.assertEqual(locData.region, "MA")
        self.assertEqual(locData.country, "USA")
        self.assertEqual(locData.latitude, 42.36)
        self.assertEqual(locData.longitude, -71.05)

if __name__ == '__main__':
    unittest.main()