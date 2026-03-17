import statistics

from typing import List

from exercises.labmodule05.CalculationsUtil import CalculationsUtil
from exercises.labmodule07.StatsData import StatsData

class StatsCalculationsUtil(CalculationsUtil):

    def __init__(self):
        pass

    @classmethod
    def calculateStats(cls, values: List[float]) -> StatsData:
        try:
            if not values:
                return {}

            stats = StatsData()

            stats.count  = len(values)
            stats.min    = min(values)
            stats.max    = max(values)
            stats.mean   = statistics.mean(values)
            stats.median = statistics.median(values)

            # Standard deviation requires at least 2 values
            if len(values) > 1:
                stats.standardDeviation = statistics.stdev(values)
            else:
                stats.standardDeviation = 0.0

            return stats

        except Exception as e:
            print(f"Error calculating statistics: {e}")
            return None