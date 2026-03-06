
from ipp.exercises.labmodule05.WeatherData import WeatherData

class WeatherDataListener():
    def __init__(self):
        pass

    def handleIncomingWeatherData(self, data: WeatherData = None):
        if data:
            self._processWeatherData(wData = data)

    def _processWeatherData(self,wData: WeatherData = None):
        pass