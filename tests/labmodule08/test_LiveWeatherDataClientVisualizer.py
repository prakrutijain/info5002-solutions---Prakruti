import logging
import unittest

from ipp.exercises.labmodule05.WeatherData import WeatherData
from ipp.exercises.labmodule05.LocationData import LocationData
from ipp.exercises.labmodule05.WeatherInfoContainer import WindData
from ipp.exercises.labmodule08.LiveWeatherDataClientVisualizer import LiveWeatherDataClientVisualizer

import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend so no window pops up during tests


class LiveWeatherDataClientVisualizerTest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        logging.basicConfig(format = '%(asctime)s:%(module)s:%(levelname)s:%(message)s', level = logging.DEBUG)
        logging.info("Testing LiveWeatherDataClientVisualizer class...")

    def setUp(self):
        self.visualizer = LiveWeatherDataClientVisualizer()

    def tearDown(self):
        pass

    # --- Helper Methods ---

    def _createTestWeatherData(self, stationID: str) -> WeatherData:
        """
        Creates a fake WeatherData object for testing.
        """
        weather = WeatherData()
        weather.location = LocationData()
        weather.location.nameID = stationID
        weather.temperature = 22.5
        weather.humidity    = 60.0
        weather.pressure    = 101325.0
        weather.wind        = WindData()
        weather.wind.speedKph = 15.0
        return weather

    # --- Test Methods ---

    def testHandleIncomingWeatherData(self):
        # send one weather data object and confirm it gets stored
        wData = self._createTestWeatherData("KBOS")
        self.visualizer.handleIncomingWeatherData(wData)

        self.assertIn("KBOS", self.visualizer.liveWeatherDataTable)

    def testHandleMultipleStations(self):
        # send data for 3 stations and confirm all are stored
        for station in ["KBOS", "KLGA", "KJFK"]:
            wData = self._createTestWeatherData(station)
            self.visualizer.handleIncomingWeatherData(wData)

        self.assertEqual(len(self.visualizer.liveWeatherDataTable), 3)
        self.assertIn("KBOS", self.visualizer.liveWeatherDataTable)
        self.assertIn("KLGA", self.visualizer.liveWeatherDataTable)
        self.assertIn("KJFK", self.visualizer.liveWeatherDataTable)

    def testWeatherDataValuesStoredCorrectly(self):
        # confirm the stored values match what was sent in
        wData = self._createTestWeatherData("KBOS")
        self.visualizer.handleIncomingWeatherData(wData)

        stored = self.visualizer.liveWeatherDataTable["KBOS"]
        self.assertEqual(stored.temperature, 22.5)
        self.assertEqual(stored.humidity, 60.0)
        self.assertEqual(stored.pressure, 101325.0)
        self.assertEqual(stored.wind.speedKph, 15.0)

    def testHandleNoneWeatherData(self):
        # sending None should not crash and table should stay empty
        self.visualizer.handleIncomingWeatherData(None)
        self.assertEqual(len(self.visualizer.liveWeatherDataTable), 0)