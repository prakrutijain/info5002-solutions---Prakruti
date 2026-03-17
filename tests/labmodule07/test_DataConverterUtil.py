
import logging
import unittest
import tempfile
import os

from typing import List

from ipp.exercises.labmodule05.WeatherData import WeatherData
from ipp.exercises.labmodule07.StatsData import StatsData
from ipp.exercises.labmodule07.DataConverterUtil import DataConverterUtil

class DataConverterUtilTest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        logging.basicConfig(format = '%(asctime)s:%(module)s:%(levelname)s:%(message)s', level = logging.DEBUG)
        logging.info("Testing DataConverterUtil class...")

    def setUp(self):
        pass

    def tearDown(self):
        pass

    # --- Helper Methods ---

    def _createTestStatsData(self) -> StatsData:
        sData = StatsData()
        sData.count = 5
        sData.mean = 55.0
        sData.median = 52.0
        sData.min = 25.0
        sData.max = 75.0
        sData.standardDeviation = 2.5
        return sData

    def _createTestWeatherData(self) -> WeatherData:
        wData = WeatherData()
        wData.temperature = 72.5
        wData.humidity = 65.0
        return wData

    def _createTestFileName(self, name: str) -> str:
        return os.path.join(tempfile.gettempdir(), name)

    # --- Test Methods ---

    def testStatsDataToJson(self):
        # convert a StatsData object to JSON string
        sData = self._createTestStatsData()
        jsonStr = DataConverterUtil.statsDataToJson(sData)

        # confirm it's a string and contains expected values
        self.assertIsInstance(jsonStr, str)
        self.assertIn("mean", jsonStr)
        self.assertIn("55.0", jsonStr)

    def testJsonToStatsData(self):
        # convert to JSON then back to object
        sData = self._createTestStatsData()
        jsonStr = DataConverterUtil.statsDataToJson(sData)
        result = DataConverterUtil.jsonToStatsData(jsonStr)

        # confirm values survived the round trip
        self.assertEqual(result.count, 5)
        self.assertEqual(result.mean, 55.0)
        self.assertEqual(result.median, 52.0)
        self.assertEqual(result.min, 25.0)
        self.assertEqual(result.max, 75.0)
        self.assertEqual(result.standardDeviation, 2.5)

    def testWeatherDataToJson(self):
        # convert a WeatherData object to JSON string
        wData = self._createTestWeatherData()
        jsonStr = DataConverterUtil.weatherDataToJson(wData)

        # confirm it's a string
        self.assertIsInstance(jsonStr, str)
        self.assertIn("temperature", jsonStr)

    def testJsonToWeatherData(self):
        # convert to JSON then back to object
        wData = self._createTestWeatherData()
        jsonStr = DataConverterUtil.weatherDataToJson(wData)
        result = DataConverterUtil.jsonToWeatherData(jsonStr)

        # confirm values survived the round trip
        self.assertEqual(result.temperature, 72.5)
        self.assertEqual(result.humidity, 65.0)

    def testWriteAndReadStatsDataFile(self):
        # write StatsData to file then read it back
        sData = self._createTestStatsData()
        fileName = self._createTestFileName("test_stats.json")

        writeResult = DataConverterUtil.writeStatsDataToFile(sData, fileName)
        self.assertTrue(writeResult)

        result = DataConverterUtil.readStatsDataFromFile(fileName)
        self.assertEqual(result.count, 5)
        self.assertEqual(result.mean, 55.0)

    def testWriteAndReadWeatherDataFile(self):
        # write WeatherData to file then read it back
        wData = self._createTestWeatherData()
        fileName = self._createTestFileName("test_weather.json")

        writeResult = DataConverterUtil.writeWeatherDataToFile(wData, fileName)
        self.assertTrue(writeResult)

        result = DataConverterUtil.readWeatherDataFromFile(fileName)
        self.assertEqual(result.temperature, 72.5)