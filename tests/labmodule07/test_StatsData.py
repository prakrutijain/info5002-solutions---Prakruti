import logging
import unittest

from datetime import datetime

from ipp.exercises.labmodule05.TimeAndDateUtil import TimeAndDateUtil
from ipp.exercises.labmodule07.StatsData import StatsData

class StatsDataTest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        logging.basicConfig(format = '%(asctime)s:%(module)s:%(levelname)s:%(message)s', level = logging.DEBUG)
        logging.info("Testing StatsData class...")

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testStatsDataContainerDefaultValues(self):
        sData = StatsData()
        isoTimeDate = TimeAndDateUtil.getCurrentIso8601LocalDate()

        self.assertEqual(sData.count, 0)
        self.assertEqual(sData.mean, 0.0)
        self.assertEqual(sData.median, 0.0)
        self.assertEqual(sData.min, 0.0)
        self.assertEqual(sData.max, 0.0)
        self.assertEqual(sData.standardDeviation, 0.0)

        timestampA = datetime.fromisoformat(sData.timestamp).timestamp()
        timestampB = datetime.fromisoformat(isoTimeDate).timestamp()

        # assert they're within 5 seconds
        self.assertAlmostEqual(timestampA, timestampB, delta = 5.0)

    def testStatsDataContainerCustomValues(self):
        sData = StatsData()
        isoTimeDate = TimeAndDateUtil.getCurrentIso8601LocalDate()

        sData.count = 5
        sData.mean = 55.0
        sData.median = 52.0
        sData.min = 25.0
        sData.max = 75.0
        sData.standardDeviation = 2.5

        self.assertEqual(sData.count, 5)
        self.assertEqual(sData.mean, 55.0)
        self.assertEqual(sData.median, 52.0)
        self.assertEqual(sData.min, 25.0)
        self.assertEqual(sData.max, 75.0)
        self.assertEqual(sData.standardDeviation, 2.5)

        timestampA = datetime.fromisoformat(sData.timestamp).timestamp()
        timestampB = datetime.fromisoformat(isoTimeDate).timestamp()

        # assert they're within 5 seconds
        self.assertAlmostEqual(timestampA, timestampB, delta = 5.0)