import json
import logging
from json import JSONEncoder
from typing import Optional

from ipp.exercises.labmodule07.FileUtil import FileUtil
from ipp.exercises.labmodule05.WeatherData import WeatherData
from ipp.exercises.labmodule07.StatsData import StatsData
from ipp.exercises.labmodule05.LocationData import LocationData
from ipp.exercises.labmodule05.WeatherInfoContainer import CloudLayerData, VisibilityData, WindData


class JsonDataEncoder(JSONEncoder):
    """
    Custom JSON encoder that converts Python objects to
    dictionaries so they can be serialized to JSON.
    """
    def default(self, o):
        return o.__dict__


class DataConverterUtil:
    """
    Utility class for converting WeatherData and StatsData objects
    to and from JSON format, and for saving and loading them as files.
    """

    def __init__(self):
        pass

    @classmethod
    def _createObjectFromDict(cls, data_dict: dict, obj_class):
        """
        Creates a new instance of obj_class and populates
        it with values from data_dict.

        Parameters:
            data_dict (dict): Dictionary containing the data.
            obj_class: The class to instantiate.

        Returns:
            A new populated instance of obj_class.
        """
        obj = obj_class()
        cls._updateData(data_dict, obj)
        return obj

    @classmethod
    def _updateData(cls, jsonStruct: dict, obj) -> None:
        """
        Copies key-value pairs from a dictionary onto
        the matching properties of an object.

        Parameters:
            jsonStruct (dict): Dictionary containing the data.
            obj: The object to update.
        """
        varStruct = vars(obj)

        for key in jsonStruct:
            if key in varStruct:
                setattr(obj, key, jsonStruct[key])
            else:
                logging.warning("JSON data contains key not mappable to object: %s", key)

    @classmethod
    def weatherDataToJson(cls, weatherData: WeatherData) -> str:
        """
        Converts a WeatherData object into a JSON string.

        Parameters:
            weatherData (WeatherData): The object to convert.

        Returns:
            str: A JSON formatted string.
        """
        return json.dumps(weatherData, cls=JsonDataEncoder, indent=2)

    @classmethod
    def jsonToWeatherData(cls, json_string: str) -> Optional[WeatherData]:
        """
        Converts a JSON string back into a WeatherData object,
        including all nested objects like location, wind, and visibility.

        Parameters:
            json_string (str): The JSON string to convert.

        Returns:
            WeatherData: A populated object, or None if an error occurred.
        """
        try:
            data_dict = json.loads(json_string)
            weatherData = WeatherData()

            # Map of nested object keys to their class types
            nested_objects = {
                'location': LocationData,
                'wind': WindData,
                'visibility': VisibilityData
            }

            # Handle nested objects
            for key, obj_class in nested_objects.items():
                if key in data_dict and isinstance(data_dict[key], dict):
                    nested_obj = obj_class()
                    cls._updateData(data_dict[key], nested_obj)
                    setattr(weatherData, key, nested_obj)
                    del data_dict[key]

            # Handle CloudLayerData list
            if 'cloudLayers' in data_dict and isinstance(data_dict['cloudLayers'], list):
                weatherData.cloudLayers = [
                    cls._createObjectFromDict(layer_dict, CloudLayerData)
                    for layer_dict in data_dict['cloudLayers']
                ]
                del data_dict['cloudLayers']

            # Update remaining simple properties
            cls._updateData(data_dict, weatherData)

            return weatherData

        except json.JSONDecodeError as e:
            logging.error(f"Error decoding JSON to WeatherData: {e}")
            return None
        except Exception as e:
            logging.error(f"Error converting JSON to WeatherData: {e}")
            return None

    @classmethod
    def statsDataToJson(cls, statsData: StatsData) -> str:
        """
        Converts a StatsData object into a JSON string.

        Parameters:
            statsData (StatsData): The object to convert.

        Returns:
            str: A JSON formatted string.
        """
        return json.dumps(statsData, cls=JsonDataEncoder, indent=2)

    @classmethod
    def jsonToStatsData(cls, json_string: str) -> Optional[StatsData]:
        """
        Converts a JSON string back into a StatsData object.

        Parameters:
            json_string (str): The JSON string to convert.

        Returns:
            StatsData: A populated object, or None if an error occurred.
        """
        try:
            data_dict = json.loads(json_string)
            statsData = StatsData()
            cls._updateData(data_dict, statsData)
            return statsData

        except json.JSONDecodeError as e:
            logging.error(f"Error decoding JSON to StatsData: {e}")
            return None
        except Exception as e:
            logging.error(f"Error converting JSON to StatsData: {e}")
            return None

    @classmethod
    def writeStatsDataToFile(cls, statsData: StatsData, fileName: str) -> bool:
        """
        Converts StatsData to JSON and saves it to a file.

        Parameters:
            statsData (StatsData): The object to save.
            fileName (str): The full path of the file to write to.

        Returns:
            bool: True if successful, False otherwise.
        """
        try:
            json_string = cls.statsDataToJson(statsData)
            return FileUtil.writeTextFile(fileName, json_string)
        except Exception as e:
            logging.error(f"Error writing StatsData to file '{fileName}': {e}")
            return False

    @classmethod
    def readStatsDataFromFile(cls, fileName: str) -> Optional[StatsData]:
        """
        Reads a JSON file and converts it into a StatsData object.

        Parameters:
            fileName (str): The full path of the file to read.

        Returns:
            StatsData: A populated object, or None if an error occurred.
        """
        try:
            json_string = FileUtil.readTextFile(fileName)
            if json_string is not None:
                return cls.jsonToStatsData(json_string)
            return None
        except Exception as e:
            logging.error(f"Error reading StatsData from file '{fileName}': {e}")
            return None

    @classmethod
    def writeWeatherDataToFile(cls, weatherData: WeatherData, fileName: str) -> bool:
        """
        Converts WeatherData to JSON and saves it to a file.

        Parameters:
            weatherData (WeatherData): The object to save.
            fileName (str): The full path of the file to write to.

        Returns:
            bool: True if successful, False otherwise.
        """
        try:
            json_string = cls.weatherDataToJson(weatherData)
            return FileUtil.writeTextFile(fileName, json_string)
        except Exception as e:
            logging.error(f"Error writing WeatherData to file '{fileName}': {e}")
            return False

    @classmethod
    def readWeatherDataFromFile(cls, fileName: str) -> Optional[WeatherData]:
        """
        Reads a JSON file and converts it into a WeatherData object.

        Parameters:
            fileName (str): The full path of the file to read.

        Returns:
            WeatherData: A populated object, or None if an error occurred.
        """
        try:
            json_string = FileUtil.readTextFile(fileName)
            if json_string is not None:
                return cls.jsonToWeatherData(json_string)
            return None
        except Exception as e:
            logging.error(f"Error reading WeatherData from file '{fileName}': {e}")
            return None