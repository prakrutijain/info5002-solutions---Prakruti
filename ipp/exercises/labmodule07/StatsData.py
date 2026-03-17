
from ipp.exercises.labmodule05.TimeAndDateUtil import TimeAndDateUtil

class StatsData():

    def __init__(self):
        self.count             = 0      # int
        self.mean              = 0.0    # float
        self.median            = 0.0    # float
        self.min               = 0.0    # float
        self.max               = 0.0    # float
        self.standardDeviation = 0.0    # float
        self.timestamp         = TimeAndDateUtil.getCurrentIso8601LocalDate()  # str